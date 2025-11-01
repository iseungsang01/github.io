    
[TOC]  

## 세 줄 요약
1. SOTA LLM Benchmark로는 MMLU, GPQA, HumanEval, LiveCodeBench (코딩), AIME(수학) 등이 있으며,  <a href="https://artificialanalysis.ai/?intelligence-tab=intelligence"> https://artificialanalysis.ai/?intelligence-tab=intelligence</a>에서 확인 할 수 있다.
2. 한국 LLM Benchmark는 [https://aihub.or.kr/leaderboard/view.do](https://aihub.or.kr/leaderboard/view.do) 에서 볼 수 있다.
3. 이러한 지표가 높게 나오기 위해서만 학습하는 경우 기준에만 over-fitting 되거나, LLM 수준이 높아져 지표가 사실상 무의미해지는 경우가 존재하여, 지표 또한 LLM처럼 업데이트 되기도 한다. (MMLU -> MMLU Pro) 
 
## SOTA LLM Benchmark
요즘 LLM에 대한 이야기를 나눌 때면 GPT가 좋다, Gemini가 더 좋다, 코딩은 Claude가 제일 잘한다 등 각각의 경험에 비롯하여 어떤 LLM이 더 좋은지에 관한 이야기 자주 하게 된다.
 그렇다면 학계에서는 어떤 방식으로 LLM을 평가할까?
 현재 가장 주요한 모델들을 평가하는 지표를 이번 목차에서 파악하도록 하겠다.
<div align="left">
   <img src="https://wikidocs.net/images/page/290522/image_202507191432.png" width="500px"><br>
   <small>(출처: Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., Chen, H., Yi, X., Wang, C., Wang, Y., Ye, W., Zhang, Y., Chang, Y., Yu, P. S., Yang, Q., & Xie, X. (2023). <i>A Survey on Evaluation of Large Language Models</i>. <a href="https://doi.org/10.48550/arXiv.2307.03109">https://doi.org/10.48550/arXiv.2307.03109</a>)</small>
</div>
한 논문을 보면 학계에서도 정말 다양한 지표를 사용하고 있는 것을 알 수 있다. 
필자는 현재 가장 앞선 모델들에 대한 OpenAI, Google, xAI, Claude, Deepseek가 제시하는 지표를 통해서 현재 LLM 평가를 위한 대표적인 Benchmark에 대해서 살펴보고자 한다.
<div align="left">
   <img src="https://wikidocs.net/images/page/290522/image_202507191647.png" width="500px"><br>
   <small>(출처 : <a href="https://artificialanalysis.ai/?intelligence-tab=intelligence"> https://artificialanalysis.ai/?intelligence-tab=intelligence</a>)
   </small>
</div>
 <div align="left">
   <img src="https://wikidocs.net/images/page/290522/image_202507191653.png" width="500px"><br>
  <small>(출처 : OpenAI. (2024). GPT-4 Technical Report. </i>. <a href=" https://arxiv.org/abs/2303.08774"> https://arxiv.org/abs/2303.08774</a>)
  </small>
 </div>

1. MMLU (Massive Multitask Language Understanding)  
 MMLU는 대규모 언어 모델의 범용 지식과 문제해결 능력을 평가하는 대표 멀티태스크 벤치마크로. 인문학, STEM, 사회과학 등 57개 다양한 과목에 걸친 15,908 문항(객관식)으로 구성된다.
 평가 특징으로는 1. 영역별 전문성(고교~전문가 수준)까지 테스트, 2. 제로샷/퓨샷 학습 세팅으로 모델의 일반화 성능 평가 (제로샷이란 사전 학습 과정에서 특정 문제 형식을 전혀 본 적이 없는 상태에서 바로 문제를 푸는 상황을 의미하며,  퓨샷은 문제를 풀기 전 몇 가지 예시를 주고 추론하게 만드는 방식을 의미), 3. 단일 태스크 벤치마크보다 모델의 범용 사고력·추론력·지식망 파악에 더 효과적이다.
 현재 LLM 모델들의 수준이 높아져, 최근엔 난이도를 높인 MMLU-Pro 등 후속 벤치마크도 등장하였다. 이 모델에서는 객관식의 선택지 수를 4개에서 10개로 늘렸으며, 같은 내용의 입력에 대한 프롬프트 차이의 오류를 줄인 데이터셋을 이용하여 LLM을 평가한다. 
(<a href="https://arxiv.org/abs/2406.01574"> https://arxiv.org/abs/2406.01574</a>)
 
2. GPQA (Graduate-level Google-Proof Q&A Benchmark)  
 GPQA는 구글 등 검색엔진으로 간단히 정답을 찾을 수 없게 설계된 대학원 수준의 과학(물리, 화학, 생물) Q&A 벤치마크이다. 약 448문항으로 구성되어 전문가(박사급)도 평균 65% 내외 정답률에 그칠 정도로 난이도가 매우 높다(GQPA 데이터셋 : <a href="https://paperswithcode.com/dataset/gpqa"> https://paperswithcode.com/dataset/gpqa</a>)
 평가 특징은 1. 문제별로 복잡한 다단계 논리 추론과 심층적 컨셉 이해 요구,  2. 고급 과학 이론·최신 연구 흐름 반영하여  단순 지식 암기나 패턴 학습을 넘어, LLM의 “심층 reasoning” 수준 한계를 평가하는 데 활용된다.
 
 
3. HumanEval (코드 생성 벤치마크)  
 HumanEval은 함수형 프로그래밍 문제(164개 내외)로 구성된 벤치마크로, LLM이 자연어로 기술된 함수 설명을 입력받아 작동하는 코드를 생성할 수 있는지 평가하는 데 주로 사용된다.
 평가 특징은 1. 각 문제는 함수 시그니처, docstring, 본문, 다수의 유닛 테스트를 포함, 2. 모델이 생성한 코드가 모든 테스트 케이스를 통과하면 성공(pass@k 기준), 3. 알고리즘, 문법, 수식 적용 등 소프트웨어 인터뷰 수준의 코딩 문제 출제한다. 
 
 
4. LiveCodeBench (코딩 벤치마크)  
 LiveCodeBench는 최신 LLM들의 실전적인 프로그래밍 문제 해결 능력을 평가하기 위해, 실제 코딩 대회(LeetCode, AtCoder, Codeforces 등)에서 수집한 1,000여개 이상 문제로 구성된 동적 벤치마크이다.
 평가 특징은 1. 문제 난이도(쉬움~어려움) 및 분야 다양화, 2. 자연어 문제 지문 및 입출력 예시, 비공개 테스트케이스 제공, 3. 코드 생성뿐 아니라 self-repair, 코드 실행, 출력 예측 등 실제 개발스러운 평가 지향, 4. 문제 데이터가 지속적으로 업데이트되어 데이터 누수/과적합 문제 방지하고 있다.
 HumanEval 등의 기존 벤치마크가 사실상 포화(상위 LLM이 만점 근접)된 상황에서, LiveCodeBench는 실제 난이도·적시성 면에서 더욱 현실적으로 모델 ‘경쟁력’을 가늠할 수 있다.
 

5. AIME (American Invitational Mathematics Examination)  
 AIME는 미국 고교 수학 올림피아드 진출자를 선발하기 위한 15문항, 3시간짜리 난이도 높은 시험이다. 문제는 모든 답이 정수로 나오는 비서술형(숫자기입형)이고, 연산·도형·조합론·정수론 등 고난도 사고력 수학 문제로 구성된다.
평가 특징은 1. 단순 연산이 아닌, 창의적 수리적 추론과 논리력을 종합적으로 평가, 2. LLM의 연쇄 사유(chain-of-thought) 성능 깊이 분석에 적합하다.

## 한국 LLM Benchmark
한국 LLM 모델은 다음과 같은 방식으로 평가한다고 한다. 보는 바와같이 성능 지표 이외에도 사회적으로 유해할 수 있는 부분에 대해 무해성을 평가하거나, 사회적 가치관에 대해서 평가하는 등 bias를 방지하는 LLM 지표들도 설정되어 평가하고 있는 것으로 보인다. 
(출처 : <a href="https://aihub.or.kr/leaderboard/view.do"> https://aihub.or.kr/leaderboard/view.do</a>)

각각의 성능지표와 Benchmark에 대해서 정리하면 다음과 같다. 

1. 추론 능력 (Winogrande)  
문장 내 대명사(예: “그는/그녀는”)가 어떤 대상을 가리키는지 추론하는 능력을 평가하는 지표이다. 이 벤치마크는 Winograd Schema Challenge(WSC)를 확장한 약 44,000개의 문제로 구성되며, 단순 연관 추출을 넘어 문맥과 상식 기반의 이해를 요구한다. 규모가 크고 난이도가 높아 모델의 실제 추론 능력을 정밀하게 감지하는 데 활용된다.

2. 산술추론 능력 (GSM8K)  
초등학교 수준의 수학 문제 8,000개를 통해 다단계 계산 및 추론 능력을 판단하는 지표이다. 평균 2~8단계의 문제 해결 과정을 요구하며, 정답 일치 방식을 기준으로 평가된다. 단순 계산 능력뿐 아니라 논리적 사고 과정을 포함한 추론력을 검증하는 데 중점을 둔다.

3. 정보추출 능력 (Ko‑GPQA)  
대학원 수준의 Google 검증 Q&A 벤치마크로, 생물학, 물리학, 화학 등 박사급 전문가들이 제작한 고난도 데이터셋을 기반으로 한다. 다지선다형 형식으로 심층 전문 지식과 도메인 간 연결 이해 능력을 평가하며, 고급 지식 기반 및 복합 질문에 대한 대응 능력을 측정한다.


4. 지시 이행 능력 (Ko‑IFEval)  
주어진 명시적 지시(예: “키워드 포함” 또는 “△형식 사용”)를 얼마나 정확하게 따르는지를 평가하는 지표이다. 0-shot 환경에서 프롬프트에 포함된 지시 사항을 얼마나 충실히 준수하는지 평가하며, 사용자의 의도를 얼마나 잘 이행하는지를 판단한다.


5. 감성 평가 (Ko‑EQ‑Bench)  
대화 맥락에서 등장인물의 감정 강도와 사회적 상호작용을 예측하고 분석하는 능력을 측정한다. EQ‑Bench 점수 시스템을 활용하며, 단순 정보 처리 수준을 넘어 감정의 맥락을 이해하고 적절히 대응할 수 있는 모델의 능력을 평가한다.


6. 정보정확성 (KorNAT‑Knowledge)  
한국 국민이 공유하는 공통 지식, 주로 초·중등 교육 수준의 내용을 얼마나 잘 알고 있는지를 평가하는 지표이다. 다지선다형 문제와 정규화된 정확도(acc_norm)를 기준으로 채점되며, 지역적·문화적 배경 지식을 반영한 정확성과 사실 기반 이해 여부를 검증한다.


7. 소셜 얼라인먼트 (KorNAT‑Social‑Value)  
최근 정치, 경제, 사회 이슈에 대해 사회 구성원의 가치관과 얼마나 일치하는지를 평가하는 지표이다. A‑SVA 지표를 활용하여 평가하며, 사회·윤리적 맥락에서 사람들의 일반적인 의견과 모델의 응답 일치도를 측정한다.


8. 무해성 (Ko‑Harmlessness)  
편향, 혐오, 민감 주제, 불법성 등 위험한 영역에서 모델이 부정적이고 위험한 응답을 얼마나 잘 회피하는지 평가하는 지표이다. 다양한 위험 범주에 대한 다지선다형 문제로 구성되며, 의도치 않은 유해 정보를 생성하지 않는 모델의 안전성을 검증하는 데 사용된다.


9. 도움 적정성 (Ko‑Helpfulness)  
사용자의 의도를 파악하고 주어진 질문의 목적에 맞게 얼마나 유용하고 적절한 정보를 제공하는지를 평가하는 지표이다. 다지선다형 문제를 활용하며, 실제 사용자 상호작용에서 실용적이고 목적에 부합하는 답변을 생성하는 능력을 측정한다.

이외에도, 한국어 자체 대답을 잘하는 LLM 성능은 다음을 통해 확인 가능하다.
<a href="https://leaderboard.dnotitia.com/"> https://leaderboard.dnotitia.com/</a>


## 참고 문서
<a href="https://artificialanalysis.ai/?intelligence-tab=intelligence"> https://artificialanalysis.ai/?intelligence-tab=intelligence</a>

 <a href="https://doi.org/10.48550/arXiv.2307.03109">https://doi.org/10.48550/arXiv.2307.03109</a>
 
<a href="https://arxiv.org/abs/2303.08774"> https://arxiv.org/abs/2303.08774</a>

<a href="https://arxiv.org/abs/2406.01574"> https://arxiv.org/abs/2406.01574</a>

<a href="https://paperswithcode.com/dataset/gpqa"> https://paperswithcode.com/dataset/gpqa</a>

<a href="https://aihub.or.kr/leaderboard/view.do"> https://aihub.or.kr/leaderboard/view.do</a>

<a href="https://leaderboard.dnotitia.com/"> https://leaderboard.dnotitia.com/</a>
