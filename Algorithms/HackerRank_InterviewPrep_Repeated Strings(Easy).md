# HackerRank
## InterviewPrep
### Jumping on the Clouds(Easy)

There is a string, of lowercase English letters that is repeated infinitely many times. Given an integer, find and print the number of letter `a`'s in the first letters of the infinite string.

**Example** 

The substring we consider is , the first  characters of the infinite string. There are  occurrences of `a` in the substring.

**Function Description**

Complete the *repeatedString* function in the editor below.

repeatedString has the following parameter(s):

- *s:* a string to repeat
- *n:* the number of characters to consider

**Returns**

- *int:* the frequency of `a` in the substring

**Input Format**

The first line contains a single string, . The second line contains an integer, .


```python
def repeatedString(s, n):
    # Write your code here
    x = n//len(s) 
    y = n%len(s)  
    return s.count('a') * x + s[0:y].count('a')
```


```python
# test case 
s = 'aba'
n = 10 

# 기대값: 7
repeatedString(s, n)
```




    7


