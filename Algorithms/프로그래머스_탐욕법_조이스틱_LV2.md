# 프로그래머스_탐욕법_조이스틱_LV2

## 문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.\
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA\

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳\
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)\
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)\
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)\
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.

따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.\
만들고자 하는 이름 name이 매개변수로 주어질 때,\
이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

## 제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
### 입출력 예
name	return\
"JEROEN"	56\
"JAN"	23


```python
name = "JEROEN"

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_dict = {}

for key, value in enumerate(alphabet):
    alpha_dict[value] = key
    
answer = 0

for i in name:
    answer += min(alpha_dict[i], 26-alpha_dict[i])
answer += (len(name)-1)
    
answer
```




    56




```python
name = "JAZ"

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_dict = {}

for key, value in enumerate(alphabet):
    alpha_dict[value] = key
    
answer = 0

for i in name:
    answer += min(alpha_dict[i], 26-alpha_dict[i])
    print(i, answer)
answer += (len(name)-1)
    
answer
```

    J 9
    A 9
    Z 10
    




    12




```python

```


```python
#풀이2
def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer
```


```python

```
