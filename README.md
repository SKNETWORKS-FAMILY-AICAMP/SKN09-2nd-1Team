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
  6️⃣ **모델 학습 결과**  
  7️⃣ **시스템 화면**  
  8️⃣ **결론**  
  9️⃣  **기대 효과**  
  🔟  **한 줄 회고**  

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

![image](https://github.com/user-attachments/assets/ffc326b1-4cd1-415d-8aca-bb4a5188a078)
###### -출처 : https://www.manuscriptlink.com/society/kips/conference/ask2024/file/downloadSoConfManuscript/abs/KIPS_C2024A0265

📉 **온라인 학습 플랫폼의 높은 이탈률**  
- 평균 이탈률 13%로, 교육 플랫폼의 **수익 감소 및 학습 효율 저하**에 직결  
- **Coursera, Udemy, Khan Academy** 등 글로벌 플랫폼도 동일한 **수강생 유지율** 문제에 직면  

---

### 3️⃣ 프로젝트 목표

#### ✅ 사용자 맞춤형 머신러닝 모델 선택 기능

- 웹사이트에서 다양한 모델을 선택하고 학습 가능, 학습 완료 후 각 모델의 성능비교

#### ✅ 이탈 가능 학습자 식별 및 정보 제공

- 이탈 확률이 높은 학습자 리스트 확인

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
#### 데이터 ERD

![image](https://github.com/user-attachments/assets/78635970-76d7-42ae-a0a0-161099a03c11)

1. 🧑‍🎓 **studentInfo.csv**
   - 학생의 인구통계학적 정보 (성별, 연령, 지역 등)
2. 📝 **studentAssessment.csv**
   - 학생의 평가(과제 및 시험) 점수
3. 🖱️ **studentVle.csv**
   - 학생들의 VLE 상호작용(클릭 수 등) 기록

#### ⚙️ 4. 주요 사용 변수
| 변수명 (column name) | 변수 설명 (description)                             | 변수 유형 (data type) |
|----------------------|------------------------------------------------|------------------|
| `id_student`         | 학습자 고유 ID (각 학생을 구분하는 키)                 | 🔢 정수형 (Integer) |
| `code_module`        | 수강한 강좌의 코드 (과목 식별자)                     | 📝 문자열 (String)  |
| `highest_education`  | 학습자의 최고 교육 수준 (고등학교, 학사, 석사 등)         | 📝 문자열 (String)  |
| `studied_credits`    | 학생이 수강한 학점 (이수하려는 학점)                   | 🔢 정수형 (Integer) |
| `imd_band`           | 학습자의 사회경제적 수준 (IMD 지표)                   | 📝 문자열 (String)  |
| `final_result`       | 학습자의 최종 결과 (Pass, Fail, Withdraw 등)          | 📝 문자열 (String)  |
| `id_assessment`      | 평가(시험, 과제 등) ID                              | 🔢 정수형 (Integer) |
| `score`              | 학생이 평가에서 받은 점수                           | 🔢 실수형 (Float)   |
| `sum_click`          | 총 클릭 수 (온라인 학습 플랫폼 내 클릭 횟수)           | 🔢 정수형 (Integer) |
| `mean_click`         | 평균 클릭 수 (평균 클릭 횟수)                       | 🔢 실수형 (Float)   |
| `log_sum_click`      | 총 클릭 수의 로그 변환 값                           | 🔢 실수형 (Float)   |
| `log_mean_click`     | 평균 클릭 수의 로그 변환 값                         | 🔢 실수형 (Float)   |
| `log_studied_credits`| 수강 학점의 로그 변환 값                            | 🔢 실수형 (Float)   |
| `scaled_studied_credits` | 표준화된 수강 학점                           | 🔢 실수형 (Float)   |
| `scaled_score`       | 표준화된 평가 점수                                 | 🔢 실수형 (Float)   |
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
```python
final_merged_data['imd_band'] = final_merged_data['imd_band'].fillna('20-30%')
final_merged_data['score'] = final_merged_data['score'].fillna(0)
final_merged_data['imd_band'] = final_merged_data['imd_band'].replace('10-20', '10-20%')
```

- 목적 변수: 이진 분류를 위해 형태 변환
0 = 학습 포기 (Withdrawn)
1 = 학습 지속 (Pass, Fail, Distinction)

```python
new_final_result_encodings = {
    'Withdrawn': 0,
    'Distinction': 1,
    'Fail': 1,
    'Pass': 1
}
```

- imd_band는 범주형 변수는 각각의 고유한 문자열을 숫자로 라벨인코딩 수행

```python
new_education_encodings = {
    'Post Graduate Qualification': 0,
    'HE Qualification': 1,
    'A Level or Equivalent': 2,
    'Lower Than A Level': 3,
    'No Formal quals': 4
}
```

- 활동 기록인 클릭 로그 데이터의 편향된 분포를 확인하고 로그 스케일링 수행

![output4](https://github.com/user-attachments/assets/2f154498-1732-4add-86b5-96dd3cdf3562)

![output3](https://github.com/user-attachments/assets/eaae731f-ce90-4308-a6f4-281cc945c18c)

- score, studied_credits 특성은 정규분포를 따르지 않아 MinMax스케일링 수행

![output6](https://github.com/user-attachments/assets/acc62c5d-b262-4404-998c-b86bcef23c02)


## 2️⃣ EDA 인사이트 및 주요 패턴

### 🆚 2.1 이탈자 vs. 수료자 비교

| 구분         | 📊 총 인원 수 | 🎓 학력 (highest_education) | 🌐 사회경제 수준 (imd_band) | 🖱️ 클릭 로그 합 (log_sum_click) | 🖱️ 클릭 로그 평균 (log_mean_click) | 🎯 **이수 학점 (scaled_studied_credits)** | 🏆 **평가 점수 (scaled_score)** |
|:-------------|:--------------:|:----------------------------:|:-----------------------------:|:-----------------------------:|:-----------------------------------:|:------------------------------------------:|:------------------------------------:|
| 🚨 **이탈자(0)** | 24,598명    | 2.26                         | 4.13                         | 7.01                         | 1.44                              | **0.278**                                  | **0.685**                              |
| 🟢 **수료자(1)** | 160,318명  | 2.15                         | 4.37                         | 7.40                         | 1.47                              | **0.235**                                  | **0.760**                              |

---

### 🔎 인사이트 및 주요 패턴

📉 **1. 이수 학점과 평가 점수의 차이:**  
- 이탈자는 **평균 이수 학점**이 더 높지만, **평가 점수**는 더 낮음  
- 👉 **이수 학점이 높을수록, 점수가 낮을수록 이탈률 증가**

🌐 **2. 사회경제적 수준의 차이:**  
- 이탈자는 수료자보다 **사회경제적 수준(imd_band)**이 다소 높게 나타남  
- 👉 **사회적 수준이 높을수록 이탈률이 증가**  

🖱️ **3. 학습 활동(클릭 로그)의 차이:**  
- 이탈자는 **클릭 로그의 합과 평균**이 모두 낮은 경향을 보임  
- 👉 **온라인 학습 활동이 적을수록 이탈 가능성 증가**  

### 📊 **📈 전체 이탈률:** **12.53%**

## 2.2 특성별 이탈률 분석

### ✅ 1. 최종 학력별 이탈률

![최종 학력별 이탈률](https://github.com/user-attachments/assets/67dcc494-e03f-40f1-b420-2e540547ed53)
![최종 학력별 이탈률](https://github.com/user-attachments/assets/a4aa1522-e1ae-4e70-b373-9f504f96b224)

🔍 **Insight**  
- **사회적 수준이 높을수록 이탈률 증가**  
- **No Formal quals**(학력 미보유) 그룹의 이탈률이 가장 높음  

---

### ✅ 2. 경제 수준별 이탈률

![경제 수준별 이탈률](https://github.com/user-attachments/assets/639c3224-66a7-4bb5-b07f-2e8b401b035c)

🔍 **Insight**  
- **경제 수준이 높을수록 이탈률 증가**  
- **상위 90-100% 구간**이 가장 높은 이탈률을 보임  

---

### ✅ 3. 시험 점수별 이탈률

![시험 점수별 이탈률](https://github.com/user-attachments/assets/774ceab6-1507-4ae1-bb7c-5475e398d994)
![시험 점수별 이탈률](https://github.com/user-attachments/assets/01300dfd-c2cb-41e9-97fe-020547695c5e)

🔍 **Insight**  
- **점수가 낮을수록 이탈률 상승**  
- **0~30점 구간**에서 이탈률이 가장 높고, 점수가 오를수록 이탈률 하락  

---

### ✅ 4. 이수 학점별 이탈률

![이수 학점별 이탈률](https://github.com/user-attachments/assets/18ad1a27-64e6-4a37-b4ca-82f49bff8063)

🔍 **Insight**  
- **이수 학점이 많을수록 이탈률 상승**  
- **220~240학점 구간**에서 이탈률이 급격히 증가  

### 📌 **종합 인사이트**

- **경제 수준과 학력 수준이 높을수록 이탈률이 증가**  
- **시험 점수는 낮을수록, 이수 학점은 많을수록 이탈 위험 상승**  
---

## 6. 모델 학습 결과

### 1️⃣ 선택 모델 및 성능 비교
#### 📊 모델 성능 비교
![image](https://github.com/user-attachments/assets/170bd2b6-ac63-4945-a949-27cdc82116a9)
- **Gradient Boosting (sum)**: Accuracy 0.902로 가장 높은 성능을 기록하였으며, 모든 지표에서 우수한 결과를 보였습니다.
- **Random Forest (sum)** 및 **Gradient Boosting (mean)** 모델이 그 뒤를 이었으며, 전반적으로 결정 트리 기반 모델이 뛰어난 성능을 보였습니다.
---
#### **하이퍼 파라미터 튜닝 결과**
  ![image](https://github.com/user-attachments/assets/45b14c38-723c-4c9c-b0b7-25a289c6e634)
- **Random Forest**와 **Gradient Boosting** 모델은 튜닝 후에도 안정적인 성능을 유지하며 상위권을 차지하였습니다.
---
#### **앙상블 모델 결과**

#### 📊 **Sum Click 기반 성능 결과** <br>
![image](https://github.com/user-attachments/assets/378a2e49-014c-4b64-a346-e36d5f1d5edc)
- **Sum Click 기반**: 로그 변환된 클릭 수와 점수가 주요한 특징으로 선정되어 성능이 개선되었습니다.  

#### 📊 **Mean Click 기반 성능 결과** <br>
![image](https://github.com/user-attachments/assets/60f30e15-d819-44bb-a71b-e7400f6ba506)
- **Mean Click 기반**: 평균 클릭 수를 기반으로 학습한 모델에서도 유사한 패턴이 관찰되었습니다.  
---
### 2️⃣ 모델 결과 시각화
![image](https://github.com/user-attachments/assets/c07ebe93-236f-4f4a-ba3a-fa9bff5a65f0)
- 이탈 여부를 예측한 결과는 수료자 그룹은 **93.58%로 높은 예측도를 보이고, 이탈 그룹 또한 **90.72%로** 높은 예측도를 보였습니다. 
---
### 3️⃣ 특성 중요도 분석

🎯 **Gradient Boosting**
- scaled_score와 log_sum_click이 중요도로 분석
- 
![image](https://github.com/user-attachments/assets/711a0401-847c-49f2-a913-d4be6ba39e4e)
![image](https://github.com/user-attachments/assets/60ec620e-cb9b-4b04-89f1-921a83aeaf38)

---

🎯 **LightGBM**
![image](https://github.com/user-attachments/assets/c04bdd3c-b35f-47f7-a401-997d89374384)
![image](https://github.com/user-attachments/assets/fdbdaafa-b51e-40bb-968e-da0f53134443)

---

🎯 **Random Forest**
![image](https://github.com/user-attachments/assets/88a5aad6-7430-41ae-8bd4-d449fe28ab99)
![image](https://github.com/user-attachments/assets/462d6d1f-7dee-483d-bb58-827309d70a67)

---

## 7. 시스템 화면

### 1️⃣ 웹사이트 구현

### 🚀 주요 기능

- ✅ **모델 학습 기능**
  - 사용자가 직접 머신러닝 모델 및 파라미터를 선택하여 학습 가능

- ✅ **모델 성능 비교**
  - 정확도, F1 Score 등의 성능 지표를 그래프로 시각화하여 비교 가능

- ✅ **이탈 가능성 예측**
  - 이탈 가능성이 높은 학습자 목록을 제공

- ✅ **문제점 분석 및 맞춤형 지원 방안 추천**
  - 이탈 가능 학생의 문제점을 분석하고 맞춤형 지원 방안 추천



### **소개 페이지**
![introduce](https://github.com/user-attachments/assets/01f5ebed-e3f9-4aa0-8c2c-f1d5b365e666)


### **모델 학습 페이지**
![model_page_1](https://github.com/user-attachments/assets/4fb7a650-5e56-447c-bfb7-4e974b462e45)
![model_page_2](https://github.com/user-attachments/assets/13382740-1f25-4b07-955e-ce59ffb25fb6)
![model_page_3](https://github.com/user-attachments/assets/3fae9fa3-216e-4912-8807-eb259beb7dd1)
![model_page_4](https://github.com/user-attachments/assets/af1bdd4d-b086-450e-9884-ed2fb906db3b)



### **최종 결과 페이지**
![result_1](https://github.com/user-attachments/assets/7f8cc71c-2699-486d-b8cf-13e1cddd6edd)
![result_2](https://github.com/user-attachments/assets/73d0d0f1-1ceb-4935-a894-252c5b1cba66)
![result_3](https://github.com/user-attachments/assets/3e57ee8a-1c71-48d0-bf39-b355633746e7)
![result_4](https://github.com/user-attachments/assets/911293ae-6653-4b1d-bbd4-afe84ff67caf)
![result_5](https://github.com/user-attachments/assets/4ba62504-53a2-4c73-ba5d-f8f402e5af03)



### **참여도 예측 페이지**
![Participation_1](https://github.com/user-attachments/assets/fdb73ae3-99b5-471c-acba-0281b554dfb4)
![Participation_2](https://github.com/user-attachments/assets/37ff8452-d1c0-45bd-9d2e-549efd993df1)
![Participation_3](https://github.com/user-attachments/assets/957b1a68-0222-4403-9d9a-5fcf349846cd)
![Participation_4](https://github.com/user-attachments/assets/fff071b2-d9fd-495b-90f2-06428c61f126)




### **결과 예측  페이지**
![search_result_1](https://github.com/user-attachments/assets/7dc2ff40-4212-417a-97b1-4607f5e4c347)
![search_result_2](https://github.com/user-attachments/assets/82a179eb-be89-400d-8ffc-2cc3430131c5)
![search_result_3](https://github.com/user-attachments/assets/2cbba1cf-1175-4601-bce2-4ba76f27ea5a)
![search_result_4](https://github.com/user-attachments/assets/0781de34-192d-497e-83a2-e6167cb8bf76)
![search_result_5](https://github.com/user-attachments/assets/fd89bf60-1868-4606-8103-0a16eed9a6a8)



<br><br>

## 8. 결론
- **Gradient Boosting 모델(Accuracy 90.2%, F1 Score 0.91)이** 가장 우수한 성능을 보였으며, **클릭 로그와 시험 점수**가 주요 요인임을 확인했습니다. 
- 🖱️ **클릭 로그와 참여도**: 평균 클릭 수 1.44 이하의 학습자는 이탈 가능성이 65% 이상 증가하였고, 이는 **온라인 학습 환경에서의 참여도 관리**의 중요성을 확인할 수 있습니다.
- 🧠 **시험 성적과 학습 지속성**: 시험 점수가 30점 미만일 경우 이탈률이 급격히 상승하고, **적절한 피드백 제공과 동기 부여 전략**의 필요성을 확인할 수 있습니다.
- 🌐 **사회경제적 요인의 영향**: IMD 지수가 90% 이상인 고소득층 학습자들의 이탈률이 상대적으로 높아, **맞춤형 학습 콘텐츠 및 유연한 학습 환경** 제공이 중요함을 확인하였습니다.

🎯 이번 프로젝트는 단순한 예측을 넘어 **학습자 행동 패턴을 기반으로 한 인사이트 도출**에 초점을 맞추었으며, **이탈 예방을 위한 전략적 의사결정 지원 도구**로서의 가능성을 확인하였습니다.

---

## 9. 기대 효과

**🏫 관리자 측면:**
- 데이터 기반 접근을 통해 **이탈 가능성 예측 및 관리 전략** 수립
- 학습 데이터 분석을 통해 강의 설계와 학습 콘텐츠의 **품질 개선**
- 웹 인터페이스를 통해 **모델 성능 비교 및 결과 시각화** 제공

**📈 산업적 가치 측면:**
- 이탈률 감소를 통한 **플랫폼 운영 비용 절감**과 **수익성 향상**
- 지속적인 데이터 분석으로 **교육 서비스의 경쟁력 강화** 및 **맞춤형 학습 솔루션 제공**

---

## 10. 한 줄 회고
- **김도연**: 
- **김영서**: 데이터 전처리부터 모델링까지의 과정에서 불균형 데이터 처리가 얼마나 중요한지 다시금 깨달았고, 다양한 모델을 쌓아 올릴수록 예측 성능이 개선될 가능성이 높다는 점을 실감한 프로젝트였다.
- **김하늘**: 
- **윤환**: 머신러닝을 활용해 학습자 이탈을 예측하고 맞춤형 지원 방안을 제안하며, 데이터 선택과 하이퍼파라미터 튜닝의 중요성을 체감할 수 있었다.
- **조민훈**: 
