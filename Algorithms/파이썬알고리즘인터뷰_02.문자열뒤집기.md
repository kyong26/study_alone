### 문자열 뒤집기
Q. 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라


```python
Q1 = ["h","e","l","l","o"]
Q2 = ["H","a","n","n","a","h"]
```


```python
# 풀이
print(Q1[::-1])
print(Q2[::-1])
```

    ['o', 'l', 'l', 'e', 'h']
    ['h', 'a', 'n', 'n', 'a', 'H']
    

## 모범답안
### 1. 투 포인터를 이용한 스왑


```python
def solution(s):
    left, right = 0, len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1 
        right -= 1
    print(s)
        
solution(Q1)
solution(Q2)
```

    ['o', 'l', 'l', 'e', 'h']
    ['h', 'a', 'n', 'n', 'a', 'H']
    

### 2. 파이썬다운 방식


```python
#reverse를 활용
Q1.reverse()
print(Q1)
Q2.reverse()
print(Q2)

#슬라이싱을 활용
Q1= Q1[::-1]
print(Q1)
Q2 = Q2[::-1]
print(Q2)

#리트코드의 경우 공간복잡도를 O(1)로 제한해서, 변수 할당을 처리하는데 제약이 있음
#그런 경우 아래와 같이 우회 가능
Q1[:] = Q1[::-1]
print(Q1)
Q2[:] = Q2[::-1]
print(Q2)
```

    ['h', 'e', 'l', 'l', 'o']
    ['h', 'a', 'n', 'n', 'a', 'H']
    ['o', 'l', 'l', 'e', 'h']
    ['H', 'a', 'n', 'n', 'a', 'h']
    ['h', 'e', 'l', 'l', 'o']
    ['h', 'a', 'n', 'n', 'a', 'H']
    
