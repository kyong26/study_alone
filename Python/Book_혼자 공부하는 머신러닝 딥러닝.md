# 혼자 공부하는 머신러닝 딥러닝
## 02-1. 훈련 세트와 테스트 세트
### 지도학습, 비지도학습, 훈련세트, 테스트세트

* 머신러닝 알고리즘은 크게 지도학습(Supervised Learning), 비지도학습(Unsupervised Learning)으로 나뉨
* 지도학습에서는 데이터와 정답을 입력(Input)과 타깃(Target)이라 하고, 이 둘을 합쳐서 훈련 데이터(Training Data)라고 부름
* 테스트 세트: 평가에 사용하는 데이터
* 훈련 세트: 훈련에 사용되는 데이터
---


```python
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 
               31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 
               34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 
               41.0, 41.0, 9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 
               12.2, 12.4, 13.0, 14.3, 15.0]

fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 
               475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 
               575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 
               920.0, 955.0, 925.0, 975.0, 950.0, 9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 
               11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

fish_data = [[l, w] for l,w in zip(fish_length, fish_weight)]
fish_target = [1]*35 + [0]*14

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# data-> test data, training data로 분리하기
# 샘플링 편향: 랜덤하게 섞이지 않음, test는 도미만 있고 train엔 빙어만 있음 -> score: 0 
train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]

# 훈련
kn = kn.fit(train_input, train_target)

# 테스트
kn.score(test_input, test_target)
```




    0.0




```python
# 샘플 섞기
import numpy as np

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

input_arr.shape # (샘플 수, 특성 수 )

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
```


```python
# 섞은 결과 scatter plot으로 확인하기
import matplotlib.pyplot as plt 

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```


    
![png](output_3_0.png)
    



```python
kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)

kn.predict(test_input)
```




    array([0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0])




```python
test_target
```




    array([0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0])




```python

```
