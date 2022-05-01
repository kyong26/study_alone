# 혼자 공부하는 머신러닝 딥러닝
## 01-3 마켓과 머신러닝
### K-최근접 이웃 알고리즘

* 알고리즘 구현을 위해서는, 데이터를 가지고 있기만 하면 됨! 예측시 가장 가까운 직선거리에 어떤 데이터가 있는지 살핌
* 단점은 이런 특징 때문에 데이터가 아주 많은 경우 사용하기 어려움. 
* 데이터가 크기 때문에 메모리가 많이 필요하고 직선거리를 계산하는데도 많은 시간이 필요함.
---

* 분류(Classification): 여러 개의 종류(혹은 class) 중 하나를 구별해 내는 문제
* 이진 분류(Binary Classification): 2개의 클래스 중 하나를 고르는 문제
* 특성(Feature): 데이터의 특성
* 모델(Model): 머신러닝 알고리즘을 구현한 프로그램


```python
# http://bit.ly/bream_list
# 도미 데이터

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
```


```python
# 산점도(Scatter Plot)를 그려 데이터 분포를 확인
import matplotlib.pyplot as plt 

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')

plt.show()
```


    
![png](output_3_0.png)
    



```python
# http://bit.ly/smelt_list 
# 빙어 데이터

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
```


```python
# 도미와 빙어의 데이터를 함께 scatter plot로 그리기

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')

plt.show()
```


    
![png](output_5_0.png)
    



```python
# K-최근접이웃(K-Nearest Neighbors)

length = bream_length + smelt_length
weight = bream_weight + smelt_length


fish_data = [[l,m] for l,m in zip(length, weight)]

fish_target = [1]*35 + [0]*14

from sklearn.neighbors import KNeighborsClassifier

# 훈련
kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)

# 평가: score, 0~1 값을 반환함
kn.score(fish_data, fish_target)
```




    1.0




```python
# 예측: 도미
kn.predict([[30, 600]])
```




    array([1])




```python
print(kn._fit_X)
```

    [[  25.4  242. ]
     [  26.3  290. ]
     [  26.5  340. ]
     [  29.   363. ]
     [  29.   430. ]
     [  29.7  450. ]
     [  29.7  500. ]
     [  30.   390. ]
     [  30.   450. ]
     [  30.7  500. ]
     [  31.   475. ]
     [  31.   500. ]
     [  31.5  500. ]
     [  32.   340. ]
     [  32.   600. ]
     [  32.   600. ]
     [  33.   700. ]
     [  33.   700. ]
     [  33.5  610. ]
     [  33.5  650. ]
     [  34.   575. ]
     [  34.   685. ]
     [  34.5  620. ]
     [  35.   680. ]
     [  35.   700. ]
     [  35.   725. ]
     [  35.   720. ]
     [  36.   714. ]
     [  36.   850. ]
     [  37.  1000. ]
     [  38.5  920. ]
     [  38.5  955. ]
     [  39.5  925. ]
     [  41.   975. ]
     [  41.   950. ]
     [   9.8    9.8]
     [  10.5   10.5]
     [  10.6   10.6]
     [  11.    11. ]
     [  11.2   11.2]
     [  11.3   11.3]
     [  11.8   11.8]
     [  11.8   11.8]
     [  12.    12. ]
     [  12.2   12.2]
     [  12.4   12.4]
     [  13.    13. ]
     [  14.3   14.3]
     [  15.    15. ]]



```python
print(kn._y)
```

    [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0
     0 0 0 0 0 0 0 0 0 0 0 0]



```python
# 실제로 훈련되는게 없음. fit() 매서드에 데이터를 모두 저장하고 있다가 예측 데이터가 들어오면 참고함.
# Default 가장 가까운 5개의 데이터를 참고해서 구분

# 참고 데이터 수를 변경하는 법
kn49 = KNeighborsClassifier(n_neighbors=49)
kn49.fit(fish_data, fish_target)
kn49.score(fish_data, fish_target)

# 5개를 참고할 때 성능이 더 좋음(5:1, 7:0.7143)
```




    0.7142857142857143


