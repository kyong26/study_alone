### 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 
소문자 구분은 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다


```python
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
```


```python
import re

paragraph = paragraph.lower().replace(banned[0], " ")
paragraph = re.sub('[^a-z]',' ', paragraph)
paragraph = paragraph.split()

max(paragraph, key=paragraph.count)
```




    'ball'



## 모범답안

###  리스트 컴프리헨션, Counter 객체 사용


```python
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
```


```python
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

import collections
import re
from typing import List

words = [word for word in re.sub(r'[^\w]', ' ', paragraph) # \w 모든 단어문자
            .lower().split()
                 if word not in banned]
counts = collections.Counter(words)

#most_common(1)하면 가장 흔하게 등장하는 단어를 선택한다
#('ball':2)가 된다
#[0]: 리스트 내 튜플 선택, [0]: 튜플 내 단어 'ball' 선택
counts.most_common(1)[0][0]
```




    ('ball', 2)


