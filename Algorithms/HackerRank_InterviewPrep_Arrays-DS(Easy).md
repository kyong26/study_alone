# HackerRank
## InterviewPrep
### Arrays-DS(Easy)

An *array* is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .

Reverse an array of integers.

**Note:** If you've already solved our C++ domain's *Arrays Introduction* challenge, you may want to skip this.

**Function Description**

Complete the function *reverseArray* in the editor below.

*reverseArray* has the following parameter(s):

- *int A[n]*: the array to reverse

**Returns**

- *int[n]*: the reversed array


```python
def reverseArray(a):
    # Write your code here
    return reversed(a)
```


```python
# test case 
a = '1432'

# 기대값: '2341'
# 값 확인을 위해 iterator를 list로 변환
print(list(reverseArray(a)))
```

    ['2', '3', '4', '1']
    
