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

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 100.0.4896
    Get LATEST chromedriver version for 100.0.4896 google-chrome
    Trying to download new driver from https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_win32.zip
    Driver has been saved in cache [C:\Users\xnsk2\.wdm\drivers\chromedriver\win32\100.0.4896.60]
    C:\Users\xnsk2\Anaconda3\envs\shomy\lib\site-packages\ipykernel_launcher.py:5: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
      """
    


```python
con_url = 'https://toss.im/every-moment'
driver.get(con_url) 
```


```python
elements = driver.page_source 
bsObj = BeautifulSoup(elements, "html.parser")
```


```python
info = bsObj.find("ul", {"class": "css-t3cgn5 e1qeiidd0"})
```


```python
toss_title = info.find_all("p", {"class":"css-1ry4dch er9u5643"})
toss_contents = info.find_all("p", {"class":"css-pjo6h5 er9u5642"})

output_title = []
output_contents = [] 

for j in range(len(toss_title)):
    output_title.append(toss_title[j].get_text())
for j in range(len(toss_contents)):
    output_contents.append(toss_contents[j].get_text())
```


```python
df1 = pd.DataFrame(output_title, columns={'title'})
df2 = pd.DataFrame(output_contents, columns={'contents'})
df1 = df1.join(df2)

df1['num'] = df1['title'].str.replace("불편함","")
df1['num'] = df1['num'].str.replace(",","")
df1['num'] = df1['num'].str.replace("번째","")
df1['num'] = df1['num'].astype(int)
```


```python
df_1st_try = df1.copy()
```


```python
df_1st_try.count()
```




    title       1157
    contents    1157
    num         1157
    dtype: int64




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

    df1 = pd.DataFrame(output_title, columns={'title'})
    df2 = pd.DataFrame(output_contents, columns={'contents'})
    df1 = df1.join(df2)
    df1['num'] = df1['title'].str.replace("불편함","")
    df1['num'] = df1['num'].str.replace(",","")
    df1['num'] = df1['num'].str.replace("번째","")
    df1['num'] = df1['num'].astype(int)

    df_2nd_try = df1.copy()

    df = pd.concat([df_2nd_try, df])
    df = df.drop_duplicates()
    print(df.count())

    sleep(2)
```


```python
df = df.sort_values(by='num')
df.to_excel('/Users/xnsk2/Anaconda3/envs/shomy/toss.xlsx')
```


```python
df = pd.read_excel('/Users/xnsk2/Anaconda3/envs/shomy/toss.xlsx')
```


```python

```


```python
del df['Unnamed: 3']
```


```python
df = df[['num','contents']]
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num</th>
      <th>contents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>넷플릭스 돈을 같이 모으고 싶어용</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>자동이체날짜를 알고 싶어요</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1.부동산 투자시 상환횟수가 표시되면 좋겠어요 언제쯤 상환예정인지 알수있도록요. 2...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>가계부 수입에 비해 지출초과분을 미리 알려줘서 과소비방지를 해줬으면 좋겠습니다.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>가계부 추출 기능! 통신사별 멤버십 혜택이 가능한 장소, 정보, 접근성 향상에 관련...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

# 한국어 Text 전처리

https://wikidocs.net/92961


### 1. PyKoSpacing

전희원님이 개발한 PyKoSpacing은 띄어쓰기가 되어있지 않은 문장을 띄어쓰기를 한 문장으로 변환해주는 패키지입니다.\
PyKoSpacing은 대용량 코퍼스를 학습하여 만들어진 띄어쓰기 딥 러닝 모델로 준수한 성능을 가지고 있습니다.

!pip install git+https://github.com/haven-jeon/PyKoSpacing.git


```python
df = pd.read_excel('/Users/xnsk2/Anaconda3/envs/shomy/toss.xlsx')
df = df[['num','contents']]
```


```python
df_poko = df.copy()
df_poko['contents_poko'] = df_poko['contents'].str.replace(" ", "")
```


```python
from pykospacing import Spacing
```


```python
spacing = Spacing()
df_poko['contents_poko_after'] = list(map(spacing, df_poko['contents_poko']))
```


```python
df_poko[df_poko.contents != df_poko.contents_poko_after][['contents','contents_poko_after']].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contents</th>
      <th>contents_poko_after</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>넷플릭스 돈을 같이 모으고 싶어용</td>
      <td>넷플릭스 돈을 같이 모으고 싶어 용</td>
    </tr>
    <tr>
      <th>1</th>
      <td>자동이체날짜를 알고 싶어요</td>
      <td>자동이체 날짜를 알고 싶어요</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.부동산 투자시 상환횟수가 표시되면 좋겠어요 언제쯤 상환예정인지 알수있도록요. 2...</td>
      <td>1.부동산 투자시 상환횟수가 표시되면 좋겠어요 언제쯤 상환예정인지 알 수 있도록요....</td>
    </tr>
  </tbody>
</table>
</div>




```python
sent = '김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를 찾으러 속세로 내려온 인물이다.'
new_sent = sent.replace(" ", '') # 띄어쓰기가 없는 문장 임의로 만들기
print(new_sent)


spacing = Spacing()
kospacing_sent = spacing(new_sent) 

```

    김철수는극중두인격의사나이이광수역을맡았다.철수는한국유일의태권도전승자를가리는결전의날을앞두고10년간함께훈련한사형인유연재(김광수분)를찾으러속세로내려온인물이다.
    

### 2.Py-Hanspell

Py-Hanspell은 네이버 한글 맞춤법 검사기를 바탕으로 만들어진 패키지입니다.\
!pip install git+https://github.com/ssut/py-hanspell.git


```python
from hanspell import spell_checker

sent = "맞춤법 틀리면 외 않되? 쓰고싶은대로쓰면돼지 "
spelled_sent = spell_checker.check(sent)

hanspell_sent = spelled_sent.checked
print(hanspell_sent)
```

    맞춤법 틀리면 왜 안돼? 쓰고 싶은 대로 쓰면 되지
    


```python
spelled_sent = spell_checker.check(new_sent)

hanspell_sent = spelled_sent.checked
print(hanspell_sent)
print(kospacing_sent) # 앞서 사용한 kospacing 패키지에서 얻은 결과
```

    김철수는 극 중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연제(김광수 분)를 찾으러 속세로 내려온 인물이다.
    김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를 찾으러 속세로 내려온 인물이다.
    


```python
df_hanspell = df.copy()
df_hanspell.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num</th>
      <th>contents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>넷플릭스 돈을 같이 모으고 싶어용</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>자동이체날짜를 알고 싶어요</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1.부동산 투자시 상환횟수가 표시되면 좋겠어요 언제쯤 상환예정인지 알수있도록요. 2...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>가계부 수입에 비해 지출초과분을 미리 알려줘서 과소비방지를 해줬으면 좋겠습니다.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>가계부 추출 기능! 통신사별 멤버십 혜택이 가능한 장소, 정보, 접근성 향상에 관련...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_hanspell['after'] = list(map(lambda x: re.sub('[\/:*?"<>|&]', '', x), df_hanspell['contents']))

# 특수문자가 있는 경우 교정값 return을 못함. 전처리.
df_hanspell['after'] = list(map(lambda x:spell_checker.check(x).checked, df_hanspell['after']))
```


```python
df_hanspell[:10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num</th>
      <th>contents</th>
      <th>after</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>넷플릭스 돈을 같이 모으고 싶어용</td>
      <td>넷플릭스 돈을 같이 모으고 싶어요</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>자동이체날짜를 알고 싶어요</td>
      <td>자동이체 날짜를 알고 싶어요</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>1.부동산 투자시 상환횟수가 표시되면 좋겠어요 언제쯤 상환예정인지 알수있도록요. 2...</td>
      <td>1. 부동산 투자 시 상환 횟수가 표시되면 좋겠어요 언제쯤 상환 예정인지 알 수 있...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>가계부 수입에 비해 지출초과분을 미리 알려줘서 과소비방지를 해줬으면 좋겠습니다.</td>
      <td>가계부 수입에 비해 지출 초과분을 미리 알려줘서 과소비 방지를 해줬으면 좋겠습니다.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>가계부 추출 기능! 통신사별 멤버십 혜택이 가능한 장소, 정보, 접근성 향상에 관련...</td>
      <td>가계부 추출 기능! 통신사별 멤버십 혜택이 가능한 장소, 정보, 접근성 향상에 관련...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8</td>
      <td>각 카드별로 내가 혜택을 잘 받고 있는지 관리하고 확인이 가능하면 좋겠다. 실적을 ...</td>
      <td>각 카드별로 내가 혜택을 잘 받고 있는지 관리하고 확인이 가능하면 좋겠다. 실적을 ...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>9</td>
      <td>각종 금융사별 카드 내역을 다 종합해서, 내가 어느 카테고리에서 썻는지 쉽게 볼수있었으면</td>
      <td>각종 금융사별 카드 내역을 다 종합해서, 내가 어느 카테고리에서 썼는지 쉽게 볼 수...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10</td>
      <td>각종 브랜드별 생일축하 쿠폰이나 기념일 혜택을 찾아주면 좋겠어요 하나도 못 누리고 있음</td>
      <td>각종 브랜드별 생일 축하 쿠폰이나 기념일 혜택을 찾아주면 좋겠어요 하나도 못 누리고 있음</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11</td>
      <td>각종 포인트들 전부 제각각 흩어져있고, 대체 어떤 포인트를 어디서 봐야하는지 얼마나...</td>
      <td>각종 포인트들 전부 제각각 흩어져있고, 대체 어떤 포인트를 어디서 봐야 하는지 얼마...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>12</td>
      <td>간편송금의 장점으로 인해서 주거래은행 어플보다 토스이용을 하는편이지만 타행들도 지금...</td>
      <td>간편송금의 장점으로 인해서 주거래은행 어플보다 토스 이용을 하는 편이지만 타행들도 ...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### 3. SOYNLP를 이용한 단어 토큰화

soynlp는 품사 태깅, 단어 토큰화 등을 지원하는 단어 토크나이저입니다. \
비지도 학습으로 단어 토큰화를 한다는 특징을 갖고 있으며, 데이터에 자주 등장하는 단어들을 단어로 분석합니다. \
soynlp 단어 토크나이저는 내부적으로 단어 점수 표로 동작합니다. \
이 점수는 응집 확률(cohesion probability)과 브랜칭 엔트로피(branching entropy)를 활용합니다.

!pip install soynlp


1. 신조어 문제
soynlp를 소개하기 전에 기존의 형태소 분석기가 가진 문제는 무엇이었는지, SOYNLP가 어떤 점에서 유용한지 정리해봅시다. \
기존의 형태소 분석기는 신조어나 형태소 분석기에 등록되지 않은 단어 같은 경우에는 제대로 구분하지 못하는 단점이 있었습니다.


```python
from konlpy.tag import Okt
tokenizer = Okt()
print(tokenizer.morphs('에이비식스 이대휘 1월 최애돌 기부 요정'))
```


```python
tokenizer = Okt()
```


    ---------------------------------------------------------------------------

    JVMNotFoundException                      Traceback (most recent call last)

    <ipython-input-105-b2eaee32874e> in <module>
    ----> 1 tokenizer = Okt()
    

    ~\Anaconda3\envs\shomy\lib\site-packages\konlpy\tag\_okt.py in __init__(self, jvmpath, max_heap_size)
         49     def __init__(self, jvmpath=None, max_heap_size=1024):
         50         if not jpype.isJVMStarted():
    ---> 51             jvm.init_jvm(jvmpath, max_heap_size)
         52 
         53         oktJavaPackage = jpype.JPackage('kr.lucypark.okt')
    

    ~\Anaconda3\envs\shomy\lib\site-packages\konlpy\jvm.py in init_jvm(jvmpath, max_heap_size)
         53     classpath = [f.format(*args) for f in folder_suffix]
         54 
    ---> 55     jvmpath = jvmpath or jpype.getDefaultJVMPath()
         56 
         57     # NOTE: Temporary patch for Issue #76. Erase when possible.
    

    ~\Anaconda3\envs\shomy\lib\site-packages\jpype\_jvmfinder.py in getDefaultJVMPath()
         72     else:
         73         finder = LinuxJVMFinder()
    ---> 74     return finder.get_jvm_path()
         75 
         76 
    

    ~\Anaconda3\envs\shomy\lib\site-packages\jpype\_jvmfinder.py in get_jvm_path(self)
        213                                    "found. Try setting up the JAVA_HOME "
        214                                    "environment variable properly."
    --> 215                                    .format(self._libfile))
        216 
        217     def _get_from_java_home(self):
    

    JVMNotFoundException: No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly.



```python

```

2. 학습하기\
soynlp는 기본적으로 학습에 기반한 토크나이저이므로 학습에 필요한 한국어 문서를 다운로드합니다.


```python
import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor
```


```python
# 훈련 데이터를 다수의 문서로 분리
corpus = DoublespaceLineCorpus("2016-10-20.txt")
len(corpus)
```

    local variable 'f' referenced before assignment
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-107-80c64b27afc9> in <module>
          1 # 훈련 데이터를 다수의 문서로 분리
          2 corpus = DoublespaceLineCorpus("2016-10-20.txt")
    ----> 3 len(corpus)
    

    ValueError: __len__() should return >= 0



```python

```


```python

```


```python
from konlpy.tag import Okt
from konlpy.tag import Kkma
```


```python
from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

print('OKT 형태소 분석 :',okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print('OKT 품사 태깅 :',okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print('OKT 명사 추출 :',okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 
```


    ---------------------------------------------------------------------------

    JVMNotFoundException                      Traceback (most recent call last)

    <ipython-input-111-6d1f0badd24e> in <module>
          2 from konlpy.tag import Kkma
          3 
    ----> 4 okt = Okt()
          5 kkma = Kkma()
          6 
    

    ~\Anaconda3\envs\shomy\lib\site-packages\konlpy\tag\_okt.py in __init__(self, jvmpath, max_heap_size)
         49     def __init__(self, jvmpath=None, max_heap_size=1024):
         50         if not jpype.isJVMStarted():
    ---> 51             jvm.init_jvm(jvmpath, max_heap_size)
         52 
         53         oktJavaPackage = jpype.JPackage('kr.lucypark.okt')
    

    ~\Anaconda3\envs\shomy\lib\site-packages\konlpy\jvm.py in init_jvm(jvmpath, max_heap_size)
         53     classpath = [f.format(*args) for f in folder_suffix]
         54 
    ---> 55     jvmpath = jvmpath or jpype.getDefaultJVMPath()
         56 
         57     # NOTE: Temporary patch for Issue #76. Erase when possible.
    

    ~\Anaconda3\envs\shomy\lib\site-packages\jpype\_jvmfinder.py in getDefaultJVMPath()
         72     else:
         73         finder = LinuxJVMFinder()
    ---> 74     return finder.get_jvm_path()
         75 
         76 
    

    ~\Anaconda3\envs\shomy\lib\site-packages\jpype\_jvmfinder.py in get_jvm_path(self)
        213                                    "found. Try setting up the JAVA_HOME "
        214                                    "environment variable properly."
    --> 215                                    .format(self._libfile))
        216 
        217     def _get_from_java_home(self):
    

    JVMNotFoundException: No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly.



```python
import platform
print(platform.architecture())
```

    ('64bit', 'WindowsPE')
    
