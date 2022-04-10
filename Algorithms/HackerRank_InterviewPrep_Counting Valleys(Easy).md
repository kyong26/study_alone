# HackerRank
## InterviewPrep
### Counting Valleys(Easy)

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an *uphill*, , or a *downhill*,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

- A *mountain* is a sequence of consecutive steps *above* sea level, starting with a step *up* from sea level and ending with a step *down* to sea level.
- A *valley* is a sequence of consecutive steps *below* sea level, starting with a step *down* from sea level and ending with a step *up* to sea level.

Given the sequence of *up* and *down* steps during a hike, find and print the number of *valleys* walked through.

**Example**

The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.

**Function Description**

Complete the *countingValleys* function in the editor below.

countingValleys has the following parameter(s):

- *int steps*: the number of steps on the hike
- *string path*: a string describing the path

**Returns**

- *int:* the number of valleys traversed

**Input Format**

The first line contains an integer , the number of steps in the hike. The second line contains a single string , of  characters that describe the path.


```python
def countingValleys(steps, path):
    location = 0
    valley_chk=[]
    for i in range(steps):
        if path[i]=="D":
            if location== 0:#현재 위치가 0이고 -1 예정일때 valley-in
                valley_chk.append('S')
            location -= 1
        elif path[i] == "U":
            if location== -1: #현재 위치가 -1이고 0 예정일때 valley-out
                valley_chk.append('E')
            location += 1
    return min(valley_chk.count('S'), valley_chk.count('E'))
```


```python
# test case 
steps = 8
path = 'UDDDUDUU'
# 기대값: 1
countingValleys(steps, path)
```




    1


