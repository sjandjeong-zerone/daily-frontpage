#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, datetime

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

headline = "구글 쇼크에 코스피 5,730·반도체 급락…내일 美 중간선거·제니엘 전사전략회의, 삼성전자 30조 배당·SK하이닉스 특별배당"

data = {
    "date": "2026-11-02",
    "dateLabel": "2026년 11월 2일(월요일)",
    "generatedAt": now.isoformat(timespec="seconds"),
    "ticker": [
        {"name": "KOSPI", "value": "5,730.74", "change": "▼3.48%", "dir": "down"},
        {"name": "KOSDAQ", "value": "724.38", "change": "▼3.83%", "dir": "down"},
        {"name": "S&P 500", "value": "7,720.39", "change": "▼0.30%", "dir": "down"},
        {"name": "나스닥 100", "value": "-", "change": "▼3.5%", "dir": "down"},
        {"name": "다우", "value": "52,342.56", "change": "▼0.25%", "dir": "down"},
        {"name": "삼성전자", "value": "-", "change": "▼3.02%", "dir": "down"},
        {"name": "SK하이닉스", "value": "-", "change": "▼7.08%", "dir": "down"},
        {"name": "원/달러", "value": "1,334.20원", "change": "-", "dir": "down"},
    ],
    "keywords": [
        {"label": "① '구글 쇼크' — 알파벳 -12%·터보퀀트 공개에 반도체 직격", "desc": "구글 AI 압축 알고리즘 '터보퀀트' 공개로 메모리 수요 우려 확산, 알파벳 -12.64%(283.82달러) 사상 최악. 코스피 5,730.74(-3.48%) 급락, 필라델피아 반도체 -7.2% 200일선 이탈"},
        {"label": "② 美 중간선거 D-1 — 민주당 '블루 웨이브' 기대감", "desc": "RCP 여론조사 민주당 제네릭 투표 8.2p 리드. 트럼프는 민주당 장악 시 '거부권 적극 행사' 예고. 역사적 중간선거 전후 랠리 통계와 충돌"},
        {"label": "③ 애플·AMD·팔란티어 실적 주간 — AI 테마 향방 가른다", "desc": "애플(11/2 장마감 후)·팔란티어(11/2)·AMD(11/3) 실적 발표. AI 투자 피로감 속 기술주 향방의 분수령"},
        {"label": "④ 삼성전자 30조 배당·SK하이닉스 특별배당", "desc": "올해 합산 영업익 640조 전망, 주주환원 190~210조 규모. 주가는 '구글 쇼크'에 부진(삼성전자 -3.02%·SK하이닉스 -7.08%)"},
        {"label": "⑤ 호르무즈 협상 D-3·10월 美 NFP(금요일)", "desc": "미국-이란 도하 간접협상 3일째, 유가 하락. 10월 비농업 고용 예상 55,000건·실업률 4.2% 발표 대기"},
    ],
    "morning": {
        "date": "2026-11-02",
        "headline": headline,
        "weather": "🌥️ 흐림 · 11°C (체감 10°C) · 습도 77% · 바람 4km/h",
        "schedule": "없음 (오늘 포커스: Z-P2 전사전략회의 최종준비 + Z-P6 AI tool 파일럿 테스트 공지)",
        "domestic": {
            "kospi": {"value": "5,730.74", "change": "▼ -206.92", "changeRate": "-3.48%", "rate": "-3.48%"},
            "kosdaq": {"value": "724.38", "change": "▼ -28.85", "changeRate": "-3.83%", "rate": "-3.83%"},
            "supply": {
                "foreign": "외국인 1.6조 순매도",
                "institution": "연기금 8,929억 순매수로 낙폭 방어",
                "individual": "개인 순매수 방어",
                "usdkrw": "1,334.20원",
                "change": "전일 대비 약보합"
            },
            "comment": "코스피가 '구글 쇼크'(알파벳 -12%) 여파로 5,730.74(-3.48%, -206.92p) 급락 마감했다. 장중 5,599까지 추락하며 매도 측 서킷브레이커가 발동됐고, 삼성전자 -3.02%·SK하이닉스 -7.08% 등 반도체 대형주가 급락했다. 외국인 1.6조 순매도에 연기금 8,929억 순매수가 낙폭을 방어했다. 원/달러는 1,334.20원으로 약보합 마감했다."
        },
        "overseas": {
            "dow": {"value": "52,342.56", "change": "▼ -0.25%", "changeRate": "-0.25%"},
            "sp500": {"value": "7,720.39", "change": "▼ -0.30%", "changeRate": "-0.30%"},
            "nasdaq": {"value": "나스닥 100", "change": "▼ -3.5%", "changeRate": "-3.5%"},
            "oil": {
                "wti": "협상 진전에 하락",
                "brent": "미-이란 협상 타결 소식에 하락",
                "note": "미국-이란 호르무즈 협상 진전으로 국제유가 하락. 알파벳 -12%+ '구글 쇼크'에 필라델피아 반도체 -7.2%(200일선 이탈), 나스닥 100 -3.5%. BOJ 금리 1.25% 동결(8:1)·ETF 매도 확대 방침."
            },
            "keyStocks": "미국 증시는 알파벳 -12%+ 급락(시총 5,000억 달러 증발)으로 '구글 쇼크'가 발생했다. S&P 500은 7,720.39(-0.30%)로 선방했지만 나스닥 100 -3.5%, 필라델피아 반도체 -7.2%(200일선 이탈)로 기술주·반도체 쇼크가 집중됐다. 아마존·인텔 실적 후 약세, BOJ 금리 1.25% 동결(8:1)에 ETF 매도 확대 방침. 닛케이 63,290.11(-2.12%)."
        },
        "topNews": headline,
        "otherNews": [
            "FBI, 바이낸스 63억달러(8.4조원) 해킹 '북한 소행' 공식 확인 — 정예 해킹조직 TraderTraitor 지목",
            "이재명 대통령, 2일 시정연설 — 내년 역대 최대 821조원(820조9,000억) 예산안 설득",
            "에르도안 튀르키예 대통령 2~4일 국빈 방한 — 3일 이재명 대통령과 정상회담",
            "한국거래소, 저PBR 기업 151곳 첫 공개 — 이마트·현대제철·한화생명 등 증권사 앱에 '꼬리표'",
            "호르무즈 협상 D-3 진전 — 국제유가 하락, 10월 美 NFP(금요일) 예상 55,000건·실업률 4.2%",
        ],
        "email": {
            "google": "sjandjeong@gmail.com — Gmail 데이터 미확보",
            "note": "🟢 오늘 모닝브리핑 주요 뉴스는 구글 쇼크·美 중간선거 D-1·삼성전자 30조 배당 등. ⚪ Gmail 데이터 수집 오류로 미확보."
        },
        "insight": "💡 11월 첫 주, 두 개의 분수령이 겹쳤다\n\n내일(3일) 美 중간선거와 제니엘 전사전략회의 — 규모는 다르지만 '방향을 결정하는 회의'라는 점에서 같습니다. 지난주 '구글 쇼크'(알파벳 -12%)로 AI 투자 피로감이 시장에 확산됐고, 이번 주 애플·AMD·팔란티어 실적이 AI 테마의 내년 방향을 가를 변수입니다.\n\n제니엘 AX 추진에도 'AI tool 파일럿 테스트 공지'가 오늘 과제입니다. 시장 전체의 AI 피로감과 별개로, 내부 실행력은 지금 만들어가는 중입니다. 오늘은 Z-P2(내일 전사전략회의) 최종 점검과 Z-P6(파일럿 공지) 두 가지에 집중하세요.\n\n날씨는 쌀쌀하지만 화요일 회의 준비에 집중할 아침입니다. 화이팅!"
    },
    "sections": {
        "kor": {
            "label": "🇰🇷 국내 경제·일간지",
            "papers": [
                {
                    "name": "매일경제",
                    "url": "https://www.mk.co.kr/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "구글 '터보퀀트' 쇼크에 코스피 3%대 급락…5,730.74 마감", "url": "https://www.mk.co.kr/news/stock/", "eng": "Kospi slides over 3% to 5,730.74 on Google 'TurboQuant' shock", "body": "구글의 AI 압축 알고리즘 '터보퀀트' 공개로 메모리 수요 감소 우려가 확산하며 코스피가 5,730.74(-3.48%) 급락 마감했다. 장중 5,599까지 추락해 매도 측 서킷브레이커가 발동됐다."},
                                {"headline": "이재명 대통령, 2일 시정연설…역대 최대 821조 예산 설득", "url": "https://www.mk.co.kr/news/politics/", "eng": "President Lee to deliver budget speech on record 821tn won plan", "body": "이재명 대통령이 2일 국회에서 2027년도 예산안 시정연설을 한다. 총지출 820조9,000억원으로 역대 최대 규모이며, 국민의힘은 포퓰리즘 예산 삭감을 예고하며 강경 대응에 나섰다."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "삼성전자 30조 배당·SK하이닉스 특별배당…주주환원 190~210조", "url": "https://www.mk.co.kr/news/stock/", "eng": "Samsung's 30tn dividend and SK hynix special dividend push returns to 210tn won", "body": "삼성전자가 3분기 30조원 규모 현금배당을 시행하고, SK하이닉스도 특별배당을 단행한다. 올해 합산 영업이익 640조 전망 속 주주환원 규모는 190~210조원에 달할 전망이다. 다만 주가는 '구글 쇼크'로 부진하다."},
                                {"headline": "한국거래소, 저PBR 기업 151곳 첫 공개…이마트·현대제철 등", "url": "https://www.mk.co.kr/news/stock/", "eng": "KRX names 151 low-PBR companies, including E-mart and Hyundai Steel", "body": "한국거래소가 3년간 PBR 하위권에 머문 151개 상장사를 처음 공개했다. 한화생명·현대제철·롯데쇼핑·이마트 등이 포함됐으며, 2일부터 증권사 앱 종목명에 '저PBR' 꼬리표가 붙는다."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "FBI, 바이낸스 63억달러 해킹 '북한 소행' 공식 확인", "url": "https://www.mk.co.kr/news/economy/", "eng": "FBI officially blames North Korea for $6.3bn Binance hack", "body": "FBI가 세계 최대 가상자산거래소 바이낸스의 63억달러(8.4조원) 탈취 사건 배후로 북한 정예 해킹조직 'TraderTraitor'를 공식 지목했다. 탈취 자산은 이더리움으로 전환돼 세탁 중인 것으로 파악됐다."},
                                {"headline": "에르도안 튀르키예 대통령 국빈 방한…3일 정상회담", "url": "https://www.mk.co.kr/news/politics/", "eng": "Turkish President Erdogan begins state visit to Korea", "body": "레제프 타이이프 에르도안 튀르키예 대통령이 2~4일 한국을 국빈 방문한다. 2018년 이후 8년 만의 방한으로, 3일 이재명 대통령과 정상회담을 열고 미래산업 협력을 논의한다."}
                            ],
                        },
                    ],
                },
                {
                    "name": "경향신문",
                    "url": "https://www.khan.co.kr/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "이재명 대통령 2일 시정연설…821조 '사상 최대' 예산 설득", "url": "https://www.khan.co.kr/politics/", "eng": "President Lee seeks support for record 821tn won budget", "body": "이재명 대통령이 2일 국회 본회의에서 2027년도 예산안 시정연설을 한다. 총지출 820조9,000억원, 미래대응기금 162조3,000억원 신설이 골자로, 국민의힘은 포퓰리즘 항목 삭감을 벼르고 있다."},
                                {"headline": "에르도안 튀르키예 대통령 2~4일 국빈 방한", "url": "https://www.khan.co.kr/politics/", "eng": "Erdogan arrives in Seoul for state visit", "body": "레제프 타이이프 에르도안 튀르키예 대통령이 2일부터 4일까지 한국을 국빈 방문한다. 3일 공식 환영식을 시작으로 정상회담, 양해각서 서명식, 국빈 만찬 등이 예정돼 있다."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "한국거래소 저PBR 151곳 공개…이마트·현대제철 '꼬리표'", "url": "https://www.khan.co.kr/economy/", "eng": "KRX tags 151 undervalued stocks including E-mart", "body": "한국거래소가 장기간 저평가된 상장사 151곳을 처음 공개했다. 평균 PBR 0.25배로 시장 평균(약 1.8배)을 크게 밑돌며, 2일부터 증권사 거래 시스템에 '저PBR' 표기가 붙는다."},
                                {"headline": "'구글 쇼크'에 코스피 3% 급락…반도체주 흔들", "url": "https://www.khan.co.kr/economy/", "eng": "Google shock sends Kospi down 3%, chips wobble", "body": "알파벳 급락 여파로 코스피가 5,730.74(-3.48%) 급락했다. 삼성전자 -3.02%, SK하이닉스 -7.08%로 반도체 대형주가 직격탄을 맞았고, 장중 5,599까지 밀리며 매도 측 서킷브레이커가 발동됐다."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "FBI, 바이낸스 해킹 '북한 소행' 공식 확인", "url": "https://www.khan.co.kr/world/", "eng": "FBI confirms North Korea behind Binance hack", "body": "FBI가 바이낸스 해킹(63억달러 탈취)의 배후로 북한 연계 해킹조직 TraderTraitor를 공식 지목했다. 탈취 자산은 20분 만에 빠져나갔고, 탈중앙화금융(DeFi)을 통한 세탁이 예상된다."},
                                {"headline": "美 중간선거 D-1…블루웨이브 가능성에 촉각", "url": "https://www.khan.co.kr/world/", "eng": "US midterms a day away amid blue-wave expectations", "body": "미국 중간선거가 하루 앞으로 다가왔다. 민주당이 여론조사에서 제네릭 투표 8.2%p 리드를 보이며 '블루 웨이브' 가능성이 거론되고, 트럼프 대통령은 민주당 장악 시 거부권 적극 행사를 예고했다."}
                            ],
                        },
                    ],
                },
                {
                    "name": "동아일보",
                    "url": "https://www.donga.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "李대통령, 오늘 시정연설…역대 최대 821조 예산안", "url": "https://www.donga.com/news/Politics/", "eng": "President Lee delivers budget speech on record 821tn won plan", "body": "이재명 대통령이 2일 국회에서 2027년도 예산안 시정연설을 한다. 사상 최대인 820조9,000억원 규모로, 국민의힘과의 예산 정국 대치가 본격화할 전망이다."},
                                {"headline": "에르도안 대통령 국빈 방한…3일 정상회담", "url": "https://www.donga.com/news/Politics/", "eng": "Erdogan arrives for state visit, summit on Nov. 3", "body": "레제프 타이이프 에르도안 튀르키예 대통령이 2~4일 한국을 국빈 방문한다. 3일 이재명 대통령과 정상회담을 열고 미래산업·방산 등 협력을 논의할 예정이다."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "코스피 5,730.74 급락…'구글 쇼크' 반도체 직격", "url": "https://www.donga.com/news/Economy/", "eng": "Kospi slides to 5,730.74 as Google shock hits chips", "body": "코스피가 알파벳 급락 여파로 5,730.74(-3.48%) 마감했다. 구글 AI 압축 알고리즘 공개로 메모리 수요 우려가 커지며 삼성전자·SK하이닉스 등 반도체주가 급락했다."},
                                {"headline": "거래소, 저PBR 기업 151곳 첫 공표…한화생명·이마트 등", "url": "https://www.donga.com/news/Economy/article/all/20261101/134944017/1", "eng": "KRX unveils 151 low-PBR firms including Hanwha Life", "body": "한국거래소가 유가증권·코스닥 상장사 중 저PBR 기업 151곳을 처음 공표했다. 한화생명·현대제철·롯데쇼핑·이마트 등이 이름을 올렸다."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "삼성전자 30조 배당·SK하이닉스 특별배당…주주환원 확대", "url": "https://www.donga.com/news/Economy/", "eng": "Samsung, SK hynix boost shareholder returns", "body": "삼성전자가 3분기 약 30조원 현금배당을 시행하고, SK하이닉스도 특별배당에 나선다. 올해 합산 영업이익 640조 전망 속 주주환원이 190~210조원에 이를 전망이다."},
                                {"headline": "바이낸스 63억달러 해킹…FBI '북한 배후' 지목", "url": "https://www.donga.com/news/Economy/", "eng": "FBI points to North Korea in $6.3bn Binance hack", "body": "FBI가 바이낸스 해킹(63억달러 탈취) 배후로 북한 정예 해킹조직을 공식 지목했다. 사상 최대 규모 가상자산 해킹으로, 탈취 자산 세탁이 진행 중이다."}
                            ],
                        },
                    ],
                },
                {
                    "name": "한국경제",
                    "url": "https://www.hankyung.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "코스피 5,730선 '구글 쇼크'…외국인 1.6조 순매도", "url": "https://www.hankyung.com/finance/", "eng": "Google shock drags Kospi to 5,730 as foreigners sell 1.6tn won", "body": "코스피가 알파벳 급락 여파로 5,730.74(-3.48%) 급락 마감했다. 외국인이 1.6조원 순매도했고, 장중 5,599까지 추락하며 매도 측 서킷브레이커가 발동됐다. 연기금 8,929억원 순매수가 낙폭을 방어했다."},
                                {"headline": "삼성전자 30조 배당·SK하이닉스 특별배당…주주환원 190~210조", "url": "https://www.hankyung.com/finance/", "eng": "Samsung and SK hynix unveil massive shareholder returns", "body": "삼성전자 3분기 30조원 배당과 SK하이닉스 특별배당으로 올해 주주환원이 190~210조원에 달할 전망이다. 합산 영업이익 640조 전망에도 주가는 '구글 쇼크'에 부진하다."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "이재명 대통령 2일 시정연설…821조 예산 정국 본격화", "url": "https://www.hankyung.com/politics/", "eng": "President Lee opens 821tn won budget fight", "body": "이재명 대통령이 2일 2027년도 예산안 시정연설을 한다. 역대 최대 820조9,000억원 규모로, 국민의힘은 포퓰리즘 항목 삭감을 예고하며 강경 대응에 나섰다."},
                                {"headline": "애플·AMD·팔란티어 실적 주간…AI 테마 향방 가른다", "url": "https://www.hankyung.com/finance/", "eng": "Apple, AMD, Palantir earnings to test AI trade", "body": "애플(11/2 장마감 후)·팔란티어(11/2)·AMD(11/3) 실적이 이번 주 발표된다. AI 투자 피로감이 확산된 가운데, 이들 실적이 AI 테마의 내년 방향을 가를 분수령이 될 전망이다."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "저PBR 151곳 꼬리표…이마트·현대제철 포함", "url": "https://www.hankyung.com/article/2026103177206", "eng": "151 low-PBR firms tagged, including E-mart", "body": "한국거래소가 현대제철·롯데케미칼·한화생명·이마트·롯데쇼핑 등 151개 상장사를 저PBR 기업으로 공표했다. 2일부터 증권사 앱에 '저PBR' 표기가 붙는다."},
                                {"headline": "호르무즈 협상 진전…국제유가 하락", "url": "https://www.hankyung.com/finance/", "eng": "Oil falls as Hormuz talks progress", "body": "미국-이란 호르무즈 협상이 도하에서 3일째 이어지며 타결 기대감이 커지고 있다. 협상 진전 소식에 국제유가가 하락세를 보였다."}
                            ],
                        },
                    ],
                },
            ],
        },
        "us": {
            "label": "🇺🇸 미국 경제·일간지",
            "papers": [
                {
                    "name": "The Wall Street Journal",
                    "url": "https://www.wsj.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "AI Investors Race to Get Insurance on the Biggest Market Bet in History", "url": "https://www.wsj.com/finance/stocks/ai-investors-are-racing-to-get-insurance-on-the-biggest-market-bet-in-history-a60e296f", "eng": "", "body": "Investors are rushing to hedge their exposure to AI stocks after Alphabet's record selloff, reflecting growing anxiety that the massive AI infrastructure bet may not pay off."},
                                {"headline": "Binance Resumes Withdrawals After Suffering Biggest-Ever Crypto Hack", "url": "https://www.wsj.com/finance/currencies/binance-resumes-withdrawals-after-suffering-biggest-ever-crypto-hack-11d1900f", "eng": "", "body": "Binance resumed withdrawals after more than $6 billion in virtual assets were stolen in the largest crypto hack in history, which the FBI attributed to the North Korea-linked TraderTraitor group."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "Earnings-Fueled Stock Rally Faces Key Test", "url": "https://www.wsj.com/finance/stocks/global-stocks-markets-dow-news-05-18-2026-f8053b68", "eng": "", "body": "The earnings-driven market rally faces a critical week as Apple, AMD and Palantir report, with investors weighing whether AI spending can sustain the sector's momentum."},
                                {"headline": "Big Tech Is Cutting Back on Buybacks. Nvidia Could Be the Exception.", "url": "https://www.wsj.com/finance/stocks/big-tech-is-cutting-back-on-buybacks-nvidia-could-be-the-exception-8fc6044f", "eng": "", "body": "Major technology companies are trimming share buybacks amid heavy AI capital spending, though Nvidia may be the outlier given its record cash generation."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "Judge Dismisses Trump Suit Against Wall Street Journal Over Epstein Letter", "url": "https://npr.org/2026/11/01/nx-s1-6025342/judge-dismisses-trump-suit-against-wall-street-journal-epstein-letter", "eng": "", "body": "A federal judge threw out Donald Trump's $10 billion lawsuit against the Journal, saying the president was 'grasping at straws' and failed to prove actual malice."},
                                {"headline": "See How Trump's Accounts Were Busy Trading Big Tech Stocks", "url": "https://www.wsj.com/finance/stocks/trump-stock-trades-ce970ce9", "eng": "", "body": "A review of trading activity shows accounts tied to the president were actively buying and selling Big Tech shares during the market's AI-driven swings."}
                            ],
                        },
                    ],
                },
                {
                    "name": "Bloomberg",
                    "url": "https://www.bloomberg.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "Wall Street Tech Rout Deepens as AI Valuation Worries Spread", "url": "https://theage.com.au/business/markets/asx-set-to-slip-wall-street-hit-by-tech-rout-binance-sees-withdrawals-spike-as-it-returns-online-20261102-p61afh.html", "eng": "", "body": "The S&P 500 tumbled 1.8% for its worst day since June, closing out a third straight losing week, as worries mounted that AI technology prices rose too high. Amazon fell 4% after reporting a weaker profit and burning $42.4 billion in cash."},
                                {"headline": "Anthropic Raises More Questions Than It Answers About Risk", "url": "https://www.bloomberg.com/news/articles/2026-10-27/anthropic-ipo-documents-raise-more-questions-about-ai-risk-and-trustees", "eng": "", "body": "Anthropic's IPO documents raise fresh questions about whether its handpicked trustees can balance rapid AI growth with concerns over computer-driven catastrophe."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "Iran to Take Action Against Sinokor Ships in Strait of Hormuz", "url": "https://www.bloomberg.com/news/articles/2026-10-27/iran-says-it-will-take-action-against-sinokor-ships-in-hormuz", "eng": "", "body": "Iran's Strait of Hormuz authority announced it will take legal action against all ships of South Korea's Sinokor, which carried over a third of crude through the strait in September."},
                                {"headline": "US MBA Applications Plunge 27% as International Demand Drops", "url": "https://www.bloomberg.com/news/articles/2026-10-27/us-mba-applications-plunge-as-international-student-demand-drops", "eng": "", "body": "Applications to US business schools fell sharply as international student demand dropped, though the decline was less steep at more selective programs."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "Apple, AMD, Palantir Lead Big Earnings Week", "url": "https://blofin.com/es/academy/education/tradfi/earnings-this-week-nov-2-6-2026", "eng": "", "body": "Apple reports Monday after the close with Palantir expected the same evening, followed by AMD on Tuesday. The results will be a key test of the AI rally after Alphabet's rout."},
                                {"headline": "Oil Falls as US-Iran Hormuz Deal Nears", "url": "https://www.bloomberg.com/markets", "eng": "", "body": "Crude prices fell on optimism that the US and Iran are closing in on a deal to reopen the Strait of Hormuz, easing supply fears that had pushed oil sharply higher."}
                            ],
                        },
                    ],
                },
                {
                    "name": "The New York Times",
                    "url": "https://www.nytimes.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "A Midterm Campaign Dominated by Concerns Over High Prices Nears Its End", "url": "https://nytimes.com/2026/11/01/us/politics/election-mood-affordability.html", "eng": "", "body": "With the war in Iran and tariffs driving up gas prices, inflation and mortgage rates, financial worries are center stage in the final days of the campaign that will decide control of Congress."},
                                {"headline": "The Largest Cyber Heist in History", "url": "https://www.nytimes.com/", "eng": "", "body": "Attackers increasingly use AI and advanced techniques to steal crypto and quickly launder funds, as the Binance hack — the biggest cyber heist ever — showed."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "Trump to Rally in Kansas and Iowa as Midterms Enter Final Stretch", "url": "https://www.nytimes.com/", "eng": "", "body": "President Trump will hold rallies in Kansas and Iowa in the closing days of the midterm campaign, while Democrats press their affordability message."},
                                {"headline": "The S&P 500 Is Set for a Small Loss in October", "url": "https://www.nytimes.com/", "eng": "", "body": "The S&P 500 is on track for a small October loss despite a deeper slide in some of the AI stocks that exert heavy influence on the index."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "Gaffes and Men's Bodies: Analysis of Trump's Speeches at Age 80", "url": "https://nytimes.com/2026/11/01/us/politics/trump-speeches-rallies-age.html", "eng": "", "body": "An AI-assisted review of Trump's speeches found his public communication has grown more vulgar, more uninhibited and less coherent than a decade ago."},
                                {"headline": "Barry Blitt's 'Polling Place'", "url": "https://newyorker.com/culture/cover-story/cover-story-2026-11-02", "eng": "", "body": "The cover of the November 2, 2026, issue sums up Trump's midterm efforts — attempts to purge voter rolls, coerce state officials and frighten voters away from polls."}
                            ],
                        },
                    ],
                },
                {
                    "name": "The Washington Post",
                    "url": "https://www.washingtonpost.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "Trump Holds Call With Netanyahu Over State of Iran War", "url": "https://www.washingtonpost.com/world/", "eng": "", "body": "The two leaders discussed whether to ramp up combat operations against Iran, with Netanyahu pressing for strikes after the midterms and Trump eager to let negotiations play out."},
                                {"headline": "Obama Rips Into Ramaswamy Over Attack Ad: 'There's No Line He Won't Cross'", "url": "https://www.washingtonpost.com/politics/2026/10/24/obama-slams-ramaswamy-over-ad-with-amy-acton-mother-no-line-he-wont-cross/", "eng": "", "body": "Barack Obama sharply criticized Vivek Ramaswamy over a campaign ad featuring a candidate's estranged mother, as Democrats lean on the former president as their closing messenger."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "Voters Angry About High Prices May Get Little Relief From the Next Congress", "url": "https://www.washingtonpost.com/business/2026/10/24/voters-angry-about-high-prices-may-get-little-relief-next-congress/", "eng": "", "body": "Even if Democrats win control of Congress on Nov. 3, lawmakers can do little about prices that are uncomfortably high and will stay that way as inflation slows."},
                                {"headline": "In First Midterm Rallies, Obama Assails Trump Administration", "url": "https://www.washingtonpost.com/politics/2026/10/24/cleveland-rally-obama-blasts-trump-administration/", "eng": "", "body": "Democrats have embraced Barack Obama as their most effective closing messenger in the final weeks of the high-stakes midterm campaign."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "Iran in 'Advanced Stages' of Plots to Kill U.S. Officials Abroad, Memo Warns", "url": "https://www.washingtonpost.com/world/2026/10/24/iran-advanced-stages-plots-kill-us-officials-abroad-memo-warns/", "eng": "", "body": "The top US intelligence official said Iran has 'substantially increased' efforts to target Americans abroad, according to a memo."},
                                {"headline": "Musk Breaks Donor Record as Ultrarich Pour $2.7 Billion Into the Midterms", "url": "https://www.washingtonpost.com/elections/interactive/2026/06/25/these-are-biggest-individual-donors-2026-election-cycle/", "eng": "", "body": "Billionaires and Elon Musk, who recently temporarily achieved trillionaire status, are the top individual donors in the 2026 midterm cycle."}
                            ],
                        },
                    ],
                },
                {
                    "name": "Financial Times",
                    "url": "https://www.ft.com/",
                    "pages": [
                        {
                            "label": "1면",
                            "articles": [
                                {"headline": "AI Selloff Deepens as Investors Question Spending", "url": "https://www.ft.com/markets", "eng": "", "body": "Global tech stocks extended their slide as Alphabet's record 12% drop amplified doubts about whether hundreds of billions in AI investment will yield adequate returns."},
                                {"headline": "Democrats Eye 'Blue Wave' as US Midterms Near", "url": "https://www.ft.com/world", "eng": "", "body": "Democrats hold a solid generic-ballot lead heading into the November 3 midterms, raising the prospect of a blue wave that could hand them control of Congress."}
                            ],
                        },
                        {
                            "label": "2면",
                            "articles": [
                                {"headline": "Apple and Palantir Earnings to Test AI Rally", "url": "https://www.ft.com/markets", "eng": "", "body": "This week's earnings from Apple, AMD and Palantir will be a crucial test for the AI trade after last week's tech rout, with Palantir expected to beat consensus."},
                                {"headline": "Oil Falls as US-Iran Hormuz Talks Progress", "url": "https://www.ft.com/markets", "eng": "", "body": "Crude prices dropped on progress in US-Iran talks over the Strait of Hormuz, easing fears that had threatened global oil flows through the key waterway."}
                            ],
                        },
                        {
                            "label": "3면",
                            "articles": [
                                {"headline": "FBI Blames North Korea's TraderTraitor for Record Binance Hack", "url": "https://www.ft.com/", "eng": "", "body": "The FBI publicly attributed the largest crypto heist in history to the North Korea-linked TraderTraitor group, which drained $6.3 billion from Binance in 20 minutes."},
                                {"headline": "Bank of Japan Holds Rates at 1.25% and Expands ETF Sales", "url": "https://www.ft.com/markets", "eng": "", "body": "The BOJ held its policy rate at 1.25% in an 8-1 vote and signaled it would expand sales of its ETF holdings, weighing on Japanese equities."}
                            ],
                        },
                    ],
                },
            ],
        },
    },
}

with open("/Users/seokjinlee/daily-frontpage/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json written OK")
print("kor papers:", len(data["sections"]["kor"]["papers"]))
print("us papers:", len(data["sections"]["us"]["papers"]))
print("morning.headline present:", bool(data["morning"].get("headline")))
print("headline == topNews:", data["morning"]["headline"] == data["morning"]["topNews"])
for p in data["sections"]["kor"]["papers"] + data["sections"]["us"]["papers"]:
    assert len(p["pages"]) == 3, p["name"]
    for pg in p["pages"]:
        assert pg["label"] in ("1면", "2면", "3면"), p["name"]
        for a in pg["articles"]:
            assert set(a.keys()) == {"headline", "url", "eng", "body"}, a
print("all pages == 3 and article schema: OK")
