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

![image](https://github.com/user-attachments/assets/ffc326b1-4cd1-415d-8aca-bb4a5188a078)
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
#### 데이터 ERD

![image](https://github.com/user-attachments/assets/78635970-76d7-42ae-a0a0-161099a03c11)

1. 🧑‍🎓 **studentInfo.csv**
   - 학생의 인구통계학적 정보 (성별, 연령, 지역 등)
2. 📝 **studentAssessment.csv**
   - 학생의 평가(과제 및 시험) 점수
3. 🖱️ **studentVle.csv**
   - 학생들의 VLE 상호작용(클릭 수 등) 기록

#### ⚙️ 4. 주요 사용 변수

![image](https://github.com/user-attachments/assets/cd77c014-bc0a-4237-b833-61c0ae55fe76)

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


### 2️⃣ EDA 인사이트 및 주요 패턴 
**2.1 이탈자 vs. 수료자 비교**

|  | 개수 count | highest_education | imd_band | log_sum_click | log_mean_click | **scaled_studied_credits** | **scaled_score** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 (이탈) | 24598 | 2.257826 | 4.125945 | 7.007977 | 1.438261 | **0.278277** | **0.685310** |
| 1 (이탈안함) | 160318 | 2.149952 | 4.369010 | 7.403126 | 1.473366 | **0.235432** | **0.760065** |

- **학생의 이수학점과 학생의 평가 점수**(studied_credits, score)의 평균 차이가 두드러짐
- **사회 경제적 수준과 클릭 로그 합**(imd_band, sum_click)에도 차이를 보임
- 전체 이탈률: 12.53%

- 🔍 주요 패턴 발견:

✅ 학생의 이수 학점이 높을수록, 학생의 평가 점수가 낮을수록 이탈률 상승

✅ 이탈자는 수료자보다 사회경제적 수준이 높음

✅ 이탈자는 수료자보다 클릭 로그 수가 더 낮음

**2.2 특성별 이탈률 분석**

✅ 최종 학력별 이탈률
![image](https://github.com/user-attachments/assets/67dcc494-e03f-40f1-b420-2e540547ed53)

![image](https://github.com/user-attachments/assets/a4aa1522-e1ae-4e70-b373-9f504f96b224)

✅ 경제 수준별 이탈률
![image](https://github.com/user-attachments/assets/639c3224-66a7-4bb5-b07f-2e8b401b035c)

✅ 시험 점수별 이탈률
![image](https://github.com/user-attachments/assets/774ceab6-1507-4ae1-bb7c-5475e398d994)
![image](https://github.com/user-attachments/assets/01300dfd-c2cb-41e9-97fe-020547695c5e)

✅ 이수 학점별 이탈률
![image](https://github.com/user-attachments/assets/18ad1a27-64e6-4a37-b4ca-82f49bff8063)

## 6. 머신러닝 학습 결과

### 1️⃣ 선택 모델 및 성능 비교
- **선택한 분류 모델**
![image](https://github.com/user-attachments/assets/170bd2b6-ac63-4945-a949-27cdc82116a9)

- **하이퍼 파라미터 튜닝 모델 추가 성능 비교**
  ![image](https://github.com/user-attachments/assets/45b14c38-723c-4c9c-b0b7-25a289c6e634)

- **앙상블 모델 결과**
- Sum Click 기반 성능 결과 <br>
![image](https://github.com/user-attachments/assets/378a2e49-014c-4b64-a346-e36d5f1d5edc)

- Mean Click 기반 성능 결과 <br>
![image](https://github.com/user-attachments/assets/60f30e15-d819-44bb-a71b-e7400f6ba506)


### 2️⃣ 모델 결과 시각화
![image](https://github.com/user-attachments/assets/c07ebe93-236f-4f4a-ba3a-fa9bff5a65f0)

### 3️⃣ 특성 중요도 분석
![image](https://github.com/user-attachments/assets/711a0401-847c-49f2-a913-d4be6ba39e4e)
![image](https://github.com/user-attachments/assets/60ec620e-cb9b-4b04-89f1-921a83aeaf38)
![image](https://github.com/user-attachments/assets/c04bdd3c-b35f-47f7-a401-997d89374384)
![image](https://github.com/user-attachments/assets/fdbdaafa-b51e-40bb-968e-da0f53134443)
![image](https://github.com/user-attachments/assets/88a5aad6-7430-41ae-8bd4-d449fe28ab99)
![image](https://github.com/user-attachments/assets/462d6d1f-7dee-483d-bb58-827309d70a67)

---

## 7. 시스템 화면

### 1️⃣ 웹사이트 구현

**📌 주요 기능:**

✅ 사용자가 직접 머신러닝 모델 및 파라미터 선택 후 학습 가능

✅ 모델 성능 비교 (정확도, F1 Score 그래프 제공)

✅ 이탈 가능성이 높은 학습자 목록 제공

✅ 이탈 가능 학생의 문제점 분석 및 해결책 자동 추천


### **소개 페이지**
![introduce](https://github.com/user-attachments/assets/4fea846a-5e8e-44f3-9bdc-b37f2910a70f)

### **모델 학습 페이지**
![model_page_1](https://github.com/user-attachments/assets/1a74bc8d-7fb4-44f4-a0e8-84880e43a20e)
![model_page_2](https://github.com/user-attachments/assets/55ab736d-37c3-4862-98b6-bce4ac17de4a)
![model_page_3](https://github.com/user-attachments/assets/4e9b7d49-3b21-4d59-a91e-62ff0bf44b21)
![model_page_4](https://github.com/user-attachments/assets/37278e1e-7810-4608-8f6f-d4169b3ff05e)


### **최종 결과 페이지**
![result_1](https://github.com/user-attachments/assets/1305c785-a667-4434-a7e9-6c41dae1e3bc)
![result_2](https://github.com/user-attachments/assets/5fdb2cf2-534e-4557-bd03-6926303aced8)
![result_3](https://github.com/user-attachments/assets/d78547f1-49bc-494b-baab-6fbedcf5cc4e)
![result_4](https://github.com/user-attachments/assets/d3f132a0-965f-4929-ac6e-94099ae8bdb3)
![result_5](https://github.com/user-attachments/assets/efa870af-e517-4bc8-95d6-7612f7d5b8f3)


### **참여도 예측 페이지**
![Participation_1](https://github.com/user-attachments/assets/06f1c889-e838-4617-bf5b-f37cd5dc52bf)
![Participation_2](https://github.com/user-attachments/assets/b893b149-98bb-4104-b54c-31a2225345d2)
![Participation_3](https://github.com/user-attachments/assets/46593f37-4aec-40d8-84fc-526453bfd7c9)
![Participation_4](https://github.com/user-attachments/assets/4fb1a393-4d2b-40d2-88c6-549f588de8ab)



### **결과 예측  페이지**
![search_result_1](https://github.com/user-attachments/assets/4d9a10a7-3728-45c9-bd0b-3ce8a68ef171)
![search_result_2](https://github.com/user-attachments/assets/98f2e1dd-adfd-4d92-8d78-f5834aefc35a)
![search_result_3](https://github.com/user-attachments/assets/f9a8e78a-ebb1-4ca5-9f2e-ba327a82fce6)
![search_result_4](https://github.com/user-attachments/assets/9d32dbd3-cdd0-4d2f-a0ef-e059da0f44f4)
![search_result_5](https://github.com/user-attachments/assets/ebde9800-8ee8-4b1d-900b-804a40ce22e9)

<br><br>

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
