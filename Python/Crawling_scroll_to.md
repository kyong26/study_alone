

```python
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import re
from selenium import webdriver
import requests
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import datetime
import sys
```


```python
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
driver = webdriver.Chrome(ChromeDriverManager().install())
```



```python
con_url = 'https://toss.im/every-moment'
driver.get(con_url) 
elements = driver.page_source 
bsObj = BeautifulSoup(elements, "html.parser")
info = bsObj.find("ul", {"class": "css-t3cgn5 e1qeiidd0"})

toss_title = info.find_all("p", {"class":"css-1ry4dch er9u5643"})
toss_contents = info.find_all("p", {"class":"css-pjo6h5 er9u5642"})

output_title = []
output_contents = [] 

for j in range(len(toss_title)):
    output_title.append(toss_title[j].get_text())
for j in range(len(toss_contents)):
    output_contents.append(toss_contents[j].get_text())

df1 = pd.DataFrame(output_title, columns={'title'})
df2 = pd.DataFrame(output_contents, columns={'contents'})
df1 = df1.join(df2)
```

데이터가 랜덤으로 뜨고, 스크롤다운 해야 업데이트가 되므로,\
스크롤다운하는 코드를 반복문을 통해 여러번 실행해서 데이터를 수집한다.

```python
for i in range(5):
    con_url = 'https://toss.im/every-moment'
    
    driver.get(con_url)
    sleep(2)
    driver.execute_script("window.scrollTo(0, 30000);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 80000);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 100000);")
    sleep(3)
    driver.execute_script("window.scrollTo(0, 120000);")
    
    elements = driver.page_source 
    bsObj = BeautifulSoup(elements, "html.parser")
    info = bsObj.find("ul", {"class": "css-t3cgn5 e1qeiidd0"})

    toss_title = info.find_all("p", {"class":"css-1ry4dch er9u5643"})
    toss_contents = info.find_all("p", {"class":"css-pjo6h5 er9u5642"})

    output_title = []
    output_contents = [] 

    for j in range(len(toss_title)):
        output_title.append(toss_title[j].get_text())
    for j in range(len(toss_contents)):
        output_contents.append(toss_contents[j].get_text())

    df3 = pd.DataFrame(output_title, columns={'title'})
    df4 = pd.DataFrame(output_contents, columns={'contents'})
    df3 = df1.join(df4)

    df1 = pd.concat([df1, df3])
    df1 = df1.drop_duplicates()
    print(df1.count())

    sleep(2)
```

<br>
<br>

