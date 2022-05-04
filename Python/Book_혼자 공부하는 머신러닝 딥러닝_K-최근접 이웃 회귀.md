# 혼자 공부하는 머신러닝 딥러닝
## 03-1. K-최근접 이웃 회귀
### 회귀, K-최근접 이웃 회귀, 결정계수, 과대적합과 과소적합

---
* 지도학습 알고리즘은 크게 분류와 휘귀(Regression)으로 나뉨 -> 두 변수 사이의 상관관계를 분석하는 방법
* K-최근접 이웃 분류: 예측하려는 샘플에 가까운 샘플 k개를 선택한 후, 이 샘플들의 클래스를 확인하여 다수 클래스를 새로운 샘플의 클래스로 예측함
* K-최근접 이웃 회귀: 예측하려는 샘플에 가까운 샘플 k개를 선택한 후, 이 샘플들의 타겟의 평균으로 새로운 샘플의 타겟을 예측함


```python
# bit.ly/perch_data

import numpy as np 

perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])
```


```python
import matplotlib.pyplot as plt

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```

![output_2_0](https://user-images.githubusercontent.com/52664532/166680714-3ae2244e-0d7d-4ef7-b1ec-79d24812631b.png)




```python
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)
```


```python
# -1: 나머지 원소 개수로 모두 채우기, 1: 두 번째 크기를 1로 채우기

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor()
knr.fit(train_input, train_target)

# 결정계수 R: 0~1
print("R-Score:", knr.score(test_input, test_target)) 

# MAE: 예측값에서 평균 19g의 오차가 있음
from sklearn.metrics import mean_absolute_error
test_prediction = knr.predict(test_input)

mae = mean_absolute_error(test_target, test_prediction)
print("MAE:", mae)
```

    R-Score: 0.992809406101064
    MAE: 19.157142857142862



```python
# 과대적합 vs 과소적합

print("trian set R-score:", knr.score(train_input, train_target))

# test set의 R-Score보다 낮음 -> 과소적합
# 과대적합: 훈련세트 성능 >>> 테스트세트 성능
# 과소적합: 훈련세트 성능 < 테스트세트 성능 or 두 세트 모두 점수가 너무 낮은 경우

# 과소적합의 원인: 모델이 너무 단순해서 훈련 세트에 적절히 훈련되지 않았거나, 세트의 크기가 매우 작은 경우
# -> 모델을 더 복잡하게 만들거나, 세트의 크기를 더 크게 만듦
# -> K-최근접 이웃 알고리즘의 경우, 이웃 k의 개수를 줄이면 모델이 더 복잡해짐(국지적인 패턴에 민감)

knr.n_neighbors = 3 
knr.fit(train_input, train_target)

# 이웃 5->3
print(knr.score(train_input, train_target))
print(knr.score(test_input, test_target))
```

    trian set R-score: 0.9698823289099254
    0.9804899950518966
    0.9746459963987609

