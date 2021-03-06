# 프로그래머스_해시_전화번호 목록_LV2

### 문제 설명

스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.\
예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면\
다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.\

종류	이름\
얼굴	동그란 안경, 검정 선글라스\
상의	파란색 티셔츠\
하의	청바지\
겉옷	긴 코트\
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.\
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.\
같은 이름을 가진 의상은 존재하지 않습니다.\
clothes의 모든 원소는 문자열로 이루어져 있습니다.\
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.\
스파이는 하루에 최소 한 개의 의상은 입습니다.


```python
# 예시
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
```


```python
# 정확성 (27/28): 테스트 1번 time-out
# 테스트 26: 665ms

def solution(clothes):
    from itertools import combinations
    from collections import Counter

    a = []
    answer = 0

    for i, j in clothes:
        a.append(j)
    b = Counter(a)
    a = set(a)

    for i in range(1, len(a)+1):
        if i==1:
            answer += len(clothes)
        else:
            comb = list(combinations(a, i))
            for j in range(len(comb)):
                numb = 1 
                for k in range(i):
                    numb = numb*b[comb[j][k]]
                answer += numb
                    
    return answer

# 기대값 5
solution(clothes)
```




    5




```python
# 정확성 (27/28): 테스트 1번 time-out
# 테스트 26: 652ms
def solution(clothes):
    from itertools import combinations
    from collections import Counter

    a = []
    answer = 0

    for i, j in clothes:
        a.append(j)
    b = Counter(a)
    a = set(a)

    for i in range(1, len(a)+1):
        if i==1:
            answer += len(clothes) 
        else:
            comb = list(combinations(a, i))
            if len(a)==len(clothes):
                answer += len(comb)
            else:
                for j in range(len(comb)):
                    numb = 1 
                    for k in range(i):
                        numb = numb*b[comb[j][k]]
                    answer += numb                 
    return answer
```


```python
# 정확성 (28/28)

def solution(clothes):
    from itertools import combinations
    from collections import Counter
    import math

    a = []
    answer = 0

    for i, j in clothes:
        a.append(j)
    b = Counter(a)
    a = set(a)

    for i in range(1, len(a)+1):
        if i==1:
            answer += len(clothes)
        elif b.most_common(1)[0][1]==1:
            answer+= math.factorial(len(a))/math.factorial(len(a)-i)/math.factorial(i)
        else:
            comb = list(combinations(a, i))
            for j in range(len(comb)):
                numb = 1 
                for k in range(i):
                    numb = numb*b[comb[j][k]]
                answer += numb
                    
    return answer
```

<img width="300" alt="image" src="https://user-images.githubusercontent.com/52664532/167317043-b4233816-ae1d-4291-af1a-41897ae25e0c.png">



```python
# 다른 사람 풀이 참고 1
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
```

```python
# 다른 사람 풀이 참고 2
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
```


```python

# reduce 사용예제

from functools import reduce

result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(result) #15

result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 100)
print(result) #115

```
