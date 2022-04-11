# 파이썬알고리즘인터뷰_01.유효한팰린드롬 


### 빅오 
- 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기방법
- 점근적 실행 시간(Asymptotic Running Time)를 표기할 때 가장 널리 쓰이는 수학적 표기법
- 시간복잡도(Time Complexity)와 동일함
- 시간복잡도 "어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산복잡도"
- 계산복잡도를 표기하는 대표적인 방법이 빅오임

### 빅오 표기방법
- 최고차항을 표기하며 계수를 무시한다
  (예) 4n^3+2n+1만큼 계산하는 함수가 있다면, 여기서의 시간복잡도는 O(n^2)이 된다.

### 빅오 표기법의 종류
- O(1): 입력값이 아무리 커도 실행 시간이 일정한 최고의 알고리즘
- O(log n) : 실행 시간은 입력값에 영향을 받으나, 로그는 매운 큰 입력값에도 크게 영향을 받지 않는 편이다.
- O(n) : 입력값만큼 실행 시간에 영향을 받으며, 이러한 알고리즘을 선형 시간 알고리즘이라고 한다.
- O(n log n) : 병합정렬을 비롯한 대부분의 효율 좋은 정렬 알고리즘이 이에 해당한다. 
- O(n^2) : 버블정렬같은 비효율적인 정렬 알고리즘
- O(2^n) : 피보나치수를 재귀로 계산하는 알고리즘이 이에 해당한다.
- O(n!) : 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제(Traveling Salesman Problem)를 브루트 포스로 풀이할 때가 이에 해당한다. 가장 느린 알고리즘으로, 입력값이 조금만 커져도 웬만한 다항시간 내에는 계산이 어렵다.

### 상한과 최악
- 빅오는 상한(Upper Bound)을 의미한다. 이외에도 하한(Lower Bound)을 나타내는 빅오메가, 평균을 나타내는 빅세타가 있는데, 학계와 달리 업계에서는 빅세타와 빅오를 하나로 합쳐서 단순화해서 표현하려는 경향이 있다.

### 유효한 팰린드롬

Q. 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
* 팰린드롬: 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장이다.



```python
#풀이

import numpy as np

input = 'A man, a plan, a canal: Panama'
input = input.replace(',','').replace(':','').replace(' ','')
input = input.lower()

print(''.join(reversed(input)))
print(input)
print(input == ''.join(reversed(input)))
```

    amanaplanacanalpanama
    amanaplanacanalpanama
    True
    

## 모범답안

### 1. 리스트로 변환


```python
s = 'A man, a plan, a canal: Panama'

strs = [] 
for char in s :
    if char.isalnum():
        strs.append(char.lower())
while len(strs)>1:
    if strs.pop(0) != strs.pop():
        print(False)
```

### 2. 데크 자료형을 이용한 최적화

* 데크 : list처럼 요소들을 한 곳에 담아두는 배열이다. 보통 큐 Queue가 FIFO이나, 데크는 양방향 que이며, O(n)의 속도인 list보다 빠르다(O(1)).

deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.\
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.\
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.\
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.\
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.\
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.\
deque.remove(item): item을 데크에서 찾아 삭제한다.\
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).\


```python
s = 'A man, a plan, a canal: Panama'

import collections
from typing import Deque

strs: Deque = collections.deque() 
#자료형을 데크로 선선하는 것만으로 5배 가까이 연산 속도를 단축시켰다.

strs = [] 
for char in s :
    if char.isalnum():
        strs.append(char.lower())
while len(strs)>1:
    if strs.pop(0) != strs.pop():
        print(False)   
```

### 3. 슬라이싱 사용


```python
s = 'A man, a plan, a canal: Panama'

import re
s = s.lower()

#정규식으로 불필요한 문자 필터링
s = re.sub('[^a-z0-9]', '', s)
print( s==s[::-1])
```

    True
    
