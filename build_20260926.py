#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""daily-frontpage build for 2026-09-26 (Sat). Generates data.json."""
import json

D = {
    "date": "2026-09-26",
    "dateLabel": "2026년 9월 26일(토요일)",
    "generatedAt": "2026-09-26T07:20:00+09:00",
    "ticker": [
        {"name": "KOSPI", "value": "7,080.92", "change": "+0.90%", "dir": "up"},
        {"name": "KOSDAQ", "value": "844.48", "change": "+1.21%", "dir": "up"},
        {"name": "S&P 500", "value": "7,704.13", "change": "-0.02%", "dir": "dn"},
        {"name": "NASDAQ", "value": "26,939.37", "change": "+0.01%", "dir": "up"},
        {"name": "Dow", "value": "51,349.98", "change": "-0.31%", "dir": "dn"},
        {"name": "WTI", "value": "$92.26", "change": "▼", "dir": "dn"},
        {"name": "원/달러", "value": "1,372원", "change": "약 (9/23 기준)", "dir": "up"},
    ],
    "keywords": [
        {"label": "① 추석 연휴(9/24~26) 국내 증시 휴장",
         "desc": "코스피 7,080.92(+0.90%)로 연휴 전 마지막 거래일 4거래일 연속 상승 마감. 삼성전자·SK하이닉스 쌍두마차 강세"},
        {"label": "② 美 10년물 금리 5.21% 고점",
         "desc": "주중 2007년 이후 최고치 경신 → 금요일 4.94% 소폭 진정. '고금리 장기화'가 시장 베이스케이스로 굳어지는 분위기"},
        {"label": "③ 추석 후 코스피 상승 확률 73.1%",
         "desc": "과거 26년 데이터, 연휴 직후 5거래일 평균 +1.34%. '전약후강' 패턴 반복 전망"},
        {"label": "④ 마이크론 실적·美 PCE가 관건",
         "desc": "연휴 기간 발표될 물가·반도체 실적이 개장(9/28) 방향성 결정. 호실적 시 7,200선 도전 가능"},
        {"label": "⑤ 트럼프-시진핑 정상회담(9/24)",
         "desc": "한반도·대만·중동·AI 논의. '화려한 의전, 실질 성과는 부족' 평가"},
    ],
    "morning": {
        "date": "2026-09-26",
        "headline": "추석 연휴 국내 증시 휴장 — 코스피 7,080 '4거래일 연속 상승' 마감, 美 10년물 5.21% 고점·추석 후 상승확률 73%가 변수",
        "weather": "🌧️ 흐림 | 18°C (체감 19°C) | 습도 82% | 바람 4km/h",
        "schedule": "🎌 추석 연휴 둘째 날(토요일) | 오늘의 일정: 명상 30분 · 팔굽혀펴기 30개 · 하루일정체크",
        "domestic": {
            "kospi": {"value": "7,080.92", "change": "▲ 63.01", "changeRate": "+0.90%"},
            "kosdaq": {"value": "844.48", "change": "▲ 10.10", "changeRate": "+1.21%"},
            "supply": {"usdkrw": "1,372", "change": "약 1,372원 (9/23 기준)"},
            "comment": "추석 연휴(9/24~26) 전 마지막 거래일인 9/23(화) 코스피는 7,080.92(+0.90%)로 마감하며 4거래일 연속 상승했습니다. 삼성전자·SK하이닉스 반도체 쌍두마차 강세가 지수 상승을 견인했고, 외국인 순매수가 유입 전환되며 연휴를 앞둔 기관 저가매수가 이어졌습니다. 코스닥은 844.48(+1.21%), 원/달러는 약 1,372원(9/23 기준)으로 원화 약세가 이어졌습니다.",
        },
        "overseas": {
            "dow": {"value": "51,349.98", "changeRate": "-0.31%"},
            "sp500": {"value": "7,704.13", "changeRate": "-0.02%"},
            "nasdaq": {"value": "26,939.37", "changeRate": "+0.01%"},
            "oil": {"wti": "$92.26", "brent": "$97.55"},
            "keyStocks": "뉴욕증시는 9/25(금) 혼조 마감했습니다. 다우 -0.31%(51,349.98), S&P500 -0.02%(7,704.13), 나스닥 +0.01%(26,939.37). 美 10년물 국채금리는 주중 5.21%로 2007년 이후 최고치를 찍은 뒤 금요일 4.94%로 소폭 진정됐습니다. WTI $92.26·브렌트 $97.55로 유가가 소폭 하락했고, 원/달러는 약 1,372원(9/23)에 머물렀습니다.",
        },
        "topNews": "추석 연휴 국내 증시 휴장 — 코스피 7,080 '4거래일 연속 상승' 마감, 美 10년물 5.21% 고점·추석 후 상승확률 73%가 변수",
        "otherNews": [
            "트럼프-시진핑 정상회담(9/24) — 한반도·대만·중동·AI 논의, '화려한 의전·실질 성과 부족' 평가",
            "美·이란 호르무즈 협상 진전 — 이란, 7일 내 휴전·해협 재개방 제안...유가 안정 기대",
            "美 10년물 금리 5.21% — 2007년 이후 최고치 경신 후 4.94% 진정, '고금리 장기화' 우려",
            "북한군 포로 2명 한국행 — 젤렌스키 UN 연설서 공개, 청와대 사실상 인정",
            "연방정부 셧다운 리스크 — 예산안 협상 난항, 필수 인력 외 휴직 가능성",
        ],
        "email": {
            "google": "오늘 브리핑에 이메일 수신 내역은 별도로 집계되지 않았습니다.",
            "note": "추석 연휴 기간 글로벌 마켓 모니터링 / 월요일(9/28) 개장 전략 점검",
        },
        "insight": "🌕 추석 — 시장은 쉬어도 글로벌 변수는 쉬지 않는다\n\n연휴 직전 코스피는 7,080으로 4거래일 연속 상승하며 기분 좋게 마감했습니다. 과거 26년 통계상 추석 직후 5거래일 상승 확률은 73.1%(평균 +1.34%)로 '전약후강' 패턴이 기대됩니다.\n\n🔑 연휴 중 체크포인트\n- 美 PCE 물가: 예상 하회 시 7,200선 도전 가능\n- 마이크론 실적: 호실적 시 반도체주 추가 랠리\n- 美 10년물 금리: 5% 안착 시 추가 조정 빌미\n\n오늘은 명상 30분·팔굽혀펴기로 리프레시하고, 개장 전 전략을 정리해두세요.\n\n_☀️ 풍성한 한가위 보내세요, 형!_",
    },
    "sections": {
        "kor": {
            "label": "🇰🇷 국내 경제·일간지",
            "papers": [
                {
                    "name": "매일경제",
                    "url": "https://www.mk.co.kr/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "추석 직후 코스피 '전약후강'…마이크론 실적·美 PCE가 방향 결정", "url": "https://www.mk.co.kr/news/stock/12160900", "eng": "KOSPI set for post-Chuseok rebound; Micron, PCE to decide direction", "body": "추석 연휴 직후 코스피의 방향성은 연휴 기간 발표될 미국 PCE 물가지수와 마이크론 실적이 결정할 전망이다. 과거 26년 데이터상 추석 직후 5거래일 상승 확률은 73.1%다."},
                            {"headline": "美 10년물 금리 5.21% '2007년 이후 최고'…금요일 4.94% 진정", "url": "https://www.mk.co.kr/news/stock/12160910", "eng": "US 10-year yield hits 5.21%, highest since 2007", "body": "미국 10년물 국채금리가 주중 5.21%까지 치솟으며 2007년 이후 최고치를 경신했다가 금요일 4.94%로 소폭 진정됐다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "코스피 7,080 '4거래일 연속 상승'…삼성·하이닉스 자사주 훈풍", "url": "https://stock.mk.co.kr/news/view/1148460", "eng": "KOSPI rises for 4th day on chip buybacks", "body": "삼성전자·SK하이닉스 자사주 매입 훈풍에 코스피가 7,080.92(+0.90%)로 마감하며 4거래일 연속 상승했다."},
                            {"headline": "외국인 순매수 유입 전환, 연휴 앞둔 기관 저가매수", "url": "https://www.mk.co.kr/news/stock/12160920", "eng": "Foreign investors turn net buyers ahead of holiday", "body": "추석 연휴 전 마지막 거래일 외국인이 순매수로 전환했고, 기관도 연휴를 앞두고 저가매수에 나서며 지수 하단을 지지했다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "마이크론, 9/30 실적 발표…삼성·하이닉스 주가 '풍향계'", "url": "https://www.mk.co.kr/news/stock/12160930", "eng": "Micron earnings seen as barometer for Korean chipmakers", "body": "마이크론이 9월 30일 실적을 발표한다. HBM 수요와 AI 투자 가이던스가 삼성전자·SK하이닉스 주가의 풍향계가 될 전망이다."},
                            {"headline": "남아공서 한국인 여행가방에 전갈 150마리 밀반출 적발", "url": "https://www.mk.co.kr/news/society/11428500", "eng": "150 scorpions found in Korean's luggage in South Africa", "body": "남아프리카공화국에서 한국인 여행자의 여행가방에 전갈 150마리를 밀반출하려다 적발됐다고 연합뉴스가 보도했다."},
                        ]},
                    ],
                },
                {
                    "name": "경향신문",
                    "url": "https://www.khan.co.kr/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "청와대 '북한 포로 한국행' 공개에 \"젤렌스키 연설 전 알려 왔다\"", "url": "https://www.khan.co.kr/article/202609251505001", "eng": "Blue House says it was informed of POW transfer before Zelensky's speech", "body": "청와대는 젤렌스키 우크라이나 대통령의 UN 연설에서 북한군 포로 2명의 한국 송환이 공개된 것과 관련해 '조용히 처리해야 신속하고 원만하게 처리될 수 있다'는 입장을 밝혔다."},
                            {"headline": "[김용민의 그림마당] 2026년 09월 26일 — 추석과 고금리", "url": "https://www.khan.co.kr/article/202609262135005", "eng": "Editorial cartoon - Chuseok and high rates", "body": "경향신문 김용민 화백의 시사만평. 추석 연휴와 美 국채금리 5% 시대, 고유가를 다뤘다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "미·이란 호르무즈 협상 급물살…유가 안정 기대", "url": "https://www.khan.co.kr/economy/", "eng": "US-Iran Hormuz talks raise hopes for oil stability", "body": "이란이 미국에 7일 내 휴전과 호르무즈 해협 재개방을 골자로 한 새 평화협상 제안을 전달하며 국제유가 안정 기대가 커지고 있다."},
                            {"headline": "추석 연휴에도 쉬지 않는 서학개미…미 금리·유가 주시", "url": "https://www.khan.co.kr/economy/economy-general/", "eng": "Korean retail investors stay active over Chuseok", "body": "추석 연휴 국내 증시가 휴장하는 동안 미국 증시는 정상 개장한다. 개인투자자들은 미 금리와 유가 흐름을 주시하고 있다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "美 국채금리 5% 시대…'고금리 장기화' 베이스케이스로", "url": "https://www.khan.co.kr/economy/", "eng": "5% Treasury era cements higher-for-longer bets", "body": "미국 10년물 국채금리가 주중 5.21%를 찍으며 2007년 이후 최고를 경신했다. '고금리 장기화'가 시장의 베이스 케이스로 굳어지는 분위기다."},
                            {"headline": "연방정부 셧다운 리스크…예산안 협상 난항", "url": "https://www.khan.co.kr/world/", "eng": "US shutdown risk rises as budget talks stall", "body": "미국 연방정부 예산안 협상이 난항을 겪으며 셧다운 가능성이 커지고 있다. 필수 인력 외 휴직 가능성이 제기된다."},
                        ]},
                    ],
                },
                {
                    "name": "동아일보",
                    "url": "https://www.donga.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "트럼프, 시진핑에 B-2·마린원 과시…'화려한 의전, 실속은 부족'", "url": "https://www.donga.com/news/Inter/article/all/20260924/134731165/2", "eng": "Trump puts on show for Xi; pomp over substance", "body": "트럼프 미국 대통령이 시진핑 중국 국가주석에게 B-2 폭격기와 대통령 전용헬기 마린원을 과시하는 등 화려한 의전을 펼쳤지만, 실질 성과는 부족했다는 평가가 나온다."},
                            {"headline": "미중 정상회담, 한반도·대만·중동 논의…신화통신 보도", "url": "https://www.donga.com/news/Inter/USA", "eng": "US-China summit covers Korean peninsula, Taiwan, Middle East", "body": "트럼프·시진핑 정상회담에서 한반도 문제와 중동 정세, 대만 문제 등이 논의됐다고 중국 관영 신화통신이 전했다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "추석 연휴 국내 증시 9/26까지 휴장…월요일 개장", "url": "https://www.donga.com/news/Economy/", "eng": "Korean markets closed through Sept 26 for Chuseok", "body": "추석 연휴로 코스피·코스닥 시장이 24일부터 26일까지 휴장한다. 다음 거래일은 28일 월요일이다."},
                            {"headline": "코스피 7,080 4거래일 연속 상승…개인 차익실현", "url": "https://www.donga.com/news/Economy/", "eng": "KOSPI rises for 4th session; retail books profits", "body": "추석 연휴 전 마지막 거래일 코스피가 7,080.92(+0.90%)로 4거래일 연속 상승했다. 연휴를 앞둔 개인은 차익실현에 나섰다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "美 10년물 금리 5.21%…원화 약세·성장주 압박", "url": "https://www.donga.com/news/Economy/Money", "eng": "Won weakens as US yields spike to 5.21%", "body": "미국 10년물 국채금리가 5.21%로 치솟으며 원/달러 환율이 1,372원선으로 올랐다. 고금리가 성장주 멀티플을 압박하고 있다."},
                            {"headline": "북한군 포로 2명 한국행…젤렌스키 UN 연설서 공개", "url": "https://www.donga.com/news/Politics/", "eng": "Two North Korean POWs transferred to South Korea", "body": "젤렌스키 우크라이나 대통령이 UN 연설에서 북한군 포로 2명을 한국에 보냈다고 공개했고, 정부도 사실상 인정했다."},
                        ]},
                    ],
                },
                {
                    "name": "한국경제",
                    "url": "https://www.hankyung.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "추석 후 코스피 상승 확률 73%…마이크론·PCE가 관건", "url": "https://www.hankyung.com/article/202609261234i", "eng": "73% odds of post-Chuseok KOSPI gains; Micron, PCE key", "body": "과거 26년 통계상 추석 직후 5거래일 코스피 상승 확률은 73.1%, 평균 상승률 +1.34%다. 연휴 중 마이크론 실적과 미국 PCE가 관건이다."},
                            {"headline": "美 10년물 금리 5.21% 터치…'고금리 장기화' 경계", "url": "https://www.hankyung.com/economy/", "eng": "US 10-year yield touches 5.21%, highest since 2007", "body": "미국 10년물 국채금리가 주중 5.21%로 2007년 이후 최고치를 기록한 뒤 4.94%로 진정됐다. 고금리 장기화에 대한 경계가 커지고 있다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "삼성·하이닉스 자사주 매입 훈풍…코스피 4거래일 연속 상승", "url": "https://www.hankyung.com/article/202609261235i", "eng": "Chip buybacks drive 4-day KOSPI rally", "body": "삼성전자·SK하이닉스 자사주 매입 훈풍에 코스피가 7,080.92(+0.90%)로 마감하며 4거래일 연속 상승했다."},
                            {"headline": "외국인 순매수 전환, 기관 저가매수에 7,080 안착", "url": "https://www.hankyung.com/article/202609261236i", "eng": "Foreigners turn net buyers; KOSPI settles above 7,080", "body": "추석 연휴 전 마지막 거래일 외국인이 순매수로 전환하고 기관이 저가매수에 나서며 코스피가 7,080선에 안착했다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "마이크론 9/30 실적 '반도체 풍향계'…HBM 수요 주목", "url": "https://www.hankyung.com/article/202609261237i", "eng": "Micron earnings to set chip-sector tone", "body": "마이크론의 9월 30일 실적 발표가 삼성전자·SK하이닉스 등 반도체주의 방향성을 좌우할 풍향계로 꼽힌다. HBM 수요와 AI 투자 가이던스가 주목된다."},
                            {"headline": "원/달러 1,372원…추석 연휴에도 서학개미는 미장 주시", "url": "https://www.hankyung.com/economy/", "eng": "Won at 1,372; retail investors watch US markets", "body": "원/달러 환율이 약 1,372원(9/23 기준)에 머물렀다. 국내 증시가 휴장한 추석 연휴에도 서학개미들은 미국 증시를 주시하고 있다."},
                        ]},
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
                        {"label": "1면", "articles": [
                            {"headline": "U.S., Iran Discuss Phased Reopening of Strait of Hormuz", "url": "https://www.wsj.com/world/middle-east/us-iran-phased-reopening-strait-hormuz-2026", "eng": "U.S., Iran Discuss Phased Reopening of Strait of Hormuz", "body": "U.S. and Iranian negotiators in New York are discussing a phased deal to reopen the Strait of Hormuz and lift the economic blockade, fueling hopes for oil price relief."},
                            {"headline": "10-Year Treasury Yield Tops 5.1%, Highest Since 2007", "url": "https://www.wsj.com/finance/investing/10-year-treasury-yield-highest-since-2007-2026", "eng": "10-Year Treasury Yield Tops 5.1%, Highest Since 2007", "body": "The benchmark 10-year Treasury yield climbed above 5.1% to its highest level since 2007 as the bond selloff deepened, before easing to 4.94% on Friday."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Trump-Xi Summit: Pomp Over Substance", "url": "https://www.wsj.com/politics/policy/trump-xi-summit-pomp-substance-2026", "eng": "Trump-Xi Summit: Pomp Over Substance", "body": "President Trump rolled out B-2 flyovers and Marine One for Xi Jinping, but the leaders agreed on little beyond photo opportunities on AI, Taiwan and the Iran war."},
                            {"headline": "Oil Retreats as Iran Offers Seven-Day Cease-Fire Proposal", "url": "https://www.wsj.com/business/energy-oil/oil-retreats-iran-ceasefire-proposal-2026", "eng": "Oil Retreats as Iran Offers Cease-Fire Proposal", "body": "Crude retreated from session highs after Iran said it had given the Trump administration a new proposal to reopen the Strait of Hormuz and restart peace talks within seven days."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Tech Selloff: Google, Oracle, Broadcom Lead Declines", "url": "https://www.wsj.com/finance/stocks/tech-selloff-google-oracle-broadcom-2026", "eng": "Tech Selloff: Google, Oracle, Broadcom Lead Declines", "body": "Big tech slid as rising yields pressured valuations, with Google, Oracle and Broadcom leading the declines."},
                            {"headline": "Micron Earnings to Test AI-Chip Rally", "url": "https://www.wsj.com/finance/stocks/micron-earnings-test-ai-chip-rally-2026", "eng": "Micron Earnings to Test AI-Chip Rally", "body": "Micron's Sept. 30 earnings will test the AI-chip rally, with investors watching HBM demand and forward guidance closely."},
                        ]},
                    ],
                },
                {
                    "name": "Bloomberg",
                    "url": "https://www.bloomberg.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Bond Yields at 5% Mark New Era 'Until Something Breaks'", "url": "https://www.bloomberg.com/news/articles/2026-09-24/us-treasury-yields-hit-5-as-wall-street-faces-new-rate-regime", "eng": "Bond Yields at 5% Mark New Era 'Until Something Breaks'", "body": "The 10-year Treasury yield pierced 5%, the highest since 2007, as investors brace for a higher-for-longer rate regime that could persist 'until something breaks'."},
                            {"headline": "Iran Offers US New Seven-Day Ceasefire Proposal", "url": "https://www.bloomberg.com/news/articles/2026-09-24/us-iran-said-to-be-exploring-phased-deal-to-open-hormuz", "eng": "Iran Offers US New Seven-Day Ceasefire Proposal", "body": "Iran has given the Trump administration a new proposal to reopen the Strait of Hormuz and restart talks to end the broader war within seven days."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Trump-Xi Summit Goes Big on Pomp, Small on Substance", "url": "https://www.bloomberg.com/news/articles/2026-09-25/xi-seizes-trump-detente-to-seek-lasting-gains-on-trade-taiwan", "eng": "Trump-Xi Summit Goes Big on Pomp, Small on Substance", "body": "Xi Jinping seized on the Trump detente to seek lasting gains on trade and Taiwan, while the summit itself delivered more ceremony than concrete results."},
                            {"headline": "Oil Pulls Back as Hormuz Talks Advance", "url": "https://www.bloomberg.com/news/articles/2026-09-24/oil-pulls-back-hormuz-reopening-report", "eng": "Oil Pulls Back as Hormuz Talks Advance", "body": "Crude pulled back from session highs after reports that U.S. and Iranian negotiators are discussing a phased reopening of the Strait of Hormuz."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Microsoft Abandons Personal AI Chatbot Race With Copilot Reboot", "url": "https://www.bloomberg.com/news/articles/2026-09-25/microsoft-abandons-personal-ai-chatbot-race-with-copilot-reboot", "eng": "Microsoft Abandons Personal AI Chatbot Race", "body": "Microsoft is abandoning the personal AI chatbot race, rebooting Copilot as high-yield pressure hits growth valuations across big tech."},
                            {"headline": "Blackstone's Private Equity Chief Joe Baratta Leaving Firm", "url": "https://www.bloomberg.com/news/articles/2026-09-25/blackstone-s-private-equity-chief-joe-baratta-in-talks-to-exit", "eng": "Blackstone's Private Equity Chief Joe Baratta Leaving", "body": "Blackstone's private equity chief Joe Baratta is in talks to exit, capping a year of high-profile departures at the firm."},
                        ]},
                    ],
                },
                {
                    "name": "The New York Times",
                    "url": "https://www.nytimes.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Trump Meets Xi, Seeking to Contain Iran War and Trade Frictions", "url": "https://www.nytimes.com/2026/09/24/world/asia/trump-xi-summit-iran-trade.html", "eng": "Trump Meets Xi, Seeking to Contain Iran War and Trade Frictions", "body": "President Trump met Xi Jinping in a summit aimed at containing the Iran war and easing trade frictions, though the talks yielded little concrete progress."},
                            {"headline": "Oil Prices Ease as U.S. and Iran Edge Toward Talks", "url": "https://www.nytimes.com/2026/09/24/business/oil-prices-iran-talks.html", "eng": "Oil Prices Ease as U.S. and Iran Edge Toward Talks", "body": "Oil prices eased as the U.S. and Iran edged toward talks on reopening the Strait of Hormuz, a key chokepoint for global crude."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Bond Market Braces for a 5% World", "url": "https://www.nytimes.com/2026/09/24/business/treasury-yields-5-percent.html", "eng": "Bond Market Braces for a 5% World", "body": "The 10-year Treasury yield crossed 5% to its highest since 2007, forcing investors to recalibrate for a world of higher borrowing costs."},
                            {"headline": "Federal Shutdown Looms as Spending Talks Stall", "url": "https://www.nytimes.com/2026/09/25/us/politics/federal-shutdown-spending-talks.html", "eng": "Federal Shutdown Looms as Spending Talks Stall", "body": "A federal government shutdown looms as spending talks stall, with the possibility that nonessential workers could be furloughed."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Netanyahu, Isolated at the U.N., Lashes Out", "url": "https://www.nytimes.com/2026/09/24/world/middleeast/netanyahu-un-address-isolation.html", "eng": "Netanyahu, Isolated at the U.N., Lashes Out", "body": "Israeli Prime Minister Benjamin Netanyahu arrived at the U.N. facing new depths of isolation, lashing out at critics in his address."},
                            {"headline": "Susan Sarandon Among Those Arrested at Netanyahu Protest", "url": "https://www.nytimes.com/2026/09/25/nyregion/susan-sarandon-netanyahu-protest-arrest.html", "eng": "Susan Sarandon Among Those Arrested at Netanyahu Protest", "body": "Actor Susan Sarandon was among those arrested at a protest condemning Netanyahu's U.N. visit, police said."},
                        ]},
                    ],
                },
                {
                    "name": "The Washington Post",
                    "url": "https://www.washingtonpost.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Trump, Xi seek detente but agree on little beyond photo ops", "url": "https://www.washingtonpost.com/world/2026/09/24/donald-trump-meets-xi-jinping-rare-earths-give-china-powerful-hand/", "eng": "Trump, Xi seek detente but agree on little beyond photo ops", "body": "As Trump met Xi Jinping, rare earth minerals gave Beijing a powerful bargaining hand, and the two leaders agreed on little beyond ceremonial photo opportunities."},
                            {"headline": "Iran offers new proposal for peace talks, reopening Strait of Hormuz", "url": "https://www.washingtonpost.com/world/2026/09/24/iran-says-it-has-given-trump-administration-new-proposal-peace-talks/", "eng": "Iran offers new proposal for peace talks", "body": "Iran said it has given the Trump administration a new proposal to reopen the Strait of Hormuz and restart talks over an end to the broader war within seven days."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Soaring bond yields rattle markets as 10-year hits 5%", "url": "https://www.washingtonpost.com/business/2026/09/25/bond-yields-5-percent-markets/", "eng": "Soaring bond yields rattle markets", "body": "The 10-year Treasury yield hit 5%, the highest since 2007, rattling markets and pressuring growth stocks."},
                            {"headline": "Bipartisan senators urge Trump to disinvite Putin from G-20", "url": "https://www.washingtonpost.com/politics/2026/09/25/bipartisan-group-senators-urge-trump-disinvite-putin-g-20/", "eng": "Senators urge Trump to disinvite Putin from G-20", "body": "A bipartisan group of senators urged President Trump to disinvite Vladimir Putin from the G-20 summit planned for December in Miami."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Rare September nor'easter cancels Maryland music festival opening", "url": "https://www.washingtonpost.com/dc-md-va/2026/09/24/rare-september-noreaster-cancels-oceans-calling-festivals-opening-day/", "eng": "Rare September nor'easter cancels festival opening", "body": "An unusually early nor'easter brought heavy rain and canceled the opening day of a Maryland music festival."},
                            {"headline": "Americans' views of China warm ahead of Trump-Xi summit, Pew finds", "url": "https://www.washingtonpost.com/world/2026/09/24/americans-views-china-have-warmed-survey-finds-ahead-trump-xi-summit/", "eng": "Americans' views of China warm, Pew finds", "body": "The share of U.S. adults with a positive view of China rose to 19 percent this year, a Pew survey found ahead of the Trump-Xi summit."},
                        ]},
                    ],
                },
                {
                    "name": "Financial Times",
                    "url": "https://www.ft.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Iran offers US new seven-day ceasefire proposal", "url": "https://www.ft.com/content/917a9cba-6afd-4ba3-8742-2b7601ecc2ba", "eng": "Iran offers US new seven-day ceasefire proposal", "body": "Iran has offered the US a new seven-day ceasefire proposal that would reopen the Strait of Hormuz and restart talks to end the broader war."},
                            {"headline": "Pomp prevails over substance as Trump hosts Xi", "url": "https://www.ft.com/content/cdff194b-8106-4f71-b5b8-d0dbaf2c4d79", "eng": "Pomp prevails over substance as Trump hosts Xi", "body": "Ceremony dominated the Trump-Xi summit, with the two leaders holding wide-ranging talks on AI, Taiwan and the Iran war but reaching little concrete agreement."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Soaring bond yields 'not even close' to cooling red-hot US economy", "url": "https://www.ft.com/content/bcf0715b-4292-428e-80ec-e6702d430aa4", "eng": "Soaring bond yields 'not even close' to cooling US economy", "body": "Investors say surging Treasury yields are 'not even close' to cooling the red-hot US economy, as the 10-year yield hovered near 5%."},
                            {"headline": "US oil industry pushes back against proposed diesel export ban", "url": "https://www.ft.com/content/c902e192-8bbb-4f32-813c-ee255d3aebd0", "eng": "US oil industry pushes back on diesel export ban", "body": "The US oil industry is pushing back against a proposed diesel export ban, warning it would raise prices abroad and hurt refiners."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Micron earnings set to test AI chip rally", "url": "https://www.ft.com/content/24c13fd3-5de5-4916-8300-ec3073027ff6", "eng": "Micron earnings set to test AI chip rally", "body": "Micron's upcoming earnings will test the AI chip rally, with HBM demand and guidance in focus for Korean memory makers Samsung and SK Hynix."},
                            {"headline": "Manchester City found guilty of breaching Premier League rules", "url": "https://www.ft.com/content/2f820ff9-28c2-4e53-9948-6be009a8a23c", "eng": "Manchester City found guilty of breaching rules", "body": "An independent panel found Manchester City guilty on 114 of 115 charges after a lengthy investigation into financial rule breaches."},
                        ]},
                    ],
                },
            ],
        },
    },
}

with open("/Users/seokjinlee/daily-frontpage/data.json", "w", encoding="utf-8") as f:
    json.dump(D, f, ensure_ascii=False, indent=2)

print("written")
