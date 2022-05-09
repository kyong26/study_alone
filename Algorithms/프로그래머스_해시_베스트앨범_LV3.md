# 프로그래머스_해시_베스트앨범_LV3

### 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.\
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.\
속한 노래가 많이 재생된 장르를 먼저 수록합니다.\
장르 내에서 많이 재생된 노래를 먼저 수록합니다.\
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.\
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,\
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한사항

genres[i]는 고유번호가 i인 노래의 장르입니다.\
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.\
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.\
장르 종류는 100개 미만입니다.\
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.\
모든 장르는 재생된 횟수가 다릅니다.


### 입출력 예

genres	plays	return\
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]


```python
def solution(genres, plays):
    
    g = {}
    answer = []

    for i in range(len(genres)):
        if genres[i] in g:
            g[genres[i]] += plays[i]
        else:
            g[genres[i]] = plays[i]

    g = sorted(g.items(), key=lambda x : -x[1])
    
    for i in range(len(g)):
        comp = []
        for key, value in enumerate(genres):
            if value == g[i][0] :
                comp.append([plays[key], key])
        comp.sort(key=lambda x : (-x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능)
        
        if len(comp)>=2:
            answer.append(comp[0][1])
            answer.append(comp[1][1])
        else:
            answer.append(comp[0][1])
    
    return answer
```


```python
genres = ["classic", "classic", "classic", "pop", "pop", "pop"]
plays = [100, 100, 100, 600, 600, 700]

solution(genres, plays)
```




    [5, 3, 0, 1]




```python
genres = ["classic", "pop", "classic", "classic", "classic"]
plays = [500, 1000, 400, 300, 200, 100]

solution(genres, plays)
```




    [0, 2, 1]




```python
# 다른 사람 풀이
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
```


```python
# defaultdict
from collections import defaultdict

def countLetters(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter


# defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 
# 모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해 줍니다.
    
def countLetters(word):
    counter = defaultdict(lambda: 0)
    for letter in word:
        counter[letter] += 1
    return counter
```
