# HackerRank
## InterviewPrep
### Sales by Match(Easy)

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

**Example** 

There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

**Function Description**

Complete the *sockMerchant* function in the editor below.

sockMerchant has the following parameter(s):

- *int n:* the number of socks in the pile
- *int ar[n]:* the colors of each sock

**Returns**

- *int:* the number of pairs

**Input Format**

The first line contains an integer , the number of socks represented in . The second line contains  space-separated integers, , the colors of the socks in the pile.


```python
def sockMerchant(n, ar):
    # Write your code here
    result=0
    color = list(set(ar))
    for i in range(len(color)):
        chk = [j for j in ar if j==color[i] ]
        #몫을 구해서 양말 쌍을 구함
        result += len(chk)//2
    #결과값은 정수의 형태로 출력
    result=int(result)
    return result
```


```python
# test case 
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# 기대값: 3
sockMerchant(n, ar)
```




    3


