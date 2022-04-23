### 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라


```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```


```python

```


```python

```

## 모범답안

###  풀이1) 투 포인터를 최대로 이동

이 문제는 높이와 너비 모든 공간을 차례대로 모두 살펴보면 O(n^2)에 풀이가 가능하다.\
그러나 시간 복잡도가 너무 높기 때문에 좀 더 효율적인 풀이를 찾아야 한다.\
투 포인터나 스택으로 O(n) 풀이가 가능하다.


```python
from typing import List

def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
        return volume
```


```python
trap(height)
```




    0




```python
# 왜 출력값이 0이 나오지?
```

###  풀이2) 스택 쌓기

스택에 쌓아 나가면서 현재 높이가 이전 높이보다 높을 때,\
즉 꺾이는 부분 변곡점을 기준으로 격차만큼 물 높이를 치운다.


```python
from typing import List


def trap(height):
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume
```


```python
trap(height)
```




    6




```python

```
