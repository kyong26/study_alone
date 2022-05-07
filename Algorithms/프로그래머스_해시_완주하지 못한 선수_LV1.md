# 프로그래머스_해시_완주하지 못한 선수_LV1

### 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다.\
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.\
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,\
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

### 제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.\
completion의 길이는 participant의 길이보다 1 작습니다.\
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.\
참가자 중에는 동명이인이 있을 수 있습니다.



```python
# 정확성(50/50), 효율성(0/50)
del solution(participant, completion):
    for i in range(len(participant)):
        if participant[i] in completion:
            completion.remove(participant[i]) #remove 시간복잡도 O(n)
        else:
            answer = participant[i]
            break
```


```python
# 정확성(50/50), 효율성(40/50)
def solution(participant, completion):
    answer = list(set(participant)-set(completion))
    if answer != []:
        return answer[0]
    else:
        a = participant + completion
        b = set(a)
        for i in b:
            if a.count(i)%2 == 1: #count 시간복잡도 O(n)
                answer = i
                break
        return answer
```


```python
# 정확성(50/50), 효율성(50/50)
def solution(participant, completion):
    from collections import Counter
    answer = Counter(participant)-Counter(completion)
    return list(answer)[0]

'''정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.40ms, 10.1MB)
테스트 4 〉	통과 (0.67ms, 10.4MB)
테스트 5 〉	통과 (0.70ms, 10.5MB)

효율성  테스트
테스트 1 〉	통과 (28.27ms, 24.3MB)
테스트 2 〉	통과 (41.29ms, 27.7MB)
테스트 3 〉	통과 (56.99ms, 30.1MB)
테스트 4 〉	통과 (64.83ms, 38.9MB)
테스트 5 〉	통과 (74.27ms, 38.9MB)'''
```


```python
# 정확성(50/50), 효율성(50/50)
# Counter만 썼을때보다 속도가 조금 더 빠르다

def solution(participant, completion):
    from collections import Counter
    answer = list(set(participant)-set(completion))
    if answer != []:
        return answer[0]
    answer = Counter(participant)-Counter(completion)
    return list(answer)[0]

'''정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.12ms, 10.4MB)
테스트 4 〉	통과 (0.19ms, 10.3MB)
테스트 5 〉	통과 (0.59ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (12.53ms, 21.7MB)
테스트 2 〉	통과 (18.90ms, 25MB)
테스트 3 〉	통과 (30.93ms, 33.4MB)
테스트 4 〉	통과 (28.16ms, 34.5MB)
테스트 5 〉	통과 (80.94ms, 38.9MB)'''
```


```python
# 참고: 좋아요 많이 받은 풀이, 내 풀이와 비슷하다
def solution(participant, completion):

    import collections

    def solution(participant, completion):
        answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]
```
