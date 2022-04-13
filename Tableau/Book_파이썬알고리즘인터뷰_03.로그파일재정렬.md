### 로그를 재정렬하라. 기준은 다음과 같다.

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.


```python
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```


```python
answers, numbers = [], []

for log in logs:
    if log[5].isalpha():
        answers.append(log[4:]+log[:4])
    else:
        numbers.append(log)
answers.sort()

for i in range(len(answers)):
    answers[i] = answers[i][-4:]+answers[i][:-4]

answers = answers+numbers
print(answers)
```

    ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
    

## 모범답안
### 람다와 + 연산자를 이용


```python
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```


```python
letters, digits = [], []

for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)
     
#식별자를 제외한 문자열 [1:]을 키로 정렬하며, 후순위로 식별자 [0]을 지정해 정렬   
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

print(letters + digits)
```

    ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
    
