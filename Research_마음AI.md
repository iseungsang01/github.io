
## 기업 개요
마음AI 는 머신러닝과 빅데이터 기술 기반의 AI 솔루션과 서비스를 제공하는 한국전자통신연구원(ETRI) 연구소 기업이다.


## 기업 보유 모델 정리

### MAAL (Multilingual Adaptive Augmentation Language-model)

1) 모델 설명  
MAAL은 다국어(한국어 고성능 포함) 대형 언어 모델(LLM)로 설계됐다. DeepSeek([2024.12 사업보고서 기준](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20250814003106))나 Llama([huggingface 공개모델 기준](https://huggingface.co/models?search=maum-ai))를 기반으로 한국어 성능을 대폭 강화한 LLM이며, 온프레미스 방식을 통해 성능과 보안성을 갖추고 있다.
밑의 그림처럼 필요한 수준에 맞는 MAAL 제품군 3가지를 운영하고 있으며, 안전성을 갖춘 업무 효율성을 증진시켜주는 LLM AI 도구이다. 입력은 자연어 텍스트이고 출력은 생성 텍스트이다.
파라미터 개수를 통해 유추해보면, MAAL Albatross는 671B으로, Deepseek V3의 Parameter 수와 같다. 따라서 공개되지 않은 MAAL Albatross는 Deepseek V3 기반의 fine-tuning 모델로 보인다.

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202508172022.png" width="600">
</div>

마음 AI 홈페이지에서 Public cloud로 돌아가고 있는 MAAL hummingbird와 Albatross를 사용해본 결과, 기본적인 세팅이 조금 다른 것을 확인하였다. MAAL hummingbird는 특별한 프롬프트 없이 바로 질문에 대답하였으나, Albatross의 경우, 내재된 프롬프트를 먼저 실행하여, 페르소나를 미리 형성하며, 멀티모달이 가능하다는 특징이 있었다.   
정리하면, Public cloud에 제공되는 MAAL Albatross모델의 경우는, 베이스 모델 (pretrained) 위에서 도메인 특화 튜닝 (PEFT/LoRA 등) → 지시 (instruction) 튜닝 → 안전·정책 필터링을 거 배포되고 있음을 확인하였다.

<p align="center">
<img src="https://wikidocs.net/images/page/293587/image_202509030901.png" width="500"\>
<br>
<small> MAAL hummingbird 구동 </small>
<br>
<img src="https://wikidocs.net/images/page/293587/image_202509030858.png" width="500"\>
<br>
<small> MAAL Albatross 구동 </small>
</p>
  
  
MAAL 자체는 LLM으로 텍스트 기반의 모델이나, MAAL-Vision 모델(멀티모달)도 개발하였으며, Llama를 기반으로 하고 있다. 아래 그림에서처럼 공개된 ~20B 수준의 KOFFVQA (한국어 시각 질의응답 Benchmark)에서 전체 8등 수준으로, nc varco-vision이 5위, 네이버의 하이퍼클로바가 9등인 것을 보면, 상당히 높은 수준의 모델 성능을 보여주는 것을 확인할 수 있다. (25.08.16 기준)  
(2024년 3월에는 parameter 개수가 8B의 텍스트 모델이었는데, 최근 2024년 12월, 11B 수준의 비전 모델으로 모델 업그레이드함)

![](https://wikidocs.net/images/page/293587/image_202508161732.png)
출처 : [https://huggingface.co/spaces/maum-ai/KOFFVQA-Leaderboard](https://huggingface.co/spaces/maum-ai/KOFFVQA-Leaderboard)
  
  
2) 내부 아키텍처  
학습 파이프라인은 당연하게도, Instruction tuning (지도학습 기반, 데이터셋을 가지고 학습하는 것을 의미)이며, Fine tuning의 방식으로 학습하였고, base 모델은 Llama 3.2이 Transformer-decoder에 autoregressive LLM이다. Fine tuning시에는 KoreanVQA와 추가적인 다른 데이터셋(OCR, math 등)을 기반으로 학습하였다.

3) 강점  
강점으로는 한국어 성능 보강, On-premise를 통한 보안 강화, 플랫폼 통합성이다.
먼저, 한국어 성능 보강은 라마 3.2에서 파생 모델 튜닝을 통해 한국어 논리·추론 평가 (LogicKor 등)에서 좋은 성능을 보여주고 있고, 많은 국가 프로젝트 수주가 이를 뒷받침한다.
다음으로, 온프레미스 지향은 데이터 지역성·보안 요구에 맞춘 배포 모델 제공 (폐쇄망에서도 운영 가능)한다는 강점이 있다.
마지막으로, 플랫폼 통합성으로, 마음 오케스트라와 결합하여, 모듈을 통합하여 사용할 수 있다.

추후에는 MLOps와 연동하여, 사용자들이 직접 데이터셋을 가지고 모델을 더 Fine-tuning 할 수 있는 구동 형태를 만들어주는 등의 방식으로, 유저 친화적인 방식으로 발전할 수 있을 것으로 보인다. 

### SUDA (Seamless Uninterrupted Dialogue Assistant)

1) 모델 설명  
SUDA는 단일 파이프라인으로 음성 입력 → STT → LLM → TTS를 처리하는 통합 음성대화 엔진이다.  
Zero Latency를 가지고 있어 AI 발화 도중에 새로운 요구를 하더라도, 설명을 멈추고 바로 새로운 요구에 응답하는 특징을 가지고 있다.  
퀄컴 기반의 오프라인 상항의 실시간 대화를 제공하며, 총 처리 지연을 1.5초 이하로 최적화하였다.  
(출처 : [https://pulse.mk.co.kr/news/english/11197328](https://pulse.mk.co.kr/news/english/11197328))
  
    
    
2) 음성 대화 엔진 산업 핵심 기술 정리  
마음 AI의 기술에 대한 상세정보들이 정확하게 나오지 않아, 현재 음성 대화 엔진에서 어떤 기술이 사용되는지 확인하였다.  
  
Front-End (ASR/VAD/Wake-word 등): 자동 음성 인식 (ASR), 실시간 음성 신호 처리 (VAD), 특정 키워드 입력 시 시스템 발화 (Wake-word, 예시로 "시리~" 나 "빅스비~"라고 부르면 답변하는 것을 생각하면 됨), 노이즈 보정 (Beamforming), 음성 증강 데이터 기반 훈련을 한다.   
  
ASR (Automatic Speech Recognition, 자동 음성 인식) : 스트리밍 디코더 (CTC/RNN-T 등) 또는 hybrid 모델 (Conformer+RNN-T), 디코더를 최적화하여 음성 신호에 가장 가까운 단어를 찾는 과정이다.  
NVIDIA의 Canary/Parakeet, IBM의 granite, OpenAI의 Whisper 등이 ASR Leaderboard 상위권을 차지중이다.   
(출처 : [https://huggingface.co/spaces/hf-audio/open_asr_leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard))  
  
Dialog Manager: LLM (또는 경량 대체 모델)을 통해 의도 분석, 다중 발화 (중첩 발화) 처리 등을 한다.     
TTS(Text-to-Speech, 음성 합성) 엔진: 멀티스피커 스타일 TTS, 감정과 톤 제어하여, 생성한 텍스트를 직접 목소리에 감정을 담아 말하도록 설계한다.   
  
On-device 최적화: Neural connection pruning(신경망 연결 가지치기, 필요한 파라미터만 활성화시키는 MoE 구조랑 조금 다르게 신경망에서 중요하지 않은 부분 완전히 삭제) and parameter quantization(매개변수 양자화, 모델 계산을 저용량 숫자로 바꿈), NPU 가속, pruning을 통한 적은 메모리 사용등을 통해 On-device에서도 작은 시스템에서도 품질이 높은 소형 음성 인식기를 만들게 되었다.   
(출처 : ["OPTIMIZING SPEECH RECOGNITION FOR THE EDGE" 논문](https://arxiv.org/pdf/1909.12408))  
  
Latency reduction: partial hypotheses (부분적인 말을 듣고 전체적으로 어떤 말을 할지 예상해서 미리 답변 생성), endpointing 최적화, speculative decoding (답변후보를 여러 가지 준비하여, 가장 맞는 대답을 빠르게 내놓는다.)을 고려하여, 끊김 없이 대화가 이어지도록 latency를 최대한 줄인다.  
마음 AI의 경우도 직접 밝히지는 않았지만, 이런 방식으로 latency를 1.5초 내로 줄인 것으로 보인다.  

3) 강점   
오프라인 작동: 네트워크가 불안정하거나 완전 차단된 환경(공항·공장·국방)에서도 실시간 대화를 제공한다. 
End-to-End 통합: STT → LLM → TTS 연쇄 파이프라인을 통합 운영하여 지연·불일치 감소시켰다.  
현장 강건성: 소음·다중 화자·방음 환경에서의 성능 튜닝이 가능한 제품화 포인트가 있고, 실전 검증 사례가 존재한다. 


### WoRV — World model for Robotics and Vehicle control

1) 모델 설명  
WoRV는 시각·센서(라이다/IMU 등) 기반의 세계 모델 (world model)으로, 인식 (perception) → 상황 이해 (semantic scene) → 행동 생성 (trajectory/controls)까지 연결하는 end-to-end 또는 modular 로봇 제어 스택이다. 입력은 카메라 영상·라이다·IMU·거리 센서 등 멀티 센서 스트림 + (선택적) 언어 명령, 출력은 제어 신호 (경로, 속도, 제스처) 또는 행위 계획 (action plan)이다. WoRV의 핵심은 시각을 ‘언어적으로’ 해석해 고수준 지시 (“저 박스 집어 옆에 놓아라”)를 저수준 제어로 변환하는 것이다.  

2) 월드 모델 산업 핵심 기술 정리
마음 AI의 기술에 대한 상세정보들이 정확하게 나오지 않아, 현재 월드 모델에서 어떤 기술이 사용되고 있는지 확인하였다. 
Perception module: CNN/Transformer 기반 비전 인코더, 객체 탐지·세그멘테이션, depth/3D reconstruction, 라이다 fusion.  
World-model: latent space에서 환경의 동적/정적 상태를 예측하는 예측 네트워크 (contrastive predictive coding / latent dynamics).  
Task policy / Planner: Behavior cloning + RL (IL+RL fine-tuning)으로 목표 달성 정책을 학습하고, 안전 제어층 (heritage PID/Model Predictive Control 병용) 포함한다.  
Sim2Real pipeline: 도메인 랜덤화, 물리 엔진 보정, 고정밀 시뮬레이터 기반 데이터 생성한다.  
Language grounding: LLM (예: MAAL)과의 인터페이스를 통해 자연어 지시를 행동 템플릿으로 변환한다.  

3) 강점 (차별성)  
멀티 센서 융합 + 언어 연동: 시각 정보를 자연어로 해석하고 행동으로 연결하는 능력으로, 안내·농기계·물류·경비 등 다양한 현장에 직접 적용 가능하다.
Sim2Real 적용 경험: 농기계 등 현장 적용 사례와 전시 시연을 통해 실전 적합성을 검증한 바 있다.  

### RFM — Robot Foundation Model (상위 통합 모델)

1) 모델 설명  
RFM은 MAAL, SUDA, WoRV 등 개별 파운데이션 모델을 상위 수준에서 통합하여, 다양한 로봇 플랫폼 (안내·경비·물류·반려 등)에 범용적으로 적용 가능한 멀티모달 로봇 두뇌다.  
입력: 비전·오디오·센서·언어·메타데이터  
출력: 종합적 행동 플랜, 대화·표현, 제어 명령  
RFM의 목표는 “로봇별로 별도 알고리즘을 개발하지 않고도 동일한 두뇌를 다양한 도메인에 재활용”하는 것이다. 최근 회사가 RFM 상용화 추진·성공을 발표했다는 보도가 여러 매체에 나왔다.  

2) 내부 아키텍처  
Hierarchical design: 공통 베이스 (멀티모달 인코더) + 도메인 헤드 (안내·경비·물류 등) + 안전·실행 런타임.  
Cross-modal alignment: 텍스트·비전·행동 latent space 정합, 행동 예측을 위한 trajectory generator.  
Edge deployment: 전용 임베디드 하드웨어 (SoC/NPU)와 프레임워크 (ONNX/TensorRT/TVM) 최적화.  
Management: 중앙 관리 (오케스트라)로 모델 업그레이드·정책 패치·위험 롤백 수행.  

3) 강점 (차별성)  
범용성: 단일 플랫폼으로 다수 로봇 제품 라인에 적용 가능 → 개발비·유지비 획기적 절감.  
임베디드 HW 라인업: 소프트웨어 + 하드웨어 패키지로 제공해 납품·설치 문제를 한꺼번에 해결 가능.  
**RFM에서의 선두적인 기술력을 보유** (이는 부록 부문에 논문을 포함하여 자세히 기술하였음)

## 비즈니스 모델(BM)

마음 AI는 크게 세 개의 핵심 카테고리로 수익원을 창출한다.

### 프로젝트형 구축 (SI/컨설팅 중심)

이 카테고리는 고객 맞춤형 AI 솔루션 개발에 집중한다. 예를 들어, 제조업체의 특정 품질 검사용 대화형 로봇, 공공기관의 보안 감시용 안내·상호작용 에이전트, 금융기관의 문서 검색 기반 직원 지원용 LLM 구축 등이 해당된다.  

프로세스는 다음과 같이 구성된다: 고객 현장 학습 데이터 수집 → 요구 조건 분석 → PoC (Proof-of-Concept) 실행 → 도메인 튜닝 → 온프레미스/온디바이스 배포 → 테스트 및 통합 → 유지보수.  

이 과정에서 전체 프로젝트 수익은 일회성 라이선스 + 개발 컨설팅 비용 + 튜닝 비용 + 초기 유지보수 장기 계약 구조로 구성되는 경우가 많다.  

23년도에 프로젝트를 보면 국가 기반 사업들 위주로 수주를 받았으며, 이는 추후 유지보수 측면에서의 추가 수익의 가능성을 시사함과 동시에, 국내에서 마음 AI의 입지를 보여주는 사례들이라고 할 수 있다.

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202508242040.png" width="700">
</div>

### 플랫폼/API 기반 반복수익

‘마음 오케스트라 (Maum Orchestra)’ 플랫폼을 통해, AI 모델 라이프사이클을 일괄 자동화할 수 있게 한다.  

데이터 수집부터 모델 구성·훈련·튜닝·배포·실험 관리·API 제공·로그 수집 모두 이 플랫폼 위에서 진행된다.  

과금 방식은 구독형(Subscription) + 사용량 기반 과금(Usage-based pricing)이 혼합된 형태로, 기업 전체 AI 사용량/규모에 맞춰 유연하게 조정된다.  

이 부분이 반복적이고 예측 가능한 예측형 수익(Predictable Revenue) 축으로, 손익분기점 도달을 견인하는 핵심 드라이버다.  


  
---
  
프로젝트형 구축이나 플랫폼/API 기반으로 현재 마음 AI에서 주력으로 만들고 있는 상품은 AICC (AI 콜센터)이며, 다음과 같은 구조로 구성되어 있다. 뉴스 인터뷰를 통해서도, AICC의 비중이 상당히 클 것임을 짐작할 수 있다. (매출의 목표 달성은 2분기 공시가 나온 현재로서는 어려워보인다.)  

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202508241836.png" width="500">
</div>

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202509051723.png" width="500">
<br>
<small>
(출처 : <a href="https://www.youtube.com/watch?v=xElPj_RafOw">"팍스 경제 TV 뉴스 RFM 기반 피지컬 AI 시장 주도···마음AI, 올해 매출 170억원 목표"</a>)
</small>
</div>


현재 마음 AI에서 진행하고 있는 프로젝트와 그 회사, 그리고 앞으로 진행 예정인 프로젝트와 회사에 대해서 간략하게 명시되어 있다. 그리고 마음 AI에서 예시로 제공하고 있는 사례를 보면, 다음처럼 각 경우에 대해서 어떻게 실행할지에 대한 코드를 시각적으로 보여주고 있어, 쉽게 알고리즘을 파악할 수 있다. 

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202508241836_Fu2iIoG.png" width="500">
</div>
<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202508241842.png" width="500">
</div>


### 엔진/디바이스 라이선스

MAAL (LLM 엔진), SUDA (온디바이스 음성대화 스택), WoRV (월드모델 로봇 두뇌), 그리고 향후 RFM (로봇 파운데이션 모델)까지.  

라이선스 방식: 연간 라이선스 계약 + 유지보수/업그레이드 포함 형태.  

적용처로는 AICC, 현장 디바이스 단위 탑재, 로봇 단위 탑재 등으로 과금 모델이 세분화된다.  

이러한 A → B → C 구조는 “프로젝트형 PoC 기반 초기 진입”에서 “플랫폼 전환으로 반복수익 확보” → “엔진 라이선스 중심으로 확장 구조화”로 이어지는 전략적 수익 전환 흐름으로 설계된 것으로 보인다.  

## 산업 분석 – Physical AI

마음 AI가 속한 산업은 Physical AI, 즉 '실존 공간과 물리적 디바이스·로봇과 결합된 AI'로, 밸류체인은 크게 세 계층으로 나눌 수 있다:  
<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202509030941.png" width="500">
</div>

### 상류 (공급 측면)
- 데이터 수집 및 라벨링  
  현장 음성 데이터, 영상/센서 데이터, 언어 콜로그램, 산업 도메인 문서 등.  
  고객사 도메인 요구사항을 반영한 도메인 특화 데이터가 중요.  

- 컴퓨팅·인프라  
  훈련용 GPU 클러스터: AI 모델 학습 및 튜닝에 필수.  
  온프레미스 배포가 중요한 고객(보안·프라이버시 요구 높은 공공·국방·금융 등)을 위해, 고객사 현장에 장착되는 엣지 서버, NPU/ARM 기반 경량 서버 개발·보급.  

- 모델 아키텍처·알고리즘 리서치  
  MAAL, SUDA, WoRV, RFM에 해당하는 AI 코어 아키텍처 설계. 예: LLM 튜닝 전략 (LoRA·PEFT), 음성 연속 처리 파이프라인, 시뮬→현장 전이 학습 설계 등.  

### 중류 (플랫폼/도구)
- Maum Orchestra 플랫폼  
  데이터 및 실험 관리, 모델 튜닝 자동화, 파이프라인 재현(Repeatability), 배포·운영 모듈, 게이트웨이 API 등 모듈을 통합한 툴킷.  
  MLOps 자동화 (버전 관리, 실험 추적, 롤백, 배포 안전성, 모니터링, 추론 메트릭 수집 등).  
  클라우드 및 온프레미스 하이브리드 운영: 사내망 배포, 프라이빗 클라우드, 또는 완전 폐쇄망 운영 가능.  
  플랫폼 가격 세분화: Enterprise tier, Usage tier, 기능 확장 패키지 등으로 구성.  
 
- 보안·프라이버시 레이어  
  민감 정보 마스킹, 감사 로그, 접속 제어, 검열·정책 필터 등 규제 준수 기능 포함.  

### 하류 (응용/실현)
- AICC (인공지능 컨택센터): SUDA 기반 현장 언어 대응 + 백엔드 시스템 호출. 고객 문의 응대, 대화 요약, 이슈 안내 등.  
- 스마트 시티/공항 안내 로봇: WoRV/RFM 기반 시각·언어·감지 통합 대응.  
- 공장/물류 로봇: 장비·창고·경로 인식, 자율 이동, 언어 명령 이해.  
- 국방/치안/경비용 시스템: 현장 자동화, 자율 경비·상황 인식, 보안 기반 언어 대응 (보안 필터 설계).  

## 부록
### 기업 매출 및 기업 정보 정리

<div style="text-align: right; font-size: 0.9em; color: #666; margin-bottom: 10px;">
    <em>단위 : 억원</em>
</div>

<div style="text-align: center; margin: 20px 0;">
    <img src="https://wikidocs.net/images/page/293587/image_202508161643.png" alt="재무데이터" style="max-width: 100%; height: auto;">
</div>


<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202508161623.png" width="450">
</div>

출처 : DART 전자공시시스템, 이승상

### RFM에서의 기업의 해자 찾기   
마음 AI는 AI 3대 학회 (NeurIPS, ICML, ICLR) 중 하나인 NeurIPS(신경정보처리시스템학회) 2024 워크숍에서 최우수논문상 (Outstanding Paper Awards)를 수상하였다. 워크숍 주제는 "Workshop on Open-World Agents: Synergizing Reasoning and Decision-Making in Open-World Environments(OWA-2024)"라는 것이었으며, 이는 Open World Agent 분야에서 최고수준의 기술력을 가지고 있음을 시사한다.
실제 공식 매체에서도 마음 AI의 지향성이 RFM인 것으로 볼 때, 현재의 AI 솔루션의 대부분은 AICC 부분에 있지만, 앞으로의 AI 솔루션의 대부분은 RFM 부문에서 이루어질 것으로 보인다.

따라서 기업의 해자를 분석하기 위해서는 수상 논문인 "Integrating Visual and Linguistic Instructions
for Context-Aware Navigation Agents"에 대해서 자세히 확인할 필요가 있다.
동사는 이 논문에서 CANVAS라는 프레임워크를 이용하였으며, COMMAND라는 human-annotated (인간이 결과를 라벨링해놓은) instruction을 네비게이션 로봇을 학습하는 데이터셋으로 잡았다.

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202509021815.png" width="450">
</div>

  학습 방식은 Imitation Learning(IL)을 통해서 하였으며, 이는 보상 함수가 필요 없는 학습 방법이다. IL에서는 multimodal action distributions (멀티모달 행동 분포)를 모델링하는 것이 어려운데, CANVAS는 이를 연속 경로 지점 128개를 K-mean clustering (유사한 데이터 포인트들을 군집화하는 방법임) 하여 변환하고, 데이터셋의 Map을 Isaac sim이라는 가상 로봇시뮬레이션 환경에서 돌릴 수 있게 지도를 추출하고, 인간이 최적 경로를 스케치한 것을 답으로 설정, 시뮬레이션 환경에서 조작하여 데이터를 수집하였다. 

<div align="center">
<img src="https://wikidocs.net/images/page/293587/image_202509021820.png" width="450">
</div>

로봇 모델의 학습은 다음 하단의 그림처럼 로봇 front view, 지금까지의 온 경로를 맵에 표현한 Canvas Map, 언어 지시 사항 L을 input으로 받아서 Vision Transformer를 기반으로 PD 제어를 통해 움직임을 학습하였다. 
이를 가지고 각각 CANVAS-L(Idefics2 8B 기반)과 CANVAS-S(SigLIP-L + Qwen2-0.5B, 경량화하여 0.7B으로 조정) 모델을 제작하였다.
  
실험 결과는 로봇 운영체제인 ROS의 내비게이션 패키지 모음인 ROS NavStack보다 우수한 성능을 보임을 입증하였다. ([ROS NavStack Code](https://github.com/ros-planning/navigation))
  
<p align="center">
<img src="https://wikidocs.net/images/page/293587/image_202509040029.png" width="400" \>
<img src="https://wikidocs.net/images/page/293587/image_202509040033.png" width="400">
</p>

즉, 정리하면 현재 위치한 곳의 Map을 알고, 로봇에 Front View를 받을 수 있다면, 지정된 언어 지시 사항을 기반으로, 예상 경로를 생성하고 이를 모방학습하는 것에서 좋은 성능을 얻었다는 것이다. 이의 발전 가능성을 생각해보면, 일단 처음 경로를 K-clustering 128개로 나누었던 것을 생각해보면, 도로가 길어질수록 clustering 개수가 선형적으로 증가할 것이며, 군집이 커질수록 실행시간에 영향을 크게 주기 때문에, 현재 데이터셋이 30~200m 정도 였던 점을 고려했을 때, 추후 마을이나 캠퍼스를 선회하는 셔틀 정도의 사이즈나 공장 내부를 돌아다니는 로봇 등에 사용할 수 있을 것이라고 생각한다. 
 

## 참고 문서
- [DART 사업보고서](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20250814003106)
- [KOFFVQA Leaderboard](https://huggingface.co/spaces/maum-ai/KOFFVQA-Leaderboard)
- [ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
- [마음AI - 2024 NeurIPS 수상 논문](https://openreview.net/forum?id=U6wyOnPt1U)
- [마음AI ChatBot(MAAL)](https://maum.ai/maum-gpt)
- [ROS NavStack Code](https://github.com/ros-planning/navigation)
