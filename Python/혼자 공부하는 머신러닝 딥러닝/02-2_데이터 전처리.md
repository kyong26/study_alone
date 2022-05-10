# 혼자 공부하는 머신러닝 딥러닝
## 02-2. 데이터 전처리
### 데이터 전처리, 표준점수, 브로드캐스팅

---

* numpy의 column_stack()은 전달받은 리스트를 일렬로 세운 다음 차례대로 나란히 연결함
* 연결할 리스트는 파이썬 튜플(tuple)로 전달함


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


import numpy as np

fish_data = np.column_stack((fish_length, fish_weight))

# 데이터가 아주 큰 경우 파이썬 리스트로 작업하는 것은 비효율적임
# 넘파이 배열은 핵심 부분이 C, C++과 같은 저수준 언어로 개발되어서 빠르고 데이터 과학 분야에 알맞게 최적화 되어 있음

fish_target = np.concatenate((np.ones(35), np.zeros(14)))
```


```python
# 사이킷런으로 훈련 세트와 테스트 세트 나누기
from sklearn.model_selection import train_test_split

# Default로 25%를 테스트 데이터로 떼어냄
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

# 분리한 데이터 확인
print(train_target.shape, test_target.shape)
```

    (36,) (13,)



```python
# 데이터를 무작위로 나눌 때, 샘플이 충분히 잘 섞이지 않을 수 있음
# 도미와 빙어 개수 35:14 -> 2.5:1
# 테스트 샘플의 비율은 3.3:1 (샘플링 편향)

print(test_target)
```

    [1. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.]



```python
# stratify 매개변수에 타깃데이터를 전달하면 클래스 비율에 맞게 데이터를 나눔
train_input, test_input, train_target, test_target \
     = train_test_split(fish_data, fish_target, stratify=fish_target, random_state=42)

# 분리한 데이터 확인: 2.75:1 수준으로 비슷해 짐
print(test_target)
```

    [0. 0. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1.]



```python
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
kn.score(test_input, test_target)
```




    1.0




```python
# 도미(1) 군집과 유사한 샘플인데, 빙어(0)로 분류함
print(kn.predict([[25, 150]]))
```

    [0.]



```python
import matplotlib.pyplot as plt

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```


![output_7_0](https://user-images.githubusercontent.com/52664532/166327389-78e7c866-4609-4ea1-8758-1147bed0ddac.png)
    



```python
distances, indexces = kn.kneighbors([[25, 150]])
```


```python
plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexces,0], train_input[indexces,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

#가까운 샘플 5개중 4개가 빙어->빙어로 분류됨
```

![output_9_0](https://user-images.githubusercontent.com/52664532/166327463-3f8c92ff-1fd7-4818-a5d8-3541cb95d68f.png)




```python
print(train_input[indexces])
print(train_target[indexces])

# 이웃 샘플까지의 거리
print(distances)
```

    [[[ 25.4 242. ]
      [ 15.   15. ]
      [ 14.3  14.3]
      [ 13.   13. ]
      [ 12.2  12.2]]]
    [[1. 0. 0. 0. 0.]]
    [[ 92.00086956 135.36986371 136.121196   137.52454326 138.39320793]]



```python
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexces,0], train_input[indexces,1], marker='D')

# x축의 범위를 지정함
plt.xlim((0,1000))
plt.xlabel('length')
plt.ylabel('weight')

plt.show()

# 생선의 길이(x)는 고려대상이 되기 어려움, 생선의 무게(y)가 주 고려대상이 됨 -> 스케일이 다름
# 스케일이 다를 경우 올바른 예측이 어려움(특히 거리 기반 알고리즘의 경우)
# 특성값을 일정한 기준으로 맞춰주어야 함 -> 데이터 전처리 진행(Data Processing)
```


    
![output_11_0](https://user-images.githubusercontent.com/52664532/166327511-3e4f6cb1-7569-418e-aaf3-08dc8e3fcc5c.png)
    



```python
# 표준점수(Standard score)를 활용한 데이터 전처리

mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

print(mean, std)
```

    [ 27.29722222 454.275     ] [  9.98244253 323.04751919]



```python
# 브로드캐스팅(Broad Casting): 일정 조건을 부합하는 다른 형태의 배열끼리 연산을 수행하는 것

train_scaled = (train_input - mean) / std
```


```python
# 전처리 데이터로 모델 훈련하기
plt.scatter(train_scaled[:,0], train_scaled[:,1])

new = ([25, 150] - mean) / std
plt.scatter(new[0], new[1], marker='^')

# x축의 범위를 지정함
plt.xlabel('length')
plt.ylabel('weight')

plt.show()
```

![output_14_0](https://user-images.githubusercontent.com/52664532/166327600-bdcbb25b-d5f1-4a73-b949-eed3f6af2ae6.png)
    


```python
kn.fit(train_scaled, train_target)
test_scaled = (test_input - mean) / std
kn.score(test_scaled, test_target)
print(kn.predict([new]))

# 도마로 예측함
```

    [1.]



```python
distances, indexces = kn.kneighbors([new])

plt.scatter(train_scaled[:,0], train_scaled[:,1])

new = ([25, 150] - mean) / std
plt.scatter(new[0], new[1], marker='^')

plt.scatter(train_scaled[indexces,0], train_scaled[indexces,1], marker='D')

plt.xlabel('length')
plt.ylabel('weight')

plt.show()
```

![output_16_0](https://user-images.githubusercontent.com/52664532/166327642-042e4b6f-3eed-484a-976d-5fec44b9af75.png)
