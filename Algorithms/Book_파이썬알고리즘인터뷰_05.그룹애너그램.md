### 문자열 배열을 받아 애너그램 단위로 그룹핑하라


```python
words = ['eat','tea','tan','ate','nat','bat']
```


```python
answer_set = []

for i in range(len(words)):
    if sorted(words[i]) not in answer_set:
        answer_set.append((sorted(words[i])))
        
solutions = [[] for i in range(len(answer_set))]

while len(words)>0:
    for i in range(len(answer_set)):
        if sorted(words[0]) == answer_set[i]:
            solutions[i].append(words.pop(0))

print(solutions)
```

    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    

## 모범답안

###  정렬하여 딕셔너리에 추가


```python
# sorted는 문자열도 잘 정렬한다

strs = ['eat','tea','tan','ate','nat','bat']

import collections
from typing import List

anagrams = collections.defaultdict(list) 
#존재하지 않는 키를 삽입하려 할 
경우 Key error가 발생하므로, defaultdict()를 선언한다

for word in strs:
    anagrams[''.join(sorted(word))].append(word) 
    # 정렬하여 딕셔너리에 추가
    
print(anagrams)
print(list(anagrams.values()))
```

    defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    

### 여러가지 정렬방법


```python
a = [2,5,1,9,7]
print(sorted(a))

b = 'zbdaf'
print(sorted(b))

print("".join(sorted(b)))

a.append(0)
print(a.sort()) #sort함수는 None을 리턴하므로 주의 필요
a.sort()
print(a)

c = ['ccc','aaaa','d','bb']
print(sorted(c, key=len))
```

    [1, 2, 5, 7, 9]
    ['a', 'b', 'd', 'f', 'z']
    abdfz
    None
    [0, 1, 2, 5, 7, 9]
    ['d', 'bb', 'ccc', 'aaaa']
    


```python
a = ['cde','cfc','abc']

def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn)) 
# 첫 문자열과 마지막 문자열 순으로 정렬함

print(sorted(a, key=lambda s:(s[0], s[-1]))) 
```

    ['abc', 'cfc', 'cde']
    ['abc', 'cfc', 'cde']
    

### (참고) 정렬 알고리즘

1. 퀵정렬
대부분 가장 빠른 정렬이지만, 데이터에 따라 편차가 큼\
최악의 경우 O(n^2)이 될 수 있다

2. 병합정렬
일정하게 안정적인 성능을 보이며, 가장 인기있는 정렬 알고리즘\
항상 일정한 속도를 보이지만, O(nlogn) 이상 빠르게 처리할 수 없다

3. 팀소트(파이썬)
데이터는 이미 정렬되어 있을 것이라고 가정, 실제 데이터에서 고성능을 낼 수 있도록 설계한 알고리즘\
이미 정렬되어 있는 경우 비교를 건너 뛰기 때문에 O(n)까지 가능하다



```python

```
