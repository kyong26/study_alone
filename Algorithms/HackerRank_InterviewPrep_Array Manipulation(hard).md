# HackerRank
## InterviewPrep
### Array Manipulation(hard)

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

**Example** 

Queries are interpreted as follows:

    `a b k
    1 5 3
    4 8 7
    6 9 1`

Add the values of  between the indices  and  inclusive:

`index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]`

The largest value is  after all operations are performed.

**Function Description**

Complete the function *arrayManipulation* in the editor below.

arrayManipulation has the following parameters:

- *int n* - the number of elements in the array
- *int queries[q][3]* - a two dimensional array of queries where each *queries[i]*contains three integers, *a*, *b*, and *k*.

**Returns**

- *int* - the maximum value in the resultant array

**Input Format**

The first line contains two space-separated integers  and , the size of the array and the number of operations. Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.


```python
def arrayManipulation(n, queries):
    # Write your code here
    answer = [0 for i in range(n)]
    for i in range(len(queries)):
        for j in range(n):
            if j>= queries[i][0]-1 and j<=queries[i][1]-1:
                answer[j] += queries[i][2]
    return max(answer)
```


```python
# test case 
n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]

# 기대값: 10
arrayManipulation(n, queries)
```




    10



첫 테스트 케이스는 패스했으나,
복잡한 테스트 케이스의 경우 time-out이 발생했다.
시간복잡도 때문인 것 같은데, 
책을 통해 연산속도가 빠른 코드에 대해 추가로 공부하게 되었다.
(파이썬 알고리즘 인터뷰 - 박상길)


```python
def arrayManipulation(n, queries):
    # Write your code here
    answer = [0 for i in range(n+1)]
    for query in queries:
        a = query[0]-1
        b = query[1]
        c = query[2]
        answer[a] += c
        answer[b] -= c 
    
    max_answer = 0
    d = 0
    for i in answer:
        d += i 
        if d>max_answer:
            max_answer = d 
    return max_answer
```


```python
# test case 
n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]

# 기대값: 10
arrayManipulation(n, queries)
```




    10


