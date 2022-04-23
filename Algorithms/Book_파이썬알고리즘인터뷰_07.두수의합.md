### 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라


```python
nums = [2,7,11,15]
target = 9
```


```python
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
```

    0 1
    

## 모범답안

###  풀이1) 브루트 포스로 계산

위에서 내가 풀이한 방법이 브루트 포스다.\
브루트 포스(Brute-Force)란 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식이다.\
이 경우 시간 복잡도는 O(n^2)이다.


```python
def twoSum(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
twoSum(nums)
```




    [0, 1]



###  풀이2) in을 이용한 탐색

모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target-n이 존재하는지 탐색하는 방법\
in의 시간복잡도는 O(n)이고, 따라서 전체 시간 복잡도는 이전과 동일한 O(n^2)이나,\
같은 시간복잡도라도 in 연산이 훨씬 더 빠르고 가볍다.


```python
def twoSum(nums):
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
        
twoSum(nums)
```




    [0, 1]



###  풀이3) 첫 번째 수를 뺀 결과 키 조회

딕셔너리는 해시테이블로 구현되어 있고, 이 경우 조회는 평균적으로 O(1)에 가능하다.\
최악의 경우에는 O(n)이 될 수 있지만 드문 경우로, 전체적으로는 O(n)이 된다.


```python
from typing import List

def twoSum(nums):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
        
twoSum(nums)
```




    [0, 1]



###  풀이4) 조회구조 개선

두 개 for 문을 1개의 for문으로 개선\
길이는 간결해지나, 실행속도는 풀이1과 비슷하다


```python
def twoSum(nums):
    nums_map = {}
    # 하나의 `for`문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
twoSum(nums)
```




    [0, 1]



###  풀이5) 투포인터 이용

왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면, 오른쪽 포인터를 왼쪽으로,\
작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식

시간복잡도 O(n), 불필요한 추가계산도 없어 빠른 속도가 기대된다.

다만 제대로 풀이하려면 정렬이 필요하고, 이렇게 되면 인덱스는 엉망이 되기 때문에 문제가 된다.

...라고 되어있는데, enumerate로 index랑 값을 출력하는 list를 하나 더 만든 다음에\
값을 key로 잡아 sort 하고 출력을 index로 하게 하면 가능은 해 보인다.\
다만 코드가 길어질 것.


```python
def twoSum(nums):
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
twoSum(nums)
```




    [0, 1]


