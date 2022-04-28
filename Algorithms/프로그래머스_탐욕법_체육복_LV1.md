# 프로그래머스_탐욕법_체육복_LV1

## 문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.\
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.\
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.\
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.\
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,\
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,\
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.\
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.\
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.\
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.\
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.\
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,\
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.


### 입출력 예
n	lost	reserve	return\
5	[2, 4]	[1, 3, 5]	5\
5	[2, 4]	[3]	4\
3	[3]	[1]	2


```python
n= 9
lost = [5,6,8,1,2]
reserve = [2,3,1,4,8,9] 

def solution(n, lost, reserve):
    answer = 0
    
    #여벌 체육복이 있는 학생이 도난당한 경우
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
    #체육복이 있는 사람
    answer += (n-len(lost))
            
    #체육복 빌리기  
    lost.sort()
    reserve.sort()
    
    for a in lost: 
        #1번일때: 2번에게만 빌릴 수 있음
        if a==1 and a+1 in reserve:
            reserve.remove(a+1)
            answer += 1 
        #마지막 번호일때: 바로 앞 번호에게만 빌릴 수 있음
        elif a==n and a-1 in reserve:
            reserve.remove(a-1)
            answer += 1  
        #그 외: -1, +! 모두에게 빌릴 수 있음
        #뒷번호를 위해, 최대한 앞 사람에게 빌림
        elif a-1 in reserve:
            reserve.remove(a-1)
            answer += 1 
        elif a+1 in reserve:
            reserve.remove(a+1)
            answer += 1  
            
    return answer

solution(n, lost, reserve)
```

    8

![image](https://user-images.githubusercontent.com/52664532/165772952-4d6d056e-be3c-439f-be49-7c0b1dbda99e.png)


```python
#참고

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
```

```python
#속도가 가장 빠른 사람의 
def solution(n, lost, reserve):

    reserve = set(reserve)    # reserve 를 집합으로 바꾼다.

    for size in [0, 1, -2]:   
        lost = set(map(lambda x : x+size, lost))
        reserve, lost = reserve - lost, lost - reserve                         
	# for문 첫 번째는 lost = reserve를 제거, 
 	# 두 번째는 lost + 1 = reserve를 제거,
 	# 세 번째는 lost - 1 = reserve를 제거하는 구문
    return n - len(lost)
```
