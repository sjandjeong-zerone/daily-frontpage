#!/usr/bin/env node
/**
 * update.js
 * ─────────────────────────────────────────────────────────────
 * Claude API(웹 검색 도구 포함)를 호출해 그날의 국내·미국 주요
 * 경제·일간지 1~3면을 수집·번역·분류하고 data.json으로 저장한다.
 *
 * 실행:  ANTHROPIC_API_KEY=sk-... node update.js
 * 의존성: Node.js 18+ (내장 fetch 사용, 외부 패키지 불필요)
 * ─────────────────────────────────────────────────────────────
 */

const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ANTHROPIC_API_KEY;
if (!API_KEY) {
  console.error('❌ ANTHROPIC_API_KEY 환경변수가 없습니다.');
  process.exit(1);
}

const MODEL = 'claude-opus-4-8';           // 필요시 claude-sonnet-4-6 으로 교체 (저렴/빠름)
const OUT_PATH = path.join(__dirname, 'data.json');

// 오늘 날짜 (한국 시간 기준)
const now = new Date();
const kst = new Date(now.getTime() + 9 * 60 * 60 * 1000);
const yyyy = kst.getUTCFullYear();
const mm = String(kst.getUTCMonth() + 1).padStart(2, '0');
const dd = String(kst.getUTCDate()).padStart(2, '0');
const dateStr = `${yyyy}-${mm}-${dd}`;
const weekdays = ['일', '월', '화', '수', '목', '금', '토'];
const dateLabel = `${yyyy}년 ${Number(mm)}월 ${Number(dd)}일(${weekdays[kst.getUTCDay()]})`;

// ─── 출력 JSON 스키마를 프롬프트에 명시 ───
const SCHEMA_HINT = `
반드시 아래 JSON 구조로만 출력하세요. 코드펜스(\`\`\`)나 설명 문장 없이 순수 JSON만 출력합니다.

{
  "date": "${dateStr}",
  "dateLabel": "${dateLabel}",
  "generatedAt": "ISO8601 시각",
  "ticker": [ { "label": "코스피", "value": "8,721", "change": "▼2.34%", "dir": "dn", "badgeColor": "red" }, ... 8~12개 ],
  "keywords": [ { "label": "① 키워드명", "desc": "한 줄 요약" }, ... 5개 ],
  "sections": {
    "kor": {
      "label": "🇰🇷 국내 경제·일간지",
      "papers": [
        {
          "name": "신문사명", "url": "도메인",
          "pages": [
            { "label": "1면", "articles": [ { "headline": "한글 헤드라인", "url": "기사URL", "eng": "", "body": "2~3문장 요약" }, ... 3~5개 ] },
            { "label": "2면", "articles": [ ... ] },
            { "label": "3면", "articles": [ ... ] }
          ]
        }
      ]
    },
    "us": { "label": "🇺🇸 미국 경제·일간지", "papers": [ ... ] }
  }
}

규칙:
- 국내지: 경향신문, 동아일보, 매일경제, 한국경제 (각 1·2·3면)
- 미국지: Wall Street Journal, Bloomberg, The New York Times, Washington Post, Financial Times (각 1·2·3면)
- ⚠️ 절대 규칙: 각 신문의 pages 배열 길이는 정확히 3이어야 합니다 (1면, 2면, 3면). 1개나 2개만 넣는 것은 허용되지 않습니다.
- 각 면마다 articles 배열에 3~5개의 기사를 포함합니다 (대표 기사 1건 + 부기사 2~4건).
- 미국지는 "eng"에 원문 영어 헤드라인을 넣고 "headline"은 한글 번역으로 채웁니다.
- "dir"은 상승 up / 하락 dn / 보합 neu 중 하나.
- "badgeColor"는 blue, green, purple, orange, teal, pink, red, amber, gray 중 하나.
- 모든 텍스트는 실제 검색된 그날 기사에 근거해야 하며, 추측·창작 금지.
- 출력 직전 자체 검증: sections.kor.papers[N].pages.length === 3 && sections.us.papers[N].pages.length === 3 인지 확인하세요.
`;

const PROMPT = `오늘은 ${dateLabel}입니다. 웹 검색을 사용해 오늘(또는 가장 최근 발행분) 자
국내 주요 경제·일간지(경향신문·동아일보·매일경제·한국경제)와
미국 주요 경제·일간지(WSJ·Bloomberg·NYT·Washington Post·Financial Times)의
1면·2면·3면 주요 기사를 수집하세요.

각 면마다 3~5건의 주요 기사(대표 헤드라인 + 부기사)를 정리하고,
미국 매체 헤드라인은 한글로 번역하되 원문도 함께 보존하세요.
또한 오늘의 주요 시장 지표(코스피·환율·S&P500·나스닥 등)와
국내외를 관통하는 공통 키워드 5개를 뽑아주세요.

충분히 검색(최소 15~30회)한 뒤, 마지막에 ${SCHEMA_HINT}`;

async function main() {
  console.log(`📡 ${dateLabel} 신문 데이터 수집 시작…`);

  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      'x-api-key': API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: 32000,
      tools: [{ type: 'web_search_20250305', name: 'web_search', max_uses: 30 }],
      messages: [{ role: 'user', content: PROMPT }]
    })
  });

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`API 오류 ${res.status}: ${txt}`);
  }

  const data = await res.json();

  // 응답에서 텍스트 블록만 모아 JSON 파싱
  const text = (data.content || [])
    .filter(b => b.type === 'text')
    .map(b => b.text)
    .join('\n')
    .trim();

  // 코드펜스가 섞여 있을 경우 제거 + 첫 { ~ 마지막 } 추출
  const cleaned = text.replace(/```json|```/g, '').trim();
  const start = cleaned.indexOf('{');
  const end = cleaned.lastIndexOf('}');
  if (start === -1 || end === -1) {
    throw new Error('JSON을 응답에서 찾지 못했습니다.\n원문:\n' + text.slice(0, 800));
  }

  const jsonStr = cleaned.slice(start, end + 1);
  let parsed;
  try {
    parsed = JSON.parse(jsonStr);
  } catch (e) {
    throw new Error('JSON 파싱 실패: ' + e.message + '\n추출 문자열 앞부분:\n' + jsonStr.slice(0, 800));
  }

  // 안전장치: 필수 키 검증
  if (!parsed.sections || !parsed.sections.kor || !parsed.sections.us) {
    throw new Error('스키마 검증 실패: sections.kor / sections.us 누락');
  }
  parsed.generatedAt = parsed.generatedAt || new Date().toISOString();

  // ⚠️ 페이지 수 검증: 각 신문이 3면(1면·2면·3면)을 모두 가지고 있는지 확인
  const allPapers = [
    ...(parsed.sections.kor?.papers || []),
    ...(parsed.sections.us?.papers || [])
  ];
  for (const paper of allPapers) {
    if (!paper.pages || paper.pages.length !== 3) {
      throw new Error(
        `페이지 수 검증 실패: "${paper.name}"의 pages 배열 길이가 ${
          paper.pages ? paper.pages.length : 0
        }입니다. 3이어야 합니다 (1면·2면·3면).`
      );
    }
  }

  // 기존 파일 백업(아카이브)
  if (fs.existsSync(OUT_PATH)) {
    const archiveDir = path.join(__dirname, 'archive');
    if (!fs.existsSync(archiveDir)) fs.mkdirSync(archiveDir);
    try {
      const prev = JSON.parse(fs.readFileSync(OUT_PATH, 'utf8'));
      if (prev.date) {
        fs.copyFileSync(OUT_PATH, path.join(archiveDir, `data-${prev.date}.json`));
      }
    } catch (_) { /* 백업 실패는 무시 */ }
  }

  fs.writeFileSync(OUT_PATH, JSON.stringify(parsed, null, 2), 'utf8');
  console.log(`✅ data.json 갱신 완료 (${parsed.date}) — ${OUT_PATH}`);
}

main().catch(err => {
  console.error('❌ 실행 실패:', err.message);
  process.exit(1);
});
