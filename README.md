# SK네트웍스 Family AI 캠프 9기 2차 프로젝트  

<br>

<details>
  <summary><strong>📑 프로젝트 목차 </strong></summary>
  <br>

  1️⃣ **팀 소개**  
  2️⃣ **프로젝트 개요**  
  3️⃣ **기술 스택**  
  4️⃣ **작업 분담 (WBS)**  
  5️⃣ **탐색적 데이터 분석 (EDA)**  
  6️⃣ **머신러닝 학습 결과**  
  7️⃣ **결론**  
  8️⃣ **한 줄 회고**  

</details>


---

# 1. 팀 소개

### **팀명:** DGMON(Dropout Guard Manager On Network)

### **팀원:**  
|![김도연](https://github.com/user-attachments/assets/df766bcf-53bd-4e2e-900e-ac812934c0d4) |![김영서](https://github.com/user-attachments/assets/705537f0-f571-4df8-878e-b1b2be82ab13) |![김하늘](https://github.com/user-attachments/assets/a7873135-dc15-4ea8-b946-7a2eafbca678)| ![윤환](https://github.com/user-attachments/assets/6eee4c24-904a-48dd-96c9-e192d4eb8011)| ![조민훈](https://github.com/user-attachments/assets/32b1165e-f7d6-49b6-b7d2-3abfd31ebc2c) |
|:-----:|:------:|:------:|:-----:|:------:|
| 김도연 | 김영서 | 김하늘 | 윤환 | 조민훈 |
| [@doyeon158](https://github.com/doyeon158) | [@youngseo98](https://github.com/youngseo98) | [@nini12091](https://github.com/nini12091) | [@MNTH](https://github.com/MNYH)  | [@alche22](https://github.com/alche22) |

<br>
<br>

---

# 2. 프로젝트 개요 

## 📌 온라인 학습 플랫폼 수강생 이탈 예측

### 1️⃣ 프로젝트 소개

온라인 학습 플랫폼에서 **수강생의 이탈을 사전에 예측**하고, **주요 원인을 파악**하여 **수료율을 개선**하는 것이 목표입니다.

### 🛠️ **프로젝트 내용**  
- **머신러닝 기반 예측 모델**을 통해 이탈 가능성을 사전에 탐지  
- **개별 학습자 특성 분석**을 바탕으로 **맞춤형 지원 방안** 추천  
- **모델 선택 및 학습 웹사이트**를 구축하여 사용자가 직접 성능을 확인할 수 있는 인터페이스 제공  


### 🌟 **핵심 기능**

| 🛠️ 기능                      | 📝 설명                                                |
|--------------------------|---------------------------------------------------|
| **모델 선택 및 성능 비교** | XGBoost, 랜덤 포레스트, 로지스틱 회귀 등 다양한 모델을 선택하여 학습 |
| **모델 성능 시각화**     | R1 Score, 정확도 등 **주요 성능 지표 시각화**로 이해도 향상    |
| **이탈 가능성 학습자 탐지** | 이탈 가능성이 높은 **학습자 목록 및 상세 분석** 제공           |
| **맞춤형 지원 방안 추천** | 학습 패턴을 바탕으로 **이탈 예방을 위한 전략 추천**      |

---

### **2️⃣ 프로젝트 필요성**

![image](https://github.com/user-attachments/assets/4c693ded-3f5f-4a2c-9513-e20e41432d92)
###### -출처 : https://www.manuscriptlink.com/society/kips/conference/ask2024/file/downloadSoConfManuscript/abs/KIPS_C2024A0265

📉 **온라인 학습 플랫폼의 높은 이탈률**  
- 평균 이탈률 13%로, 교육 플랫폼의 **수익 감소 및 학습 효율 저하**에 직결  
- **Coursera, Udemy, Khan Academy** 등 글로벌 플랫폼도 동일한 **수강생 유지율** 문제에 직면  

---

### 3️⃣ 프로젝트 목표

#### ✅ 사용자 맞춤형 머신러닝 모델 선택 기능 제공

- 웹사이트에서 다양한 모델을 선택하고 학습 가능, 학습 완료 후 각 모델의 성능비교 제공

#### ✅ 이탈 가능 학습자 식별 및 정보 제공

- 이탈 확률이 높은 학습자 리스트 제공

#### ✅맞춤형 지원 방안 자동 추천 
- **수동적인 사용자 관리** → **비효율적**  
- **머신러닝 기반 맞춤형 개입** → **학습자의 패턴 분석을 통한 최적화 전략 도출**  

#### ✅ **관리자 (UX) 제공**  
- **웹 페이지**에서 **사용자가 직접 모델을 선택**하여 학습 결과 확인 가능  
- **모델 성능과 데이터 분석 결과** 제공

---

### 4️⃣ 데이터 개요

#### 📉 Open University Learning Analytics Dataset (OULAD) 소개

---

#### 🗂️ 1. 데이터셋 개요

OULAD는 영국 Open University에서 제공하는 학습 분석 데이터셋으로, 학생들의 학습 행동과 성과를 분석하는 연구에 활용됩니다. 본 데이터셋은 학습자들의 **행동(Behavior)** 및 **성과(Performance)** 요소를 포함하고 있으며, 총 **22개 코스, 32,593명의 학생 데이터** 기반으로 구성되어 있습니다.

📌 **주요 특징**
- 🎓 **교육 분야 연구에 최적화된 데이터셋**
- 🔍 **다양한 학습 행동 및 성과 지표 포함**
- 🛠️ **머신러닝 모델 학습 및 분석에 유용**

#### 🧾 2. 데이터 구성

- 📊 **학습 행동 데이터**: 학생들의 학습 환경(VLE)에서의 활동 기록 (**총 10,655,280개의 클릭 로그**)
- 🎯 **성과 데이터**: 학생들의 평가(assessment) 점수 및 최종 성적

#### 📂 3. 주요 데이터 파일

1. 🧑‍🎓 **studentInfo.csv**
   - 학생의 인구통계학적 정보 (성별, 연령, 지역 등)
2. 🗓️ **studentRegistration.csv**
   - 학생의 코스 등록 상태 및 시기
3. 📝 **studentAssessment.csv**
   - 학생의 평가(과제 및 시험) 점수
4. 🖱️ **studentVle.csv**
   - 학생들의 VLE 상호작용(클릭 수 등) 기록
5. 🎓 **studentFinalResult.csv**
   - 학생들의 최종 성적 결과

#### ⚙️ 4. 주요 사용 변수

![image1](https://github.com/user-attachments/assets/83063868-5071-4dd4-882f-88aff2690718)
---


## 🛠️ 기술 스택

| 분야             | 기술 |
|------------------|------|
| **데이터 분석** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white) |
| **머신러닝**    | ![XGBoost](https://img.shields.io/badge/-XGBoost-EB4C42?logo=xgboost&logoColor=white) ![LightGBM](https://img.shields.io/badge/-LightGBM-00A651?logo=lightgbm&logoColor=white) ![Random Forest](https://img.shields.io/badge/-Random%20Forest-228B22?logo=treehouse&logoColor=white) |
| **기타**       | ![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white) ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white) |

---

## 4. 작업 분담 (WBS)  

![image9](https://github.com/user-attachments/assets/b482f4d7-fdda-4bc3-80d1-70f72572d915)

---

## 5. 탐색적 데이터 분석 (EDA)

### 1️⃣ 데이터 전처리 과정
- 결측값 처리: 
imd_band 와 score, sum_click에 결측값이 존재, 이를 최빈값과 0으로 대체
![image](https://github.com/user-attachments/assets/a1e173b9-51fe-4979-aeac-59120ae40865)

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

- **학생의 이수학점과 학생의 평가 점수**(studied_credits, score)의 평균 차이가 두드러짐
- **사회 경제적 수준과 클릭 로그 합**(imd_band, sum_click)에도 차이를 보임
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

✅ 사용자가 직접 머신러닝 모델 및 파라미터 선택 후 학습 가능

✅ 모델 성능 비교 (정확도, AUC 그래프 제공)

✅ 이탈 가능성이 높은 학습자 목록 제공

✅ 이탈 가능 학생의 문제점 분석 및 해결책 자동 추천

#### A) 분석 모델 선택

**첫 페이지**
![introduce](https://github.com/user-attachments/assets/4fea846a-5e8e-44f3-9bdc-b37f2910a70f)

<br>

**모델 선정**

![model_page_1](https://github.com/user-attachments/assets/0ee512df-3fda-4b63-9614-e07a5d3a0946)

<br>

**파라미터 선정**

![model_page_2](https://github.com/user-attachments/assets/6878cb4b-cbbd-4196-a79c-060c9742f93f)
![model_page_3](https://github.com/user-attachments/assets/33fc6f15-cc27-4795-869e-6bb8c492b765)

<br>

**분석 수행**

![model_page_4](https://github.com/user-attachments/assets/4ff77a16-8fa9-447f-9bb6-09243c32d547)



#### B) 분석 모델 시각화

**분석 결과 확인**

![result_1](https://github.com/user-attachments/assets/737b9486-b78e-4b66-a83f-4438be3f92f5)

<br>

#### B) 
**1111**
![Participation_1](https://github.com/user-attachments/assets/b96197b6-bc2b-4a03-9354-418f4c8aca78)

<br>

**2222**
![Participation_2](https://github.com/user-attachments/assets/0932f2ce-b9af-4f98-8cbe-f64b39f7762a)

<br>

**3333**
![Participation_3](https://github.com/user-attachments/assets/add3e8af-c4c5-437d-b466-a44b3ac4ece7)

<br>

**4444**
![Participation_4](https://github.com/user-attachments/assets/81e3dd46-b05c-4c1c-a220-6f0387906012)

<br>

#### D)
**1111**
![result_1](https://github.com/user-attachments/assets/3e297a9a-46f9-455a-9e0d-e389e7c61256)

<br>

**2222**
![result_2](https://github.com/user-attachments/assets/bc8f735c-0e6b-4c5b-810e-e0c8d9730aea)

<br>

**3333**
![result_3](https://github.com/user-attachments/assets/e698c4ec-5951-4b03-b3b3-ec5ef6c48e65)

<br>

**4444**
![result_4](https://github.com/user-attachments/assets/0324b512-de97-4ee0-9fc3-04c8928e8272)

<br>

**5555**
![result_5](https://github.com/user-attachments/assets/6c0abe33-0e6f-4e78-b8fd-1572348fbbe2)

<br>


#### E) 이탈 학생 정보 확인

**학생 정보 확인 페이지**

![search_result_1](https://github.com/user-attachments/assets/390f04c9-87a5-4113-b307-4f0c1e7a9b33)
![search_result_2](https://github.com/user-attachments/assets/d2129738-d476-485e-9e85-b0f23e792815)

<br>

**학생이 유지로 예측하는 경우**

![search_result_3](https://github.com/user-attachments/assets/aaf5f66d-5c7b-4759-9768-5555988f6af6)

<br>

**학생이 이탈로 예측하는 경우**

![search_result_4](https://github.com/user-attachments/assets/036ff44c-e3fc-4fc0-aa17-8f8cfbca31a1)

<br>

**이탈로 예측했을 때 지원 방안 제시**
 
![search_result_5](https://github.com/user-attachments/assets/0a83aab5-c683-4151-825a-d1e62aceeca2)



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
