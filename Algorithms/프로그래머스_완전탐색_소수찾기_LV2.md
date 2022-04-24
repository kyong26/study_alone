## 프로그래머스
### 완전탐색_소수찾기_LV2

#### 문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다.\
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,\
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

#### 제한 조건

numbers는 길이 1 이상 7 이하인 문자열입니다.\
numbers는 0~9까지 숫자만으로 이루어져 있습니다.\
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.\

---

#### 입출력 예

|answers|return|
|---|--|
"17"|3
"011"|2

---


```python
import itertools
numbers = "17"
```


```python
answer = []
prime_numbers = [] 
num_set = [] 

for i in range(len(numbers)):
    prime_numbers += list(itertools.permutations(numbers, i+1))
for i in range(len(prime_numbers)):
    num = int(''.join(prime_numbers[i]))
    if num not in num_set and num>1:
        num_set.append(num)
```




    [7, 17, 71]




```python
for i in range(len(num_set)):
    if num_set[i]==2:
        answer.append(2)
    else:
#         print("num:", num_set[i])
        div_set = [] 
        for j in range(3, num_set[i], 2):
            div_set.append(j)
        cnt = 0 
        for j in range(len(div_set)):
#             print('div:',div_set[j])
            if num_set[i] % div_set[j] == 0 :
                break
            else:
                cnt+=1
#                 print('cnt:',cnt)
        if cnt==len(div_set):
            answer.append(num_set[i])
            
print(len(answer))
```

    3
    


```python

```


```python

```
