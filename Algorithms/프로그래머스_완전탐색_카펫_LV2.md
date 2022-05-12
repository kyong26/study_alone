# 프로그래머스_해시_카펫_LV2

### 문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.\
Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.\
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때\
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.


### 제한사항

갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.\
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.\
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.


### 입출력 예

brown	yellow	return\
10	2	[4, 3]\
8	1	[3, 3]\
24	24	[8, 6]


```python
def solution(brown, yellow):
    yellow_chk = set()

    for i in range(1, yellow+1):
        a, b =  divmod(yellow, i)
        if b==0 and a not in yellow_chk and a<brown and i<brown and (a+2)*(i+2)-yellow == brown :
            yellow_chk.add(a)
            yellow_chk.add(i)
            
    yellow_chk = list(yellow_chk)
    answer = [i+2 for i in yellow_chk]
    answer.sort(reverse=True)
    
    if len(answer)==1:
        answer = answer*2
        
    return answer
```

<img width="300" alt="image" src="https://user-images.githubusercontent.com/52664532/167489285-2c355e1d-008a-4a59-a0ff-a12478dc356a.png">

```python
brown, yellow = 10, 2
solution(brown, yellow) # 4, 3
```




    [4, 3]




```python
brown, yellow = 8, 1
solution(brown, yellow) # 3, 3
```




    [3, 3]




```python
brown, yellow = 24, 24
solution(brown, yellow) # 8, 6
```




    [8, 6]




```python
# 다른 사람 풀이

# 둘레 길이 이용
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
```


```python
# 근의 공식

import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
```
