# Inflearn
## 파이썬 알고리즘 문제풀이
### Dynamic Programming

# 1. Bottom-Up, Top-Down

현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다.
예를 들어 4m의 네트워크 선이 주어진다면,

1) [1,1,1,1]
2) [2,1,1]
3) [1,2,1]
4) [1,1,2]
5) [2,2]

의 5가지 방법을 생각할 수 있습니다.
그렇다면 네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?


```python
# Bottom Up: 반복문을 사용하는 방법 

def line_cutting_bottom_up_re(n):
    dy = [0]*(n+1)
    dy[1]=1
    dy[2]=2
    for i in range(3, n+1):
        dy[i] = dy[i-1]+dy[i-2]
    return dy[n]

line_cutting_bottom_up_re(4)
```




    5




```python
# Top Down: 재귀함수/메모이제이션을 사용하는 방법
# 넓은 의미에서 동적기획법이라고 부르나,
# Bottom-Up 방식이 좁은 의미에서의 동적기획법이다.

def DFS(n):
    dy = [0]*(n+1)
    if dy[n]>0:
        return dy[n]
    if n==1 or n==2:
        return n
    else:
        dy[n] = DFS(n-1) + DFS(n-2) #메모이제이션
        return dy[n]
    
DFS(4)
```




    5



## 응용문제: 알리바바와 40인의 도둑

알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다. 알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 합니다. 
계곡의 돌다리는 N x N 개의 돌들로 구성되어 있습니다. 각 돌다리들은 높이가 서로 다릅니다.
해당 돌다리를 건널 때, 돌의 높이 만큼 에너지가 소비됩니다.
N x N 의 계곡의 돌다리 격자정보가 주어지면, (1, 1) 격자에서 (N, N) 까지 가는데 드는 에너지의 최소량을 구하는 프로그램을 작성하세요.

만약 N =3 이고, 계곡의 돌다리 격자 정보가 다음과 같다면

| n=1 | n=2 | n=3 |
| --- | --- | --- |
| 3 | 3 | 5 |
| 2 | 3 | 4 |
| 6 | 5 | 2 |

(1, 1) 좌표에서 (3, 3) 좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2 = 14 입니다.


```python
# 풀이1: DP 사용 전

import itertools
n = 3 
arr = [[3,3,5],[2,3,4],[6,5,2]]


###################################

n = len(arr)
ways = ['D'] * (n-1) + ['R'] * (n-1)

aa = list(itertools.permutations(ways, len(ways)))
aa = list(set(aa)) #중복순열제거

dy = ['0'] * len(aa)

for i in range(len(aa)):
    power, x, y = 0, 0, 0
    for j in range(len(aa[0])):
        if aa[i][j] == 'D':
            x += 1
            power += arr[x][y]
        elif aa[i][j] == 'R':
            y += 1
            power += arr[x][y]
    dy[i] = power + arr[0][0] 

print(min(dy))
```

    14
    


```python
# 풀이2 : Bottom Up

def solutions(n, arr):
    dy = [[0]*n for _ in range(n)]
    dy[0][0] = arr[0][0]
    for i in range(1, n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i][j-1], dy[i-1][j]) + arr[i][j]
    print(dy[n-1][n-1])

n = 3 
arr = [[3,3,5],[2,3,4],[6,5,2]]

solutions(n, arr)
```

    14
    


```python
# 풀이3 : Top Down

dy = [[0]*n for _ in range(n)]

def DFS(x, y):
    if dy[x][y]>0: #cut 조건
        return dy[x][y]
    if x==0 and y==0:
        return arr[0][0]
    else:
        if y==0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x==0:
            dy[x][y] =  DFS(x, y-1) + arr[x][y] 
        else:
            dy[x][y] = min(DFS(x, y-1), DFS(x-1, y)) +arr[x][y] 
        return dy[x][y]

n = 3 
arr = [[3,3,5],[2,3,4],[6,5,2]]
DFS(n-1, n-1)
```




    14


