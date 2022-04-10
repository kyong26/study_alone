# Leet Code
## 1. Two sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.


```python
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
```


```python
# test case 
nums = [2,7,11,15]
target = 9
# 기대값: [0,1]
twoSum(nums, target)
```




    [0, 1]



* 14:49Accepted3848 ms14.9 MBpython3

이 문제에 Dynamic Programming을 적용하면 연산 속도가 더 빨라진다.
아래는 DP를 적용한 샘플코드로,
실행 시간은 아래와 같다.

* 02/13/2022 14:42Accepted60 ms15.1 MBpython3


```python
def twoSum(nums, target):
    for i,x in enumerate(nums):
        if target - x in index:
            return [index[target-x],i]
        index[x] = i
```


```python
# test case 
nums = [2,7,11,15]
target = 9
# 기대값: [0,1]
twoSum(nums, target)
```




    [0, 1]


