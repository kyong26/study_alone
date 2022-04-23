### 가장 긴 팰린드롬 부분 문자열을 출력하라


```python
a = 'babad'
b = 'cbbd'
```


```python
def solutions(a):
    answer = ''
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            if a[i:j] == a[i:j][::-1] and len(answer)<len(a[i:j]):
                answer = a[i:j]
    return answer
```


```python
solutions(a)
```




    'bab'




```python
solutions(b)
```




    'bb'



## 모범답안

###  중앙을 중심으로 확장하는 풀이


(참고)
컴퓨터과학의 오랜 문제 중에 "최장 공통 부분 문자열(Longest Common Substring)"이라는 문제가 있다.\
여러 개의 입력 문자열이 있을 때 서로 공통된 가장 긴 부분 문자열을 찾는 문제로\
다이나믹 프로그래밍으로 풀 수 있는 전형적인 문제다.



```python
a = 'babad'
b = 'cbbd'

def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        print(s)

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    print(result)
    
solution(a)
solution(b)
```

    bab
    bb
    
