## 문제 설명
수포자는 수학을 포기한 사람의 준말입니다.\
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.\ 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...\
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...\
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,\ 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.\
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.\
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예\
answers	return\
[1,2,3,4,5]	[1]\
[1,3,2,4,2]	[1,2,3]


```python
def solution(answers):
    answer = []
    seq = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    scores = [] 

    for i in range(3):
        submit_answers = []

        if len(seq[i])>len(answers):
            submit_answers = seq[i][:len(answers)]
        else:
            a, b = divmod(len(answers), len(seq[i]))
            if b==0:
                submit_answers = seq[i] * a 
            else:
                submit_answers = seq[i] * a + seq[i][:b]

        score = 0 
        for j in range(len(submit_answers)):
            if submit_answers[j] == answers[j]:
                score +=1
        scores.append(score)

    for i, j in enumerate(scores):
        if j == max(scores):
            answer.append(i+1)
    return answer
```

### 참고할 만한 풀이


```python
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
```


```python
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
```
