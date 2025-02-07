# SK네트웍스 Family AI 캠프 9기 2차 프로젝트  




# 목차
### 1. 팀 소개
### 2. 프로젝트 개요 (소개, 필요성, 목표)
### 3. 기술 스택
### 4. WBS
### 5. 데이터 전처리 결과
### 6. 인공지능 학습 결과
### 7. 수행결과
### 8. 한 줄 회고


---


## 1. 팀 소개  
**팀명:** (팀 이름)  
**팀원:**  
- **김도연**: [GitHub](https://github.com/kimdy158)
- **김영서**: [GitHub](https://github.com/youngsu98)
- **김하늘**: [GitHub](https://github.com/nini12091)
- **윤환**: [GitHub](https://github.com/MNYH)
- **조민훈**: [GitHub](https://github.com/alche22)
 

---

## 2. 프로젝트 개요  
### 📌 프로젝트명: 온라인 학습 수강생 이탈 예측  

### 📌 프로젝트 소개  

온라인 학습 플랫폼이 발전하면서 학생들의 학습 패턴을 분석하고 이탈 여부를 예측하는 것이 중요한 과제가 되었다. 학습자의 **이탈을 방지하고 학습 경험을 개선**하기 위해, 데이터 기반의 예측 모델을 구축하는 것이 필요하다. 본 프로젝트에서는 **온라인 학습자의 행동 데이터를 기반으로 이탈 여부를 예측**하는 머신러닝 모델을 개발하고 평가한다.

### 📌 프로젝트 필요성 (배경)  
온라인 학습 환경에서는 학생들의 자율성이 높지만, 그만큼 이탈률도 높아질 수 있다. 주요 원인으로는 동기 부족, 학습 난이도, 환경적 요인 등이 있다. 이러한 문제를 해결하기 위해 다음과 같은 필요성이 존재한다:

- 학생들의 학습 패턴을 분석하여 이탈을 사전에 예측하고 예방 조치를 마련
- 맞춤형 학습 지원 시스템을 구축하여 학습 지속률 향상
- 교육 기관 및 플랫폼 운영자의 효율적인 리소스 관리 지원

### 📌 프로젝트 목표  
- 학습자의 이탈 여부를 예측하는 머신러닝 모델 개발
- 다양한 학습 데이터 분석을 통해 주요 이탈 요인 파악
- 최적의 모델을 선정하여 실무 적용 가능성 검토

---

## 3. 기술 스택  
| 분야 | 기술 |
|------|------|
| **데이터 분석** | Pandas, NumPy, Scikit-learn |
| **머신러닝** | XGBoost, LightGBM, Random Forest |
| **딥러닝 (필요시)** | TensorFlow, PyTorch |
| **기타** | Git, Docker, Streamlit, AWS/GCP |

---

## 4. 작업 분담 (WBS)  
| 작업 항목 | 담당자 |
|----------|------|
| 데이터 수집 | (담당자) |
| 전처리 | (담당자) |
| 모델링 | (담당자) |
| 모델 최적화 | (담당자) |
| 결과 분석 | (담당자) |
| 보고서 작성 | (담당자) |

---
## 5. 데이터 전처리 (EDA)

📌 **데이터 전처리 과정**  
- 결측값 처리: 일부 컬럼에 결측값이 존재했으나, 이들을 적절히 처리하거나 제거하여 데이터의 일관성을 유지했습니다.
- 형식 변환: 문자열 형식으로 되어 있는 데이터를 카테고리형 데이터로 변환하고, 수치형 데이터는 스케일링을 통해 모델 학습에 적합한 형태로 변환했습니다.
- 이상치 처리: 학습자의 성적이나 클릭 수 등에서 비정상적으로 큰 값들이 발견되었고, 이를 이상치로 간주하여 적절히 처리했습니다.
- 특성 엔지니어링: highest_education, imd_band와 같은 카테고리형 변수는 원-핫 인코딩을 적용하여 모델에 입력될 수 있도록 변환했습니다.

📌 **EDA 인사이트**  
- 특정 변수(A, B, C)와 고객 이탈률 간 강한 상관관계 발견  
- 고객의 연령, 사용 패턴, 결제 방식이 이탈에 영향을 미치는 주요 요소로 분석됨  
최종적으로 사용된 데이터는 학습자의 성적, 클릭 수, 교육 수준, 지역, 수업 이수 학점 등이 포함된 데이터셋으로, 이들 모두 이탈 여부를 예측하는 데 중요한 특성으로 작용했습니다.

## 6. 인공지능 학습 결과
< 중요하다고 싶은것만 입력 + 모델 학습 속도(시간비용)>
| 모델명 | 정확도 | 설명 |
|----------|------|-----|
| 랜덤포레스트 |  | 비교적 좋은 예측 성능을 보였지만, 모델의 해석이 어려운 편 |
| 로지스틱회귀 |  | 간단하고 빠른 모델이었지만, 성능이 상대적으로 낮았 |
| LightGBM |  | XGBoost보다 더 빠른 학습 시간과 더 나은 예측 성능 |
|  |  |  |
|  |  |  |
|  |  |  |

## 7. 수행결과

| 모델명 | 정확도 | 정밀도 | 재현율 | f1 | 설명 |
|----------|------|------|-----|------|------|
| 랜덤포레스트 |  |  |   |  | |

이 결과를 바탕으로, 최종 모델은 실제 온라인 교육 환경에서 학습자의 이탈 여부를 예측하는 데 사용될 수 있을 것으로 기대됩니다. 이 모델은 학습자의 행동 패턴과 학습 상황을 분석하여, 이탈 가능성이 높은 학습자에게 선제적으로 개입할 수 있는 기회를 제공합니다.

## 8. 한 줄 회고
- **김도연**: 
- **김영서**: 
- **김하늘**: 
- **윤환**: 
- **조민훈**: 
