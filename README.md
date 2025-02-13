# SK네트웍스 Family AI 캠프 9기 2차 프로젝트  

<br>

# 목차
### 1. 팀 소개
### 2. 프로젝트 개요

1) 프로젝트 소개
2) 프로젝트 필요성
3) 프로젝트 목표
4) 데이터 소개

### 3. 기술 스택
### 4. 작업 분담 (WBS)
### 5. 탐색적 데이터 분석 (EDA)

1) 데이터 전처리 수행과정
2) EDA 인사이트 및 주요패턴

### 6. 머신러닝 학습 결과

1) 선택 모델 및 성능 비교
2) 모델 결과 시각화
3) 특성 중요도 분석

### 7. 결론

1) 웹사이트 구현
2) 향후 과제

### 8. 한 줄 회고

<br><br>

---


# 1. 팀 소개

**팀명:** (팀 이름)

**팀원:**  
| 사진 | 1 | 2 | 3 | 4 |
|:-----:|:------:|:------:|:-----:|:------:|
| 김도연 | 김영서 | 김하늘 | 윤환 | 조민훈 |
| [@doyeon158](https://github.com/doyeon158) | [@youngseo98](https://github.com/youngseo98) | [@nini12091](https://github.com/nini12091) | [@MNTH](https://github.com/MNYH)  | [@alche22](https://github.com/alche22) |

<br>
<br>

---

## 2. 프로젝트 개요 

<br>

### 📌 프로젝트명: 온라인 학습 플랫폼 수강생 이탈 예측

### 1️⃣ 프로젝트 소개

- 온라인 학습 플랫폼에서 수강생의 수료를 달성하기 위해, 이탈하는 학생을 예측하고 주요 원인을 파악함.
- 머신러닝을 활용하여 학습자의 이탈을 예측하고, 맞춤형 개입 전략을 자동 추천하는 시스템을 구축.
- 또한, 사용자가 머신러닝 모델과 파라미터를 직접 선택하고 학습할 수 있는 웹사이트를 제작하여, 모델의 성능을 직접 확인할 수 있도록 함.

✅ 핵심 기능:
1. 다양한 머신러닝 모델(XGBoost, 랜덤 포레스트, 로지스틱 회귀 등)을 직접 선택하고 학습
2. 예측 모델 성능(AUC-ROC, 정확도) 비교 기능 제공
3. 이탈 가능성이 높은 학습자의 정보 제공
4. 이탈을 방지하기 위한 맞춤형 개선 전략 자동 추천

<br>

### 2️⃣ 프로젝트 필요성
📉 온라인 학습 플랫폼의 높은 이탈률 문제

- 온라인 강의를 등록한 학습자의 이탈률이 **13%**에 달하며, 교육 플랫폼의 수익 감소와 직결됩니다.
- Coursera, Udemy, Khan Academy 등 주요 온라인 교육 플랫폼에서도 수강생 유지율이 큰 도전 과제
- 학습자가 초기에는 적극적으로 참여하지만, 시간이 지날수록 학습 동기가 약화됨

🤖 머신러닝 기반 자동화된 개입의 필요성

- 기존의 수동적인 사용자 관리 방식은 효과가 낮으며, 머신러닝을 활용한 자동 이탈 예측 및 대응이 필수적입니다.
- 단순한 이메일 리마인더 → 효과 제한적
- 머신러닝 기반 맞춤형 개입 → 개별 학습자의 학습 패턴 분석 후 최적의 개입 전략 제공 가능

💡 사용자가 직접 모델을 선택하고 학습해볼 수 있는 기능 제공

- 일반적인 머신러닝 분석 결과를 제공하는 것이 아니라, 사용자가 원하는 모델을 직접 학습하고 성능을 비교할 수 있도록 함
- 데이터 분석 결과의 신뢰성을 제공

<br>

### 3️⃣ 프로젝트 목표

✅ 사용자 맞춤형 머신러닝 모델 선택 기능 제공

- 웹사이트에서 다양한 모델을 선택하고 학습 가능, 학습 완료 후 각 모델의 성능비교 제공

✅ 이탈 가능 학습자 식별 및 정보 제공

- 이탈 확률이 높은 학습자 리스트 제공

✅ 맞춤형 개입 전략 자동 추천

<br>

### 4️⃣ 데이터 개요

#### 📉 Open University Learning Analytics Dataset (OULAD) 소개

**데이터셋 개요**

OULAD는 영국 Open University에서 제공하는 학습 분석 데이터셋으로, 학생들의 학습 행동과 성과를 분석하는 연구에 활용됩니다. 본 데이터셋은 학습자들의 **행동(Behavior)** 및 **성과(Performance)** 요소를 포함하고 있으며, 총 **22개 코스, 32,593명의 학생 데이터** 기반

**데이터 구성**

- **학습 행동 데이터**: 학생들의 학습 환경(VLE)에서의 활동 기록 (총 10,655,280개의 클릭 로그)
- **성과 데이터**: 학생들의 평가(assessment) 점수 및 최종 성적

**주요 데이터 파일**

1. **studentInfo.csv** – 학생의 인구통계학적 정보 (성별, 연령, 지역 등)
2. **studentRegistration.csv** – 학생의 코스 등록 상태 및 시기
3. **studentAssessment.csv** – 학생의 평가(과제 및 시험) 점수
4. **studentVle.csv** – 학생들의 VLE 상호작용(클릭 수 등) 기록
5. **studentFinalResult.csv** – 학생들의 최종 성적 결과

**주요 사용 변수**
![image1](https://github.com/user-attachments/assets/83063868-5071-4dd4-882f-88aff2690718)

<br>

---


## 3. 기술 스택  
| 분야 | 기술 |
|------|------|
| **데이터 분석** | Pandas, NumPy, Scikit-learn |
| **머신러닝** | XGBoost, LightGBM, Random Forest |
| **기타** | Git, Streamlit |


<br>

---

## 4. 작업 분담 (WBS)  

![image9](https://github.com/user-attachments/assets/b482f4d7-fdda-4bc3-80d1-70f72572d915)

<br>

---

## 5. 탐색적 데이터 분석 (EDA)

### 1️⃣ 데이터 전처리 과정
- 결측값 처리: 
imd_band 와 score, sum_click에 결측값이 존재, 이를 최빈값과 0으로 대체함 (결측값이 시험을 보지 않아서 0으로 대체?)
- 목적 변수: 이진 분류를 위해 형태 변환
0 = 학습 포기 (Withdrawn)
1 = 학습 지속 (Pass, Fail, Distinction)
- code_module과 imd_band는 범주형 변수는 각각의 고유한 문자열을 숫자로 라벨인코딩 수행
- 활동 기록인 클릭 로그 데이터의 편향된 분포를 확인하고 로그 스케일링 수행

![output4](https://github.com/user-attachments/assets/2f154498-1732-4add-86b5-96dd3cdf3562)

![output3](https://github.com/user-attachments/assets/eaae731f-ce90-4308-a6f4-281cc945c18c)

- score, studied_credits 특성은 정규분포를 따르지 않아 MinMax스케일링 수행

![output6](https://github.com/user-attachments/assets/acc62c5d-b262-4404-998c-b86bcef23c02)

- 학생 아이디를 기준으로 데이터 병합
- 최종 데이터 <사진 추가>

### 2️⃣ EDA 인사이트 및 주요 패턴 
**2.1 이탈자 vs. 비이탈자 비교**

|  | 개수 count | highest_education | imd_band | log_sum_click | log_mean_click | **scaled_studied_credits** | **scaled_score** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 (이탈) | 24598 | 2.257826 | 4.125945 | 7.007977 | 1.438261 | **0.278277** | **0.685310** |
| 1 (이탈안함) | 160318 | 2.149952 | 4.369010 | 7.403126 | 1.473366 | **0.235432** | **0.760065** |

- **학생의 이수학점과 학생의 평가 점수**(**studied_credits, score)**의 평균 차이가 두드러짐
- **사회 경제적 수준과 클릭 로그 합(imd_band, sum_click)**에도 차이를 보임
- 전체 이탈률: 12.53%

- 🔍 주요 패턴 발견:
✅ 학생의 이수 학점이 높을수록, 학생의 평가 점수가 낮을수록 이탈률 상승
✅ 이탈자는 비이탈자보다 사회경제적 수준이 낮음
✅ 이탈자는 비이탈자보다 클릭 로그 수가 더 낮음


<br>

---

## 6. 머신러닝 학습 결과

### 1️⃣ 선택 모델 및 성능 비교
- **선택한 분류 모델**
- 랜덤포레스트, 그레디언트 부스팅, 결정 트리, KNN, XGBoost, LightGBM, 로지스틱 회귀
<표 추가>

### 2️⃣ 모델 결과 시각화
<시각화 자료 추가>

### 3️⃣ 특성 중요도 분석
<특성 중요도 사진 추가>
<설명 추가>

<br>

---

## 7. 결론

### 1️⃣ 웹사이트 구현

**📌 주요 기능:**
1️⃣ 사용자가 직접 머신러닝 모델 및 파라미터 선택 후 학습 가능
2️⃣ 모델 성능 비교 (정확도, AUC 그래프 제공)
3️⃣ 이탈 가능성이 높은 학습자 목록 제공
4️⃣ 이탈 가능 학생의 문제점 분석 및 해결책 자동 추천

#### A) 분석 모델 선택

**첫 페이지**
![model_page_1](https://github.com/user-attachments/assets/212d3203-477b-4ce2-b9e8-60570194feca)

<br>

**모델 선정**

![model_page_2](https://github.com/user-attachments/assets/d76b12a9-dd8c-44dc-8200-a0b0c62376b3)

<br>

**파라미터 선정**

![model_page_3](https://github.com/user-attachments/assets/d9492772-8ce5-46a1-ae9e-8a4699659a68)


<br>

**분석 수행**

![model_page_4](https://github.com/user-attachments/assets/40c1daa1-7396-415f-9110-43c221752a65)


#### B) 분석 모델 시각화

**분석 결과 확인**

![result_1](https://github.com/user-attachments/assets/737b9486-b78e-4b66-a83f-4438be3f92f5)


#### C) 이탈 학생 정보 확인

**학생 정보 확인 페이지**

![search_result_1](https://github.com/user-attachments/assets/08f180e2-4670-4113-85c8-fb07f3793fa4)

<br>

**학생이 유지로 예측하는 경우**

![search_result_2](https://github.com/user-attachments/assets/f724ab63-a76d-4a2c-829a-7d79c778fa3d)

<br>

**학생이 이탈로 예측하는 경우**

![search_result_3](https://github.com/user-attachments/assets/9d5630a6-7c1c-4fb2-9bfd-751fd747c69e)


<br>

**이탈로 예측했을 때 지원 방안 제시**
 
![search_result_4](https://github.com/user-attachments/assets/35acab4e-3bcb-42ed-8697-ba2ddcc72f80)


### 2️⃣ 향후 과제
- 머신러닝을 활용한 학습 지속률 개선 + 실질적인 비즈니스 성과 창출

<br>

---


## 8. 한 줄 회고
- **김도연**: 
- **김영서**: 
- **김하늘**: 
- **윤환**: 
- **조민훈**: 
