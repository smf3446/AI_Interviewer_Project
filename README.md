# 면접 경험이 부족한 취준생을 위한 AI 면접 시뮬레이터 (Qwen2.5-7B QLoRA 파인튜닝)

ICT 직무 면접 시뮬레이터의 LLM 학습 및 평가 파이프라인입니다.
사용자의 이력서와 직무에 맞춰 **'압박형'과 '친화형'**이라는 상반된 페르소나를 가진 AI 면접관과 실전 모의 면접을 진행하고 피드백을 제공하는 서비스입니다.
파인튜닝을 통해 베이스 모델의 중국어 혼입 문제를 0%대로 해결하고, 프롬프트 엔지니어링과의 시너지를 통해 응답 속도를 최대 7초에서 1~2초대로 단축했습니다.

프로젝트 내에서의 역할
- 데이터 수집 및 파인튜닝
- prompt engineering 및 judge 모델 구현
- 데이터 전처리 및 평가 지표 설계

> 팀 협업 및 개발 환경 설정은 [CONTRIBUTING.md](./CONTRIBUTING.md)를 참고하세요.

---

## 프로젝트 기간

| 구분 | 기간 | 활동 |
| :--- | :--- | :--- |
| 사전 기획 | 5/20(수) ~ 22(금) | 프로젝트 주제 확인 및 목표 설정, 기능 정의 |
| 파이프라인 구축 | 5/25(월) ~ 27(수) | 파이프라인 구축 |
| 데이터 수집 및 전처리 | 5/25(월) ~ 29(금) | 데이터 수집 및 학습 & 개선 |
| 파인튜닝 테스트 | 5/28(목) ~ 29(금) | LLM + LoRA 연결 & 테스트 |
| 백엔드 구축 | 6/1(월) ~ 5(금) | FastAPI & DB 연결 |
| 프론트엔드 구축 | 6/8(월) ~ 9(화) | 웹페이지 생성 & API 연결 |
| QA 및 통제실험 | 6/1(월) ~ 9(화) | 모델 성능 보완, 발표자료 준비 |
| 테스트 | 6/10(수) | 동작 테스트 및 점검 |
| 발표준비 | 6/11(목) ~ 12(금) | 발표자료 준비 |


---

## 제안 배경

- 많은 취준생들이 기술적 역량을 갖추었음에도 불구하고, 실전 면접의 압박감과 돌발 질문 대응에 어려움을 겪는다.
  면접은 항상 존재하는 과제이지만 스터디를 통하지 않으면 경험하고 대비하기 어렵다.

- AI를 이용하여 면접에 대비하고자 하나, 기존 LLM은 면접관 특유의 꼬리질문 생성이나, 특정 직무에 특화된 페르소나를
  유지하는 데 한계가 존재하며, 면접 환경을 제공하는 것 보다 피드백 위주에 초점을 맞춘다.

- 본 시뮬레이터는 사용자의 이력서와 직무에 맞춰 '압박형', '친화형' 페르소나를 구현하여
  실제 면접장과 유사한 긴장감과 피드백을 제공하고자 한다.
  
---

주요 기능

- 페르소나 선택 : 논리 검증 위주의 압박 면접형 또는 긴장 완화 위주의 공감 유도형 면접관 선택 가능
- 이력서 기반 맞춤 질문 : 사용자가 업로드한 이력서와 채용 공고를 분석하여 개인화된 첫 질문 및 꼬리질문 생성
- LoRA 학습 : 파인튜닝을 통해 모델이 별도의 긴 지시문 없이도 면접관의 발화 패턴과 ICT 도메인 지식을 활용하도록 설계
- 실시간 스타일 전환 : 면접 진행 도중 사용자 니즈에 따라 면접관의 성향을 즉시 변경할 수 있는 유연한 로직 구현
- 최종 피드백 리포트 : 면접 종료 후 전체 대화 내용을 분석하여 강점, 개선점 및 STAR 기법 기반의 제안 포함


---

파이프라인 구조
[면접 준비 단계]
사용자 정보 입력 (직무/이력서)
    └─▶ Backend API (FastAPI) 세션 생성
            └─▶ MongoDB 세션 및 대화 기록 저장 공간 확보

[실전 면접 단계]
사용자 답변 입력
    └─▶ Prompt Engineering (이전 대화 Context 구성)
            └─▶ LoRA Routing (Friendly / Pressure 어댑터 선택)
                    └─▶ Qwen2.5-7B + LoRA (맞춤형 꼬리질문 추론)
                            └─▶ Frontend 인터페이스 출력

[결과 분석 단계]
면접 종료 요청
    └─▶ 전체 대화 데이터 분석 (LLM Judge)
            └─▶ 피드백 리포트 생성 및 화면 표시

---

## LoRA 어댑터

허깅페이스에서 다운로드할 수 있습니다.

레포지토리 주소 : **[teems79/interview-lora](https://huggingface.co/teems79/interview-lora)**

| 어댑터 | 설명 |
|--------|------|
| `qwen2.5/pressure` | Qwen2.5-7B-Instruct 압박 면접관 LoRA |
| `qwen2.5/friendly` | Qwen2.5-7B-Instruct 친화 면접관 LoRA |
| `qwen3.5/pressure` | Qwen3.5-9B 압박 면접관 LoRA |
| `qwen3.5/friendly` | Qwen3.5-9B 친화 면접관 LoRA |

---

## 실행 환경

| 구분 | 환경 | 용도 |
|------|------|------|
| 학습 / 추론 | A100 40GB (SSH, MIG 3g.40gb) | LoRA 학습, 하이퍼파라미터 탐색, 추론 |
| 평가 / 분석 | Google Colab (L4 GPU) | A/B 테스트, 프롬프트 엔지니어링, LLM-as-a-Judge, 시각화 |

> SSH 환경은 GPU 공유로 인한 OOM 발생 가능성이 있어, 평가 및 분석 작업은 Colab에서 진행하였습니다.

---

## 프로젝트 구조

```
daon_ai_train/
│
├── src/                             # 핵심 학습 및 평가 코드
│   ├── train_lora.py                # LoRA 파인튜닝 (Pressure / Friendly 순차 학습)
│   ├── hyperparameter_search.py     # Optuna TPE 하이퍼파라미터 탐색
│   ├── inference.py                 # Qwen2.5-7B 추론 (Multi-LoRA 스와핑)
│   ├── inference_9B.py              # Qwen3.5-9B 추론
│   ├── inference_cpu.py             # CPU 환경 추론
│   ├── convert_to_gguf.py           # GGUF 변환
│   ├── prompt_engineering.ipynb     # 프롬프트 엔지니어링 v1~v12 [Colab]
│   ├── AB_Test.ipynb                # A/B 강약 프롬프트 테스트 [Colab]
│   ├── AB_Test_evaluation.ipynb     # Rule Pass Rate / Style Score 평가 [Colab]
│   ├── llm_as_a_judge.ipynb         # LLM-as-a-Judge Pairwise Win Rate 분석 [Colab]
│   └── four_quadrants.ipynb         # 4사분면 모델 성능 시각화 [Colab]
│
├── scripts/                         # 데이터 전처리 및 증강
│   ├── augment_persona.py           # GPT 기반 페르소나 데이터 증강
│   ├── extract_neutral_followups.py # 중립 꼬리질문 추출
│   └── run_style_qa.py              # 스타일 QA 자동 평가 파이프라인
│
├── evaluators/
│   └── style_rules.py               # Pressure / Friendly 룰 기반 평가 기준 정의
│
├── experiments/                     # 하이퍼파라미터 탐색 및 프롬프트 실험 결과
│   ├── hyperparam_results.csv       # Optuna 탐색 결과
│   ├── prompt_scores.csv            # 프롬프트 버전별 평가 점수
│   ├── prompt_evolution_summary.txt # 프롬프트 개선 이력 요약
│   ├── qwen2.5_hyperparameter.txt   # Qwen2.5 최적 하이퍼파라미터
│   └── qwen3.5_hyperparameter.txt   # Qwen3.5 최적 하이퍼파라미터
│
├── prompts/                         # 프롬프트 버전 관리
│   ├── final_pressure.txt           # 최종 압박 페르소나 프롬프트
│   ├── final_friendly.txt           # 최종 친화 페르소나 프롬프트
│   ├── prompt_versions_pressure.txt # 압박 페르소나 프롬프트 변경 이력
│   ├── prompt_versions_friendly.txt # 친화 페르소나 프롬프트 변경 이력
│   ├── prompt_baseline_summary.txt  # 프롬프트 엔지니어링 baseline 총정리
│   └── prompt_changelog.txt         # 프롬프트 엔지니어링 변경점 총정리
│
├── data/
│   ├── processed/                   # 전처리 및 증강 완료 데이터
│   ├── raw/                         # 원본 데이터
│   ├── samples/                     # 샘플 데이터
│   └── splits/                      # train / val / test split
│
├── training/                        # 학습 설정 및 Unsloth 관련
│   ├── configs/
│   └── unsloth/
│
├── embedding.py                     # OpenAI 임베딩 + 클러스터링 기반 데이터 분할
├── requirements.txt
├── CONTRIBUTING.md                  # 개발 환경 및 협업 규칙
└── README.md
```

---


## 파이프라인

### 1. 데이터 증강

```bash
python scripts/augment_persona.py
```

GPT-4o-mini를 활용하여 ICT 직무 면접 질문에 대한 지원자 답변 및 페르소나별 꼬리질문을 ThreadPoolExecutor 기반 병렬 처리로 생성합니다.
Pressure / Friendly 페르소나 각각에 대해 vague, logical, experience_based 등 6가지 답변 유형을 생성합니다.

### 2. 데이터 분할

```bash
python embedding.py
```

OpenAI 임베딩 + AgglomerativeClustering + GroupShuffleSplit을 사용하여
의미적으로 유사한 데이터가 동일 split에 집중되지 않도록 분할합니다.

### 3. LoRA 학습

```bash
python src/train_lora.py
```

Unsloth QLoRA를 사용하여 Pressure / Friendly 페르소나 어댑터를 순차 학습합니다.

| 모델 | LoRA Rank | Learning Rate | Trainable Params |
|------|-----------|---------------|-----------------|
| Qwen2.5-7B-Instruct | 32 | 1e-4 | 80.7M (1.05%) |
| Qwen3.5-9B | 8 | 2e-4 | 14.5M (0.15%) |

- Optimizer: AdamW (cosine scheduler)
- Effective Batch Size: 16 (batch 4 × gradient accumulation 4)
- Early Stopping: patience=3 (eval_loss 기준)

### 4. 하이퍼파라미터 탐색

```bash
python src/hyperparameter_search.py
```

Optuna TPE 탐색으로 LoRA rank, learning rate, batch size 최적값을 탐색합니다.
탐색 결과는 `experiments/` 디렉토리에 저장됩니다.

### 5. 추론

```bash
# Qwen2.5-7B (Multi-LoRA 스와핑)
python src/inference.py

# Qwen3.5-9B
python src/inference_9B.py
```

### 6. 스타일 QA 평가

```bash
python scripts/run_style_qa.py
```

룰 기반 검증기(Style Rules)를 통해 모델 출력의 규칙 준수율을 자동 평가합니다.

---

## 평가 지표

| 지표 | 설명 |
|------|------|
| Style Score | Pressure / Friendly 룰 준수 종합 점수 |
| Rule Pass Rate | sentence / question / forbidden / end / korean 규칙별 통과율 |
| Win Rate | LLM-as-a-Judge Pairwise 양방향 평가 승률 (position bias 보정) |
| Hard Fail Rate | 중국어 혼입 / 프롬프트 유출 / 한국어 비율 미달 발생률 |
| Reference Similarity | 모델 출력과 reference output 간 코사인 유사도 |

---

## 주요 결과

### LLM-as-a-Judge Pairwise (표현 품질)
GPT-5 양방향 평가 (position bias 보정)

| 순위 | 모델 | Win Rate |
|------|------|----------|
| 1 | Qwen3.5-9B-LoRA | 81.09% |
| 2 | Qwen2.5-7B-Base | 48.40% |
| 3 | Qwen2.5-7B-LoRA | 37.50% |
| 4 | Qwen3.5-9B-Base | 33.01% |

### Rule Pass Rate (형식 준수율)
시스템이 요구하는 출력 규칙 준수 여부 측정

| 모델 | Style Score | sentence | question | end | korean |
|------|------------|----------|----------|-----|--------|
| Qwen3.5-9B-LoRA | 83.77% | 100% | 84.21% | 52.64% | 53.38% |
| Qwen2.5-7B-LoRA | 66.82% | 98.87% | 73.31% | 18.42% | 78.38% |
| Qwen2.5-7B-Base | 61.68% | 96.99% | 71.43% | 20.11% | 94.74% |
| Qwen3.5-9B-Base | 54.92% | 92.30% | 63.72% | 22.56% | 44.74% |

> Win Rate는 출력의 자연스러움과 표현 품질을, Rule Pass Rate는 시스템이 요구하는 출력 형식 준수 여부를 측정하며 두 지표는 상호 보완적으로 해석해야 합니다.
> 
---

## 의존성 설치

```bash
pip install -r requirements.txt
```

---

### 회고


## 프로젝트 회고

### 어려웠던 점
1. Qwen 2.5-7B 모델의 중국어 혼입, 9B 모델의 STAR구조 폭주가 자주 발생하였음.
2. test set 기반 모델 출력 평가 과정에서, qwen 2.5-7b-base 모델의 한국어 비율이 94.74%로 높게 측정되었으나, 동일 모델에서
   중국어 혼입(3~7%)이 별도로 발견되어 지표 간 불일치 발생
3. Pairwise 평가에서 GPT-5가 순서쌍에 따라 편향된 판단(랜덤으로 골랐는데 B 위치 선택 비율 61.8%)을 내렸음.
4. 일부 LoRA 모델 조합에서 추론 결과가 빈 문자열로 반환되어 NaN으로 처리되는 현상이 발견되었음.


### 해결 방법
1. 프롬프트 v1 ~ v12에 걸친 반복 개선과 LoRA fine-tuning을 통해 부분적으로 해소하였다.
   다만, 프롬프트 엔지니어링 과정이 7B와 9B 모델에 동일하게 적용되어 모델별 최적화에는 한계가 있었다.
2. korean_ratio 계산 시 중국어가 분모에서 제외되는 구현 방식을 발견하였고, 일본어/중국어/영어 모두 분모에 포함시도록 함수 수정
3. 모든 모델 쌍에 대해 A/B 순서를 교차한 양방향 평가(12쌍, 624회)를 수행하고 결과를 합산하여 보정하였다.
4. tokenizer 입/출력 길이 비교를 통해 불일치나 입력 패턴 문제의 확률이 낮음을 확인했다.
   해당 현상이 base 모델이 아닌 lora 모델에만 발생하는 것으로 보아, 특정 입력 패턴에 대해 출력이 조기종료(early EOS collapse)되어
   의미 있는 토큰 생성에 실패한 것으로 추측된다.
   
   다만, 추론 당시 generated_ids 로그가 없어 정확한 원인은 확정하지 못했으며, 
   NaN 제외 기준의 Effective Pass Rate를 별도 산출하였다.


### 개선 방향

1. 모델 크기 별 독립적인 프롬프트 최적화 및 LoRA 하이퍼 파라미터 탐색(Optuna 진행했으나, 샘플 수가 적음)
2. NaN 발생 원인을 명확히 규명하기 위해 generated_ids 로깅을 진행해야 하며, 안정화를 위해 min_new_tokens 설정 적용
3. LLM-as-a-Judge의 경우 candidate_answer 컬럼을 적용하지 않은 것으로 보여, 이를 포함하여 맥락 기반 신뢰도 상승을 꾀할 수 있음
