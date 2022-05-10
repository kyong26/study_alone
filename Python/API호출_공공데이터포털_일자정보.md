```python
# https://www.data.go.kr/data/

import requests
import pandas as pd
import numpy as np
import requests
from urllib import parse
from bs4 import BeautifulSoup
from datetime import datetime

'''
정부 API
- 계정: kyong26, cermerus12!
- End Poing: http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService
- 일반인증키(Encoding): GVXMedFOG13uoOLsx40U%2FsQ3qbmk1xCt918OWfwbGRRWMgXaKb5HCNvQPFgrOzdRjY%2BwkupnMI%2BTapfIJuilWQ%3D%3D
- 일반인증키(Decoding): GVXMedFOG13uoOLsx40U/sQ3qbmk1xCt918OWfwbGRRWMgXaKb5HCNvQPFgrOzdRjY+wkupnMI+TapfIJuilWQ==
'''

api_key_utf8 = "GVXMedFOG13uoOLsx40U%2FsQ3qbmk1xCt918OWfwbGRRWMgXaKb5HCNvQPFgrOzdRjY%2BwkupnMI%2BTapfIJuilWQ%3D%3D"
```

### API Conn Test


```python
url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/"
api_key_decode = parse.unquote(api_key_utf8)

url_holiday = url + "getRestDeInfo"
params = {
            "ServiceKey": api_key_decode,
            "solYear": 2021,
            "numOfRows": 100
            }

response = requests.get(url_holiday, params=params)
```


```python
print(response.text)
```

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header><resultCode>00</resultCode><resultMsg>NORMAL SERVICE.</resultMsg></header><body><items><item><dateKind>01</dateKind><dateName>1월1일</dateName><isHoliday>Y</isHoliday><locdate>20210101</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>설날</dateName><isHoliday>Y</isHoliday><locdate>20210211</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>설날</dateName><isHoliday>Y</isHoliday><locdate>20210212</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>설날</dateName><isHoliday>Y</isHoliday><locdate>20210213</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>삼일절</dateName><isHoliday>Y</isHoliday><locdate>20210301</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>어린이날</dateName><isHoliday>Y</isHoliday><locdate>20210505</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>부처님오신날</dateName><isHoliday>Y</isHoliday><locdate>20210519</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>현충일</dateName><isHoliday>Y</isHoliday><locdate>20210606</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>광복절</dateName><isHoliday>Y</isHoliday><locdate>20210815</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>대체공휴일</dateName><isHoliday>Y</isHoliday><locdate>20210816</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>추석</dateName><isHoliday>Y</isHoliday><locdate>20210920</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>추석</dateName><isHoliday>Y</isHoliday><locdate>20210921</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>추석</dateName><isHoliday>Y</isHoliday><locdate>20210922</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>개천절</dateName><isHoliday>Y</isHoliday><locdate>20211003</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>대체공휴일</dateName><isHoliday>Y</isHoliday><locdate>20211004</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>한글날</dateName><isHoliday>Y</isHoliday><locdate>20211009</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>대체공휴일</dateName><isHoliday>Y</isHoliday><locdate>20211011</locdate><seq>1</seq></item><item><dateKind>01</dateKind><dateName>기독탄신일</dateName><isHoliday>Y</isHoliday><locdate>20211225</locdate><seq>1</seq></item></items><numOfRows>100</numOfRows><pageNo>1</pageNo><totalCount>18</totalCount></body></response>


### 공휴일 정보 확인하기

https://yogyui.tistory.com/entry/공공데이터포털공휴일-데이터-조회-REST-API


```python
def getHoliday(year: int) -> pd.DataFrame:
    
    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "solYear": year,
        "numOfRows": 100
    }
    

    temp = ["월", "화", "수", "목", "금", "토", "일"]

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        dt = datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
        item_dict = {
            "이름": item.find("datename").text.strip(),
            "날짜": dt,
            "요일": temp[dt.weekday()],
            "종류": item.find("datekind").text.strip(),
        }
        item_list.append(item_dict)
    return pd.DataFrame(item_list)
```


```python
getHoliday(2022)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>날짜</th>
      <th>요일</th>
      <th>종류</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1월1일</td>
      <td>2022-01-01</td>
      <td>토</td>
      <td>01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>설날</td>
      <td>2022-01-31</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>설날</td>
      <td>2022-02-01</td>
      <td>화</td>
      <td>01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>설날</td>
      <td>2022-02-02</td>
      <td>수</td>
      <td>01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>삼일절</td>
      <td>2022-03-01</td>
      <td>화</td>
      <td>01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>대통령선거일</td>
      <td>2022-03-09</td>
      <td>수</td>
      <td>01</td>
    </tr>
    <tr>
      <th>6</th>
      <td>어린이날</td>
      <td>2022-05-05</td>
      <td>목</td>
      <td>01</td>
    </tr>
    <tr>
      <th>7</th>
      <td>부처님오신날</td>
      <td>2022-05-08</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>8</th>
      <td>전국동시지방선거</td>
      <td>2022-06-01</td>
      <td>수</td>
      <td>01</td>
    </tr>
    <tr>
      <th>9</th>
      <td>현충일</td>
      <td>2022-06-06</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>10</th>
      <td>광복절</td>
      <td>2022-08-15</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>11</th>
      <td>추석</td>
      <td>2022-09-09</td>
      <td>금</td>
      <td>01</td>
    </tr>
    <tr>
      <th>12</th>
      <td>추석</td>
      <td>2022-09-10</td>
      <td>토</td>
      <td>01</td>
    </tr>
    <tr>
      <th>13</th>
      <td>추석</td>
      <td>2022-09-11</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>14</th>
      <td>대체공휴일</td>
      <td>2022-09-12</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>15</th>
      <td>개천절</td>
      <td>2022-10-03</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>16</th>
      <td>한글날</td>
      <td>2022-10-09</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>17</th>
      <td>대체공휴일</td>
      <td>2022-10-10</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>18</th>
      <td>기독탄신일</td>
      <td>2022-12-25</td>
      <td>일</td>
      <td>01</td>
    </tr>
  </tbody>
</table>
</div>




```python
Holiday = getHoliday(2022)
```


```python
Holiday['구분'] = '공휴일API'
```

### 기념일 정보 확인하기


```python
def getAnniversary(year: int) -> pd.DataFrame:

    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getAnniversaryInfo"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "numOfRows": 100,
        "solYear": year,
    }


    temp = ["월", "화", "수", "목", "금", "토", "일"]

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        dt = datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
        item_dict = {
            "이름": item.find("datename").text.strip(),
            "날짜": dt,
            "요일": temp[dt.weekday()],
            "종류": item.find("datekind").text.strip(),
        }
        item_list.append(item_dict)
    return pd.DataFrame(item_list)
```


```python
getAnniversary(2022) 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>날짜</th>
      <th>요일</th>
      <th>종류</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2·28 민주운동 기념일</td>
      <td>2022-02-28</td>
      <td>월</td>
      <td>02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>납세자의 날</td>
      <td>2022-03-03</td>
      <td>목</td>
      <td>02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3·8 민주의거 기념일</td>
      <td>2022-03-08</td>
      <td>화</td>
      <td>02</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3·15 의거 기념일</td>
      <td>2022-03-15</td>
      <td>화</td>
      <td>02</td>
    </tr>
    <tr>
      <th>4</th>
      <td>상공의 날</td>
      <td>2022-03-16</td>
      <td>수</td>
      <td>02</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>아동학대예방의 날</td>
      <td>2022-11-19</td>
      <td>토</td>
      <td>02</td>
    </tr>
    <tr>
      <th>62</th>
      <td>소비자의 날</td>
      <td>2022-12-03</td>
      <td>토</td>
      <td>02</td>
    </tr>
    <tr>
      <th>63</th>
      <td>무역의 날</td>
      <td>2022-12-05</td>
      <td>월</td>
      <td>02</td>
    </tr>
    <tr>
      <th>64</th>
      <td>자원봉사자의 날</td>
      <td>2022-12-05</td>
      <td>월</td>
      <td>02</td>
    </tr>
    <tr>
      <th>65</th>
      <td>원자력 안전 및 진흥의 날</td>
      <td>2022-12-27</td>
      <td>화</td>
      <td>02</td>
    </tr>
  </tbody>
</table>
<p>66 rows × 4 columns</p>
</div>




```python
Anniversary = getAnniversary(2022) 
```


```python
Anniversary['구분'] = '기념일API'
```

### 국경일 정보 확인하기


```python
def getHoliDe(year: int) -> pd.DataFrame:

    url = " http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "numOfRows": 100,
        "solYear": year,
    }


    temp = ["월", "화", "수", "목", "금", "토", "일"]

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        dt = datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
        item_dict = {
            "이름": item.find("datename").text.strip(),
            "날짜": dt,
            "요일": temp[dt.weekday()],
            "종류": item.find("datekind").text.strip(),
        }
        item_list.append(item_dict)
    return pd.DataFrame(item_list)
```


```python
getHoliDe(2022)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>날짜</th>
      <th>요일</th>
      <th>종류</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1월1일</td>
      <td>2022-01-01</td>
      <td>토</td>
      <td>01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>설날</td>
      <td>2022-01-31</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>설날</td>
      <td>2022-02-01</td>
      <td>화</td>
      <td>01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>설날</td>
      <td>2022-02-02</td>
      <td>수</td>
      <td>01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>삼일절</td>
      <td>2022-03-01</td>
      <td>화</td>
      <td>01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>대통령선거일</td>
      <td>2022-03-09</td>
      <td>수</td>
      <td>01</td>
    </tr>
    <tr>
      <th>6</th>
      <td>어린이날</td>
      <td>2022-05-05</td>
      <td>목</td>
      <td>01</td>
    </tr>
    <tr>
      <th>7</th>
      <td>부처님오신날</td>
      <td>2022-05-08</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>8</th>
      <td>전국동시지방선거</td>
      <td>2022-06-01</td>
      <td>수</td>
      <td>01</td>
    </tr>
    <tr>
      <th>9</th>
      <td>현충일</td>
      <td>2022-06-06</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>10</th>
      <td>제헌절</td>
      <td>2022-07-17</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>11</th>
      <td>광복절</td>
      <td>2022-08-15</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>12</th>
      <td>추석</td>
      <td>2022-09-09</td>
      <td>금</td>
      <td>01</td>
    </tr>
    <tr>
      <th>13</th>
      <td>추석</td>
      <td>2022-09-10</td>
      <td>토</td>
      <td>01</td>
    </tr>
    <tr>
      <th>14</th>
      <td>추석</td>
      <td>2022-09-11</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>15</th>
      <td>대체공휴일</td>
      <td>2022-09-12</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>16</th>
      <td>개천절</td>
      <td>2022-10-03</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>17</th>
      <td>한글날</td>
      <td>2022-10-09</td>
      <td>일</td>
      <td>01</td>
    </tr>
    <tr>
      <th>18</th>
      <td>대체공휴일</td>
      <td>2022-10-10</td>
      <td>월</td>
      <td>01</td>
    </tr>
    <tr>
      <th>19</th>
      <td>기독탄신일</td>
      <td>2022-12-25</td>
      <td>일</td>
      <td>01</td>
    </tr>
  </tbody>
</table>
</div>




```python
HoliDe = getHoliDe(2022) 
HoliDe['구분'] = '국경일API'
```

### 24절기 정보 확인하기


```python
def get24Divisions(year: int) -> pd.DataFrame:

    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/get24DivisionsInfo"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "numOfRows": 100,
        "solYear": year,
    }


    temp = ["월", "화", "수", "목", "금", "토", "일"]

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        dt = datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
        item_dict = {
            "이름": item.find("datename").text.strip(),
            "날짜": dt,
            "요일": temp[dt.weekday()],
            "종류": item.find("datekind").text.strip(),
        }
        item_list.append(item_dict)
    return pd.DataFrame(item_list)
```


```python
get24Divisions(2022) 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>날짜</th>
      <th>요일</th>
      <th>종류</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>소한</td>
      <td>2022-01-05</td>
      <td>수</td>
      <td>03</td>
    </tr>
    <tr>
      <th>1</th>
      <td>대한</td>
      <td>2022-01-20</td>
      <td>목</td>
      <td>03</td>
    </tr>
    <tr>
      <th>2</th>
      <td>입춘</td>
      <td>2022-02-04</td>
      <td>금</td>
      <td>03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>우수</td>
      <td>2022-02-19</td>
      <td>토</td>
      <td>03</td>
    </tr>
    <tr>
      <th>4</th>
      <td>경칩</td>
      <td>2022-03-05</td>
      <td>토</td>
      <td>03</td>
    </tr>
    <tr>
      <th>5</th>
      <td>춘분</td>
      <td>2022-03-21</td>
      <td>월</td>
      <td>03</td>
    </tr>
    <tr>
      <th>6</th>
      <td>청명</td>
      <td>2022-04-05</td>
      <td>화</td>
      <td>03</td>
    </tr>
    <tr>
      <th>7</th>
      <td>곡우</td>
      <td>2022-04-20</td>
      <td>수</td>
      <td>03</td>
    </tr>
    <tr>
      <th>8</th>
      <td>입하</td>
      <td>2022-05-05</td>
      <td>목</td>
      <td>03</td>
    </tr>
    <tr>
      <th>9</th>
      <td>소만</td>
      <td>2022-05-21</td>
      <td>토</td>
      <td>03</td>
    </tr>
    <tr>
      <th>10</th>
      <td>망종</td>
      <td>2022-06-06</td>
      <td>월</td>
      <td>03</td>
    </tr>
    <tr>
      <th>11</th>
      <td>하지</td>
      <td>2022-06-21</td>
      <td>화</td>
      <td>03</td>
    </tr>
    <tr>
      <th>12</th>
      <td>소서</td>
      <td>2022-07-07</td>
      <td>목</td>
      <td>03</td>
    </tr>
    <tr>
      <th>13</th>
      <td>대서</td>
      <td>2022-07-23</td>
      <td>토</td>
      <td>03</td>
    </tr>
    <tr>
      <th>14</th>
      <td>입추</td>
      <td>2022-08-07</td>
      <td>일</td>
      <td>03</td>
    </tr>
    <tr>
      <th>15</th>
      <td>처서</td>
      <td>2022-08-23</td>
      <td>화</td>
      <td>03</td>
    </tr>
    <tr>
      <th>16</th>
      <td>백로</td>
      <td>2022-09-08</td>
      <td>목</td>
      <td>03</td>
    </tr>
    <tr>
      <th>17</th>
      <td>추분</td>
      <td>2022-09-23</td>
      <td>금</td>
      <td>03</td>
    </tr>
    <tr>
      <th>18</th>
      <td>한로</td>
      <td>2022-10-08</td>
      <td>토</td>
      <td>03</td>
    </tr>
    <tr>
      <th>19</th>
      <td>상강</td>
      <td>2022-10-23</td>
      <td>일</td>
      <td>03</td>
    </tr>
    <tr>
      <th>20</th>
      <td>입동</td>
      <td>2022-11-07</td>
      <td>월</td>
      <td>03</td>
    </tr>
    <tr>
      <th>21</th>
      <td>소설</td>
      <td>2022-11-22</td>
      <td>화</td>
      <td>03</td>
    </tr>
    <tr>
      <th>22</th>
      <td>대설</td>
      <td>2022-12-07</td>
      <td>수</td>
      <td>03</td>
    </tr>
    <tr>
      <th>23</th>
      <td>동지</td>
      <td>2022-12-22</td>
      <td>목</td>
      <td>03</td>
    </tr>
  </tbody>
</table>
</div>




```python
Divisions = get24Divisions(2022) 
Divisions['구분'] = '24절기API'
```

### 잡절 정보 확인하기


```python
def getSundryDay(year: int) -> pd.DataFrame:

    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getSundryDayInfo"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "numOfRows": 300,
        "solYear": year,
    }


    temp = ["월", "화", "수", "목", "금", "토", "일"]

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        dt = datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d')
        item_dict = {
            "이름": item.find("datename").text.strip(),
            "날짜": dt,
            "요일": temp[dt.weekday()],
            "종류": item.find("datekind").text.strip(),
        }
        item_list.append(item_dict)
    return pd.DataFrame(item_list)
```


```python
getSundryDay(2022) 
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>날짜</th>
      <th>요일</th>
      <th>종류</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정월대보름</td>
      <td>2022-02-15</td>
      <td>화</td>
      <td>04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>한식</td>
      <td>2022-04-06</td>
      <td>수</td>
      <td>04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>단오</td>
      <td>2022-06-03</td>
      <td>금</td>
      <td>04</td>
    </tr>
    <tr>
      <th>3</th>
      <td>초복</td>
      <td>2022-07-16</td>
      <td>토</td>
      <td>04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>중복</td>
      <td>2022-07-26</td>
      <td>화</td>
      <td>04</td>
    </tr>
    <tr>
      <th>5</th>
      <td>칠석</td>
      <td>2022-08-04</td>
      <td>목</td>
      <td>04</td>
    </tr>
    <tr>
      <th>6</th>
      <td>말복</td>
      <td>2022-08-15</td>
      <td>월</td>
      <td>04</td>
    </tr>
  </tbody>
</table>
</div>




```python
SundryDay = getSundryDay(2022) 
SundryDay['구분'] = '잡절API'
```

### 절기 dataframe 합산해서 excel로 export


```python
final_output = pd.concat([Holiday,Anniversary,HoliDe,Divisions,SundryDay])
```


```python
final_output['날짜'] = final_output['날짜'].astype('str')
```


```python
final_output = final_output.reset_index()
del final_output['index']
```


```python
final_output.to_excel('/Users/seomingyeong/Downloads/gov_date_api_info_2022.xlsx')
```
