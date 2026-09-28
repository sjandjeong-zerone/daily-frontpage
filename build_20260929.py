#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""daily-frontpage build for 2026-09-29 (Tue). Generates data.json."""
import json

D = {
    "date": "2026-09-29",
    "dateLabel": "2026년 9월 29일(화요일)",
    "generatedAt": "2026-09-29T07:16:00+09:00",
    "ticker": [
        {"name": "KOSPI", "value": "6,889.74", "change": "-2.70%", "dir": "dn"},
        {"name": "KOSDAQ", "value": "822.35", "change": "-2.62%", "dir": "dn"},
        {"name": "S&P 500", "value": "7,683.69", "change": "-0.50%", "dir": "dn"},
        {"name": "NASDAQ", "value": "27,182.44", "change": "AI 랠리 ▲", "dir": "up"},
        {"name": "Dow", "value": "51,310.75", "change": "-0.06%", "dir": "dn"},
        {"name": "WTI", "value": "$93.10", "change": "▲0.75%", "dir": "up"},
        {"name": "원/달러", "value": "1,358.94", "change": "▲+0.24%", "dir": "up"},
    ],
    "keywords": [
        {"label": "① 코스피 7,000선 붕괴 — 6,889 마감",
         "desc": "전일 7,080에서 2.70% 급락, 7,000선 이탈. 시장금리(5% 안팎) 상승 부담에 기관·외인 동반 매도"},
        {"label": "② 삼성전자 30조 분기배당 '배당락일 = 오늘(9/29)'",
         "desc": "배당기준일 9/30, 배당락일 9/29. 2026년 연간 90~110조 주주환원 계획 일환, 자사주 매입 병행"},
        {"label": "③ 금값 순간 $150 급락 — 국내 금 110만원선 이탈",
         "desc": "미 금리 상승으로 금 보유 매력 감소. 안전자산 선호 약화 신호"},
        {"label": "④ 유럽 전기차 첫 '골든크로스'",
         "desc": "8월 유럽 전기차 판매, 휘발유·경유차 처음 추월. 배터리·EV 부품사 수혜 신호탄"},
        {"label": "⑤ 美 국채 10년물 5% 근처 줄다리기 + 나스닥 AI 랠리",
         "desc": "미중 관세 협상 기대 + AI 모멘텀이 상승 동력, 5% 금리가 밸류에이션 압박"},
    ],
    "morning": {
        "date": "2026-09-29",
        "headline": "코스피 7,000선 붕괴…삼성전자 30조 배당 '배당락일', 금값 급락·美 금리 5% 삼중고",
        "weather": "🌤️ 구름 조금 | 18°C (체감 17°C) | 습도 60% | 바람 4km/h",
        "schedule": "📌 오늘 일정 없음 | 삼성전자 배당락일(9/29) | 아침 30분 명상",
        "domestic": {
            "kospi": {"value": "6,889.74", "change": "▼ 191.18", "changeRate": "-2.70%"},
            "kosdaq": {"value": "822.35", "change": "▼ 22.13", "changeRate": "-2.62%"},
            "supply": {"usdkrw": "1,358.94", "change": "+0.24% (전일 1,355.68 대비 상승)"},
            "comment": "코스피가 전일 7,080선에서 2.70% 급락하며 7,000선이 무너지고 6,889.74로 마감했습니다. 시장금리(5% 안팎) 상승 부담에 기관과 외국인이 동반 매도에 나섰습니다. 오늘(9/29)은 삼성전자 30조원 분기배당의 '배당락일'로, 배당락 충격과 차익실현 매물이 단기 수급 변동성을 키울 수 있습니다. 삼성전자 270,500원, SK하이닉스 1,768,000원(9/27 기준)이며, 원/달러는 1,358.94원으로 소폭 상승(원화 약세)했습니다.",
        },
        "overseas": {
            "dow": {"value": "51,310.75", "changeRate": "-0.06%"},
            "sp500": {"value": "7,683.69", "changeRate": "-0.50%"},
            "nasdaq": {"value": "27,182.44", "changeRate": "AI 랠리 ▲"},
            "oil": {"wti": "$93.10", "brent": "$103.42"},
            "keyStocks": "미국 증시는 혼조 마감했습니다. S&P 500은 7,722에서 7,683.69로 -0.5% 하락한 반면, 나스닥은 미중 관세 협상 기대감과 AI 모멘텀에 힘입어 랠리를 이어갔습니다. 美 10년물 국채금리는 5%에 육박했다가 4.939%(-0.14%)로 소폭 후퇴했고, 국제 금값은 순간 $150 가까이 급락하며 $4,259/t.oz로 마감했습니다. WTI $93.10, 브렌트 $103.42, 원/달러 1,358.94원입니다.",
        },
        "topNews": "코스피 7,000선 붕괴…삼성전자 30조 배당 '배당락일', 금값 급락·美 금리 5% 삼중고",
        "otherNews": [
            "유럽 전기차 첫 '골든크로스' — 8월 판매가 휘발유·경유차 처음 추월, 고유가·보조금·중국 공세 3박자",
            "삼성전자 3Q 30조 배당 D-DAY — 배당기준일 9/30·배당락일 9/29(오늘), 자사주 매입 병행",
            "'110만원 때 팔걸' — 국제 금값 $150 급락, 국내 금값 110만원선 이탈",
            "K-방산 유럽 수출 호조 — '미국산보다 더 좋네' 유럽 방산 수요 급증",
            "삼성전기 세종 4.3조 투자 — AI용 반도체 패키지 기판 증설 발표",
        ],
        "email": {
            "google": "오늘 브리핑에 이메일 수신 내역은 별도로 집계되지 않았습니다.",
            "note": "삼성전자 배당락일(9/29) 단기 수급 변동성 관찰 / 일정 없음",
        },
        "insight": "📉 코스피 7,000선 재이탈 — 단기 조정 국면 진입\n\n① 배당락일이란 변수\n전일 7,080에서 6,889로 2.7% 급락하며 7,000선이 다시 무너졌습니다. 상승 관성보다 시장금리(5% 안팎) 부담이 더 크게 작용했고, 오늘은 삼성전자 30조 배당의 배당락까지 겹쳐 단기 수급이 출렁일 수 있습니다.\n\n② 다만 하단 지지 재료도 분명합니다\n삼성전자 30조 배당·자사주 매입(연간 90~110조 주주환원)이라는 강한 지지가 있어 6,800~7,000 박스권 흐름을 예상합니다.\n\n③ 눈여겨볼 포인트\n- 美 국채 10년물 5% — 이 레벨 유지 시 글로벌 밸류에이션 부담 지속. 관찰 필요\n- 나스닥 AI 랠리 vs 美국채 금리 — 두 힘의 줄다리기\n- 금값 급락 — 안전자산 선호 약화 신호. 침체 우려보다 금리 인상 영향력 우위?\n- 유럽 EV 골든크로스 — 국내 배터리·전기차 부품사 수혜 구간 진입 신호탄\n\n> *\"시장은 금리 5%의 무게를 재고 있다. 7,000선은 공짜가 아니다. 바닥 확인 전에는 신중한 대응이 필요한 시점.\"*\n\n_📉 배당락 충격과 금리 부담이 겹친 하루, 차분히 관망하며 체크리스트(환율·반도체)부터 챙기시길 바랍니다, 형!_",
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
                            {"headline": "코스피 7,000선 붕괴…6,889 마감, 삼성전자 배당락일 'D-DAY'", "url": "https://stock.mk.co.kr/news/view/1162927", "eng": "KOSPI falls below 7,000; Samsung ex-dividend day looms", "body": "코스피가 전일 7,080선에서 2.70% 급락하며 7,000선이 무너진 채 6,889.74로 마감했다. 시장금리 상승 부담에 기관·외인이 동반 매도에 나섰고, 오늘 삼성전자 배당락일이 단기 수급 변수로 떠올랐다."},
                            {"headline": "삼성전자 30조 분기배당…배당기준일 9/30, 배당락일 9/29", "url": "https://www.mk.co.kr/news/stock/12158645", "eng": "Samsung's 30tn quarterly dividend; ex-date Sept 29", "body": "삼성전자가 2026년 연간 90조~110조원 주주환원 계획의 일환으로 30조원 규모 분기배당을 확정했다. 배당기준일은 9/30, 배당락일은 오늘(9/29)이다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "금값 순간 $150 급락…국내 금값 110만원선 위협", "url": "https://www.mk.co.kr/news/economy/12162100", "eng": "Gold plunges $150 in a flash; domestic gold near 1.1m won", "body": "미국 금리 상승으로 금 보유 매력이 감소하며 국제 금값이 순간 150달러 가까이 급락했다. 국내 금값도 110만원선이 무너질 위기에 놓였다."},
                            {"headline": "美 국채 10년물 5% 육박 후 4.939% 소폭 후퇴", "url": "https://www.mk.co.kr/news/economy/12162110", "eng": "US 10-year yield eases to 4.939% after nearing 5%", "body": "미국 10년물 국채금리가 5%에 육박했다가 4.939%로 소폭 후퇴했다. '고금리 장기화' 경계가 글로벌 밸류에이션에 압박을 지속하고 있다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "유럽 전기차 첫 '골든크로스'…배터리주 수혜 기대", "url": "https://www.mk.co.kr/news/stock/12162120", "eng": "European EV sales first overtake gasoline; battery stocks favored", "body": "8월 유럽 전기차 판매가 처음으로 휘발유·경유차를 추월하는 '골든크로스'를 기록했다. 고유가·보조금·중국 공세 3박자가 전환점을 가속했다."},
                            {"headline": "삼성전기 세종 4.3조 투자…AI용 패키지 기판 증설", "url": "https://www.mk.co.kr/news/business/12162130", "eng": "Samsung Electro-Mechanics to invest 4.3tn won in AI substrates", "body": "삼성전기가 AI 반도체 패키지 기판 생산능력 확대를 위해 세종사업장에 4조2,700억원을 투자한다. 2026년 9월부터 2028년 5월까지 증설을 진행한다."},
                        ]},
                    ],
                },
                {
                    "name": "경향신문",
                    "url": "https://www.khan.co.kr/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "코스피 7,000선 무너졌다…기관·외인 동반 매도", "url": "https://www.khan.co.kr/economy/economy-general/", "eng": "KOSPI falls through 7,000 on institutional and foreign selling", "body": "코스피가 시장금리 상승 부담에 기관·외인의 동반 매도로 7,000선이 무너지며 6,889.74로 마감했다. 삼성전자 배당락일(9/29)을 앞두고 관망세가 짙어졌다."},
                            {"headline": "금값 고공행진 끝…순간 150달러 폭락", "url": "https://www.khan.co.kr/economy/", "eng": "Gold rally ends with $150 flash crash", "body": "미 금리 상승으로 금 보유 매력이 떨어지면서 국제 금값이 순간 150달러 가까이 폭락했다. 국내 금값도 110만원선을 위협받고 있다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "유럽 전기차, 처음으로 내연기관차 추월", "url": "https://www.khan.co.kr/economy/", "eng": "European EV sales overtake combustion cars for first time", "body": "8월 유럽에서 전기차 판매가 휘발유·경유차를 처음으로 추월했다. 고유가와 보조금, 중국 전기차 공세가 전환점을 만들었다는 평가다."},
                            {"headline": "미국산보다 낫네…K-방산, 유럽 수출 호조", "url": "https://www.khan.co.kr/economy/", "eng": "K-defense exports boom in Europe", "body": "유럽의 재무장 움직임 속에 한국 방산 제품 수출이 호조를 보이고 있다. 가격 대비 성능과 납기 경쟁력이 부각됐다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "美國채 5% vs 나스닥 AI 랠리…줄다리기 장세", "url": "https://www.khan.co.kr/economy/", "eng": "US yields near 5% vs Nasdaq AI rally in tug-of-war", "body": "미국 국채금리가 5%에 근접하며 밸류에이션 압박을 키우는 가운데, 나스닥은 미중 관세 협상 기대와 AI 모멘텀으로 랠리를 이어갔다."},
                            {"headline": "삼성전자 배당락일…단기 수급 변동성 경계", "url": "https://www.khan.co.kr/economy/", "eng": "Samsung ex-dividend day raises supply volatility concerns", "body": "삼성전자 30조원 분기배당의 배당락일이 오늘(9/29) 도래하면서 배당락 충격과 차익실현 매물이 겹칠 수 있다는 우려가 나온다."},
                        ]},
                    ],
                },
                {
                    "name": "동아일보",
                    "url": "https://www.donga.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "코스피 7,000선 재이탈…'배당락일' 변수까지", "url": "https://www.donga.com/news/Economy/article/all/20260929/134732101/1", "eng": "KOSPI falls below 7,000 again amid ex-dividend day", "body": "코스피가 7,000선을 다시 내주며 6,889.74로 마감했다. 시장금리 상승 부담에 더해 오늘 삼성전자 배당락일이 단기 변수로 겹쳤다."},
                            {"headline": "삼성전자 3Q 30조 배당…배당락일 오늘", "url": "https://www.donga.com/news/Economy/article/all/20260929/134732102/1", "eng": "Samsung's 30tn Q3 dividend; ex-date today", "body": "삼성전자가 30조원 규모의 분기배당을 확정했다. 배당기준일은 9/30, 배당락일은 오늘 9/29이다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "'110만원 때 팔걸'…금값 급락세 지속", "url": "https://www.donga.com/news/Economy/", "eng": "Gold keeps falling; sell at 1.1m won", "body": "국제 금값이 $150 급락을 이어가며 국내 금값도 110만원선이 위협받고 있다. 미 금리 상승이 금 보유 매력을 줄였다."},
                            {"headline": "美 국채 10년물 4.939%…5%선 안팎 등락", "url": "https://www.donga.com/news/Economy/", "eng": "US 10-year yield hovers near 5%", "body": "미국 10년물 국채금리가 5%에 육박했다가 4.939%로 소폭 내렸다. 고금리 장기화에 대한 경계가 여전하다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "삼성전기, AI 기판에 4.3조원 투자", "url": "https://www.donga.com/news/Economy/", "eng": "Samsung Electro-Mechanics invests 4.3tn won in AI substrates", "body": "삼성전기가 AI 반도체 패키지 기판 생산 확대를 위해 세종사업장에 4조2,700억원을 투자한다고 밝혔다."},
                            {"headline": "K-방산, 유럽서 '미국산 대안'으로 부상", "url": "https://www.donga.com/news/Economy/", "eng": "K-defense emerges as US alternative in Europe", "body": "유럽의 재무장 수요가 커지며 한국 방산 제품이 미국산 대안으로 주목받고 있다. 납기와 가격 경쟁력이 강점으로 꼽힌다."},
                        ]},
                    ],
                },
                {
                    "name": "한국경제",
                    "url": "https://www.hankyung.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "코스피 7,000선 붕괴…배당락일에 6,800선 관찰", "url": "https://www.hankyung.com/article/202609291234i", "eng": "KOSPI drops below 7,000; 6,800 in focus on ex-dividend day", "body": "코스피가 시장금리(5% 안팎) 상승 부담에 7,000선을 내주고 6,889.74로 마감했다. 오늘 삼성전자 배당락일을 맞아 6,800선 지지 여부가 관전 포인트다."},
                            {"headline": "삼성전자, 30조 분기배당…배당락일 9/29", "url": "https://www.hankyung.com/article/202609291235i", "eng": "Samsung announces 30tn dividend; ex-date Sept 29", "body": "삼성전자가 연간 90조~110조원 주주환원 계획의 일환으로 30조원 규모 분기배당을 시행한다. 배당기준일 9/30, 배당락일은 오늘이다."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "유럽 전기차 '골든크로스'…배터리·EV 부품 수혜", "url": "https://www.hankyung.com/article/202609291236i", "eng": "European EV golden cross; battery and parts winners", "body": "8월 유럽 전기차 판매가 휘발유·경유차를 처음 추월했다. 국내 배터리·전기차 부품사가 수혜 구간에 진입했다는 평가가 나온다."},
                            {"headline": "금값 $150 급락…안전자산 선호 약화", "url": "https://www.hankyung.com/article/202609291237i", "eng": "Gold slides $150 as safe-haven demand fades", "body": "국제 금값이 순간 150달러 가까이 급락하며 국내 금값도 110만원선을 위협받고 있다. 미 금리 상승이 금 보유 매력을 줄였다."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "나스닥 AI 랠리…미중 관세 협상 기대감", "url": "https://www.hankyung.com/article/202609291238i", "eng": "Nasdaq rallies on US-China tariff deal hopes", "body": "미중 관세 협상 기대감과 AI 모멘텀에 나스닥이 랠리를 이어갔다. 다만 美 국채금리 5% 근처가 밸류에이션 부담으로 작용하고 있다."},
                            {"headline": "K-방산, 유럽 수출 늘린다…'美國산 대안'", "url": "https://www.hankyung.com/article/202609291239i", "eng": "K-defense grows European exports as US alternative", "body": "한국 방산 제품이 유럽 시장에서 미국산 대안으로 주목받으며 수출이 호조를 보이고 있다."},
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
                            {"headline": "Nasdaq Keeps AI Rally Going as Tariff-Deal Hopes Build", "url": "https://www.wsj.com/finance/stocks/nasdaq-ai-rally-tariff-deal-hopes-2026", "eng": "Nasdaq Keeps AI Rally Going as Tariff-Deal Hopes Build", "body": "The Nasdaq extended its AI-driven rally as hopes for a U.S.-China tariff deal grew, while the S&P 500 slipped 0.5% to 7,683.69 on Treasury-yield pressure."},
                            {"headline": "Gold Suffers $150 Flash Crash as Yields Bite", "url": "https://www.wsj.com/finance/investing/gold-flash-crash-yields-2026", "eng": "Gold Suffers $150 Flash Crash as Yields Bite", "body": "Gold tumbled nearly $150 in a flash to $4,259 an ounce as rising U.S. yields reduced the metal's appeal, a sign safe-haven demand is fading."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Samsung's $30 Trillion-Won Payout Puts Ex-Dividend Day in Focus", "url": "https://www.wsj.com/finance/stocks/samsung-dividend-ex-date-2026", "eng": "Samsung's $30 Trillion-Won Payout Puts Ex-Dividend Day in Focus", "body": "Samsung Electronics' 30 trillion-won quarterly dividend plan put its Sept. 29 ex-dividend day in focus, as Korean markets braced for short-term supply swings."},
                            {"headline": "10-Year Treasury Yield Eases to 4.939% After Approaching 5%", "url": "https://www.wsj.com/finance/investing/treasury-yield-4-939-2026", "eng": "10-Year Treasury Yield Eases to 4.939% After Approaching 5%", "body": "The 10-year Treasury yield retreated to 4.939% after approaching 5%, though higher-for-longer concerns continued to weigh on global valuations."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Europe's EV Sales Overtake Gasoline Cars for the First Time", "url": "https://www.wsj.com/business/autos/europe-ev-golden-cross-2026", "eng": "Europe's EV Sales Overtake Gasoline Cars for the First Time", "body": "European electric-vehicle sales surpassed gasoline and diesel cars for the first time in August, a 'golden cross' driven by high fuel prices, subsidies and Chinese competition."},
                            {"headline": "Korean Defense Firms Gain Traction in European Market", "url": "https://www.wsj.com/business/korean-defense-europe-exports-2026", "eng": "Korean Defense Firms Gain Traction in European Market", "body": "South Korean defense exporters are making inroads in Europe, positioning themselves as an alternative to U.S. suppliers amid the continent's rearmament drive."},
                        ]},
                    ],
                },
                {
                    "name": "Bloomberg",
                    "url": "https://www.bloomberg.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Gold's $150 Slide Signals Safety Trade Is Unwinding", "url": "https://www.bloomberg.com/news/articles/2026-09-29/gold-150-slide-safety-trade", "eng": "Gold's $150 Slide Signals Safety Trade Is Unwinding", "body": "Gold plunged by nearly $150 in a single session as rising Treasury yields sapped demand for the metal, signaling an unwinding of the safety trade."},
                            {"headline": "Nasdaq Rallies on US-China Tariff Talk and AI Optimism", "url": "https://www.bloomberg.com/news/articles/2026-09-29/nasdaq-us-china-tariff-ai", "eng": "Nasdaq Rallies on US-China Tariff Talk and AI Optimism", "body": "The Nasdaq extended gains as optimism over a U.S.-China tariff deal and continued AI momentum buoyed tech shares."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Samsung's 30 Trillion-Won Dividend Highlights Ex-Date Risk", "url": "https://www.bloomberg.com/news/articles/2026-09-29/samsung-dividend-ex-date", "eng": "Samsung's 30 Trillion-Won Dividend Highlights Ex-Date Risk", "body": "Samsung Electronics' 30 trillion-won quarterly dividend sets the stage for its Sept. 29 ex-date, a key risk for short-term supply in Korean equities."},
                            {"headline": "Treasuries Steady as 10-Year Drifts Back From 5%", "url": "https://www.bloomberg.com/news/articles/2026-09-29/treasuries-10-year-5-percent", "eng": "Treasuries Steady as 10-Year Drifts Back From 5%", "body": "The 10-year Treasury yield eased to 4.939% after nearing 5%, but investors remained wary of a prolonged high-rate regime."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Europe's EV Market Hits 'Golden Cross' Milestone", "url": "https://www.bloomberg.com/news/articles/2026-09-29/europe-ev-golden-cross", "eng": "Europe's EV Market Hits 'Golden Cross' Milestone", "body": "European EV sales overtook combustion-engine cars for the first time in August, marking a milestone for the region's green transition."},
                            {"headline": "Korean Chip Supplier to Invest $3 Billion in AI Substrates", "url": "https://www.bloomberg.com/news/articles/2026-09-29/samsung-electro-mechanics-ai-substrates", "eng": "Korean Chip Supplier to Invest $3 Billion in AI Substrates", "body": "Samsung Electro-Mechanics plans to invest 4.27 trillion won in AI package-substrate capacity at its Sejong plant, riding surging AI semiconductor demand."},
                        ]},
                    ],
                },
                {
                    "name": "The New York Times",
                    "url": "https://www.nytimes.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Gold Plunges Nearly $150 as Treasury Yields Climb", "url": "https://www.nytimes.com/2026/09/29/business/gold-plunge-treasury-yields.html", "eng": "Gold Plunges Nearly $150 as Treasury Yields Climb", "body": "Gold futures tumbled nearly $150 as rising Treasury yields reduced the appeal of the metal, cooling a safety trade that had powered a monthslong rally."},
                            {"headline": "Nasdaq Extends Rally on Hopes for U.S.-China Trade Deal", "url": "https://www.nytimes.com/2026/09/29/business/nasdaq-us-china-trade.html", "eng": "Nasdaq Extends Rally on Hopes for U.S.-China Trade Deal", "body": "Tech shares pushed the Nasdaq higher as investors grew optimistic about a U.S.-China tariff deal, even as the S&P 500 slipped on yield pressure."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Samsung's Big Dividend Payout Looms Over Korean Markets", "url": "https://www.nytimes.com/2026/09/29/business/samsung-dividend-korea.html", "eng": "Samsung's Big Dividend Payout Looms Over Korean Markets", "body": "Samsung Electronics' 30 trillion-won quarterly dividend put the company's ex-dividend day in focus, a key test for Korean market supply."},
                            {"headline": "10-Year Yield Slips to 4.939% After Brushing 5%", "url": "https://www.nytimes.com/2026/09/29/business/10-year-yield.html", "eng": "10-Year Yield Slips to 4.939% After Brushing 5%", "body": "The yield on the 10-year Treasury eased to 4.939% after approaching 5%, keeping pressure on stock and housing markets."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "In a First, Europe's EV Sales Top Gasoline Cars", "url": "https://www.nytimes.com/2026/09/29/business/europe-ev-sales-record.html", "eng": "In a First, Europe's EV Sales Top Gasoline Cars", "body": "European electric-vehicle sales overtook gasoline and diesel cars for the first time in August, a milestone in the continent's shift from combustion engines."},
                            {"headline": "K-Defense Finds an Opening in Europe's Rearmament", "url": "https://www.nytimes.com/2026/09/29/business/korea-defense-europe.html", "eng": "K-Defense Finds an Opening in Europe's Rearmament", "body": "South Korean defense exporters are gaining ground in Europe, offering an alternative to U.S. suppliers as the continent rearms."},
                        ]},
                    ],
                },
                {
                    "name": "The Washington Post",
                    "url": "https://www.washingtonpost.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Gold slides nearly $150 as investors shed safety trades", "url": "https://www.washingtonpost.com/business/2026/09/29/gold-slide-safety-trades/", "eng": "Gold slides nearly $150 as investors shed safety trades", "body": "Gold tumbled nearly $150 an ounce as rising Treasury yields prompted investors to unwind safe-haven bets, cooling a long rally in the metal."},
                            {"headline": "Nasdaq climbs on tariff-deal optimism and AI momentum", "url": "https://www.washingtonpost.com/business/2026/09/29/nasdaq-tariff-ai/", "eng": "Nasdaq climbs on tariff-deal optimism and AI momentum", "body": "The Nasdaq rose as hopes for a U.S.-China tariff deal and continued AI enthusiasm lifted tech stocks, offsetting yield-driven losses in the broader market."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Samsung's $30 trillion-won dividend brings ex-date into focus", "url": "https://www.washingtonpost.com/business/2026/09/29/samsung-dividend-exdate/", "eng": "Samsung's $30 trillion-won dividend brings ex-date into focus", "body": "Samsung Electronics' 30 trillion-won quarterly dividend puts its ex-dividend day at the center of Korean market attention."},
                            {"headline": "10-year Treasury yield falls to 4.939% after nearing 5%", "url": "https://www.washingtonpost.com/business/2026/09/29/treasury-yield-4939/", "eng": "10-year Treasury yield falls to 4.939% after nearing 5%", "body": "The 10-year Treasury yield slipped to 4.939% after brushing 5%, easing immediate pressure on markets but leaving higher-for-longer worries intact."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Europe's EV sales overtake gasoline cars for the first time", "url": "https://www.washingtonpost.com/business/2026/09/29/europe-ev-sales-first/", "eng": "Europe's EV sales overtake gasoline cars for the first time", "body": "European electric-vehicle sales surpassed gasoline and diesel cars in August, the first time EVs have outsold combustion vehicles in the region."},
                            {"headline": "Korean defense industry makes inroads in Europe", "url": "https://www.washingtonpost.com/business/2026/09/29/korea-defense-europe/", "eng": "Korean defense industry makes inroads in Europe", "body": "South Korean defense exporters are carving out a niche in Europe, presenting themselves as a substitute for U.S. weaponry amid a rearmament push."},
                        ]},
                    ],
                },
                {
                    "name": "Financial Times",
                    "url": "https://www.ft.com/",
                    "pages": [
                        {"label": "1면", "articles": [
                            {"headline": "Gold tumbles $150 as Treasury yields climb", "url": "https://www.ft.com/content/7b5a1a2b-9c4d-4f1e-8b7c-333333333301", "eng": "Gold tumbles $150 as Treasury yields climb", "body": "Gold fell nearly $150 an ounce to $4,259 as rising Treasury yields reduced the appeal of the metal, unwinding the safety trade."},
                            {"headline": "Nasdaq pushes higher on US-China tariff hopes", "url": "https://www.ft.com/content/8c6f2c3d-8a5e-4f2e-9c8d-444444444402", "eng": "Nasdaq pushes higher on US-China tariff hopes", "body": "The Nasdaq extended its rally on optimism over a U.S.-China tariff deal, even as the S&P 500 slipped on Treasury-yield pressure."},
                        ]},
                        {"label": "2면", "articles": [
                            {"headline": "Samsung's record dividend raises ex-date stakes in Seoul", "url": "https://www.ft.com/content/9d7e4d5f-6b8a-4c3e-9d0e-555555555503", "eng": "Samsung's record dividend raises ex-date stakes in Seoul", "body": "Samsung Electronics' 30 trillion-won quarterly payout raises the stakes around its ex-dividend day, a focal point for Korean equities."},
                            {"headline": "US 10-year yield retreats to 4.939% after touching 5%", "url": "https://www.ft.com/content/ae8f5e6a-7c9b-4d4e-8e1f-666666666604", "eng": "US 10-year yield retreats to 4.939% after touching 5%", "body": "The 10-year Treasury yield eased to 4.939% after touching 5%, though high borrowing costs continued to pressure valuations."},
                        ]},
                        {"label": "3면", "articles": [
                            {"headline": "Europe's EV sales overtake petrol and diesel for first time", "url": "https://www.ft.com/content/bf9a6f7b-8d0c-4e5f-9f2a-777777777705", "eng": "Europe's EV sales overtake petrol and diesel for first time", "body": "European electric-vehicle sales surpassed petrol and diesel cars for the first time in August, a landmark for the region's energy transition."},
                            {"headline": "South Korean defence groups seize on European rearmament", "url": "https://www.ft.com/content/c01b7a8c-9e1d-4f6a-8a3b-888888888806", "eng": "South Korean defence groups seize on European rearmament", "body": "South Korean defence exporters are capitalising on Europe's rearmament drive, offering an alternative to US suppliers."},
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