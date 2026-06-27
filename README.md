# 📰 글로벌 신문 프런트 페이지 — 매일 자동 갱신 시스템

국내·미국 주요 경제·일간지의 1~3면을 매일 아침 자동으로 수집·번역·정리해
하나의 웹페이지로 보여줍니다. 데이터와 디자인이 분리되어 있어, 매일
`data.json`만 자동 교체되고 페이지 디자인은 그대로 유지됩니다.

## 구성 파일

| 파일 | 역할 |
|------|------|
| `index.html` | 고정 템플릿. 로딩 시 `data.json`을 읽어 카드를 그림 |
| `data.json` | 그날의 신문 데이터 (매일 자동 교체) |
| `update.js` | Claude API(웹 검색)로 기사 수집→정리→`data.json` 생성 |
| `.github/workflows/daily.yml` | 매일 오전 7시(KST) 자동 실행 + 배포 |
| `archive/` | 지난 날짜 `data.json` 자동 백업 |

## 동작 흐름

```
매일 07:00 KST
  → GitHub Actions 실행
    → update.js (Claude API 웹검색으로 기사 수집·번역·분류)
      → data.json 갱신 + archive 백업
        → git commit & push
          → GitHub Pages 자동 재배포
            → 같은 URL에서 최신 내용 확인
```

## 설치 단계

### 1. GitHub 저장소 생성
새 저장소(예: `daily-frontpage`)를 만들고 이 폴더의 모든 파일을 올립니다.

```bash
git init
git add .
git commit -m "초기 설정"
git branch -M main
git remote add origin https://github.com/<사용자명>/daily-frontpage.git
git push -u origin main
```

### 2. API 키를 Secret으로 등록
저장소 → **Settings → Secrets and variables → Actions → New repository secret**
- Name: `ANTHROPIC_API_KEY`
- Secret: 본인의 Anthropic API 키 (`sk-ant-...`)

> API 키는 https://console.anthropic.com 에서 발급합니다.
> 키는 절대 코드에 직접 적지 말고 반드시 Secret으로만 관리하세요.

### 3. GitHub Pages 활성화
저장소 → **Settings → Pages**
- Source: **GitHub Actions** 선택

### 4. 첫 실행 (수동 테스트)
저장소 → **Actions** 탭 → "매일 신문 프런트 페이지 갱신" → **Run workflow** 클릭.
완료되면 `https://<사용자명>.github.io/daily-frontpage/` 에서 확인할 수 있습니다.

이후로는 매일 오전 7시(KST)에 자동으로 갱신됩니다.

## 로컬에서 테스트하기

```bash
# 1) 데이터 생성
export ANTHROPIC_API_KEY=sk-ant-...
node update.js

# 2) 로컬 서버로 페이지 확인 (file:// 직접 열기는 fetch가 막힘)
npx serve .        # 또는  python3 -m http.server 8000
# 브라우저에서 http://localhost:8000 접속
```

## 커스터마이징

- **갱신 시각 변경**: `daily.yml`의 `cron: '0 22 * * *'` 수정 (UTC 기준, 22:00 UTC = 07:00 KST)
- **신문사 추가/변경**: `update.js`의 `PROMPT` 안에 매체명을 추가
- **비용 절감**: `update.js`의 `MODEL`을 `claude-sonnet-4-6`으로 교체
- **디자인 변경**: `index.html`의 `<style>`만 수정하면 됨 (데이터는 그대로)

## 비용 안내

하루 1회 실행 기준, 웹 검색 약 10~20회 + 응답 생성으로
대략 회당 수백 원 수준입니다. 정확한 단가는 Anthropic 콘솔의
현재 가격표를 확인하세요. (모델·검색 횟수에 따라 변동)

## 주의

- `data.json`의 내용은 검색 결과에 기반하지만, AI가 정리하는 과정에서
  부정확하거나 누락이 생길 수 있습니다. 중요한 의사결정 전에는 원문 확인을 권장합니다.
- 각 기사 전문이 아닌 헤드라인·요약만 다루므로 저작권 범위 내에서 운영하세요.
