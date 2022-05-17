# Crawling_Card_Plate_Img

아래 크롤링은, 카드사 간 협약에 근거했습니다.\
(서로간의 카드 플레이트 이미지를 마이데이터 서비스에서 자유롭게 사용할 수 있도록 합의)\
현재 하나카드 마이데이터 내자산한눈에>카드조회 페이지에서, \
보유한 카드들의 플레이트 이미지를 보여주고 있습니다.
<br>
<br>

### 문제정의 
하나카드 마이데이터 서비스 오픈 전, 서비스 준비를 위한 카드 플레이트 이미지 필요\
⇒ 4,000개 준비 완료\
마이데이터 서비스 오픈 후 새로 출시된 카드들에 대해 이미지 지속 업데이트가 필요함
<br>
<br>

### 가설설정
신규Mass 카드의 경우, 각 카드사 홈페이지에 가장 빨리 업로드 됨\
정기적으로 카드사 홈페이지에서 카드 플레이트 이미지를 추가로 가져오기로 함
<br>
<br>


### 데이터 분석
필요한 카드의 이름을 카드사 홈페이지에서 검색하고,\
검색 결과로 나온 이미지들을 가져오는 코드 작성

에러가 생겨서 작업이 중단되면, 어느 단계에서 중단되었는지 확인할 수 있도록 로그를 print


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

# 실행상황을 모니터링 할 수 있는 log 출력
def logging_time(*messages):
    today = datetime.datetime.today()
    log_time = today.strftime('[%Y/%m/%d %H:%M:%S]')
    log = list()
    # 넘겨받은 메시지를 unzip 해서 각 메시지를 로그 리스트의 개별 원소로 저장
    for message in messages:
        log.append(str(message))
        print(log_time + '::' + ' '.join(log))
    sys.stdout.flush()

def mydata_crawling():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # 저장 directory 위치 지정
    root_dir = '/Users/seomingyeong/Downloads/crawling/'
    img_dir = root_dir + 'shinhan/'
    # 마이데이터 제공자 기관코드 dictionary 생성
    bur_no = {'shinhan':'D1AAEX0000', 'kb':'D1AAAF0000', 'hyundai':'D1AAFO0000', 'woori':'D1AAAH0000'}

# 크롤링 시작: 검색창에 플레이트 이미지 수집이 필요한 파일명을 순차적으로 진행
def shinhan_crawling(shinhan):
    # 로그출력 시작
    logging_time("loop start")
    cnt_all = len(shinhan) # 이미지 필요한 전체 카드 개수
    cnt_noimg = 0
    not_found = []

    # 결과값 csv로 export를 위한 dataframe 생성
    df = pd.DataFrame({ 'company_name': pd.Series([], dtype='str'),
                        'searched_card_name': pd.Series([], dtype='str'),
                        'seq': pd.Series([], dtype='int'),
                        'result_card_name' : pd.Series([], dtype='str')})

    # loop: 카드명 하나씩 꺼내서 이미지 저장 및 csv 리스트에 추가함
    for i in range(len(shinhan)):
        logging_time(shinhan[i])
        card = shinhan[i]
        con_url = 'https://www.shinhancard.com/mob/MOBFM004N/MOBFM004R0201.shc?query=' + str(card)

        logging_time(shinhan[i] + ":url접속")
        driver.get(con_url) #해당 url로 이동함
        sleep(2) # pause

        logging_time(shinhan[i] + ":소스코드 가져옴")
        elements = driver.page_source # 소스 가져옴
        bsObj = BeautifulSoup(elements, "html.parser")
        # 카드 정보가 있는 class 정보를 불러옴
        info = bsObj.find("ul", {"class": "card_list_wrap"}) # 카드 리스트가 있는 전체 이미지 확인
        # 검색결과 카드명 리스트 생성
        card_name = []
        logging_time(shinhan[i] + ":카드리스트 생성")
        card_name = info.find_all("h5", {"class":"s_title"})

        if card_name == [] : # 검색결과가 없는 경우
            logging_time(shinhan[i] + ":카드 이미지 검색결과 없음")
            cnt_noimg+=1
            # 크롤링 실패한 카드이름 저장
            not_found.append(shinhan[i])
        elif card_name != [] : # 검색결과가 있는경우
            for j in range(len(card_name)):
                card_name[j] = card_name[j].get_text()
                card_name[j] = re.sub('[\/:*?"<>|]', '', card_name[j])
            cnt = len(card_name) # 검색결과 카드개수 확인

            # 카드 이미지 url 가져오기
            logging_time(shinhan[i] + ":이미지url 가져오기")
            imageurl = [] # 이미지
            extension = []  # 확장자
            for j in range(cnt):
                url = info.find("img", {"alt": card_name[j]})
                url = str(url).split('src="')
                url = str(url[1]).split('"')
                url = 'https://www.shinhancard.com' + url[0]
                imageurl.append(url)
                extension.append(url[-4:])
            # 이미지 저장
            logging_time(shinhan[i] + ":이미지 저장")
            for j in range(cnt):
                imagename = bur_no['shinhan'] + '_' + card_name[j]
                image_dir = img_dir + imagename + extension[j]
                try :
                    urllib.request.urlretrieve(imageurl[j], image_dir)
                except :
                    img_data = requests.get(imageurl[j]).content
                    with open(image_dir, 'wb') as handler:
                        handler.write(img_data)
            # dataframe에 정리(csv저장용)
            logging_time(shinhan[i] + ":df 카드정보 추가")
            card_info=[]
            for j in range(cnt):
                one_card_info = ['Shinhan', card, j+1, card_name[j]]
                card_info.append(one_card_info)
            df = df.append(pd.DataFrame(card_info, columns=df.columns), ignore_index=True)
        # pause
        sleep(3)
    not_found = pd.DataFrame(not_found, columns={'card_name'})
    # 로그생성종료: 작업완료
    logging_time("loop end")
    # 크롤링한 카드리스트 csv 파일로 저장
    df.to_csv(img_dir + 'shinhan_card_list.csv')
    not_found.to_csv(img_dir + 'shinhan_card_not_found_list.csv') # 카드사 홈페이지 외 재탐색 필요
    # 크롤링 결과 요약출력
    print("크롤링 시도한 카드 개수: " , cnt_all)
    print("성공:" , (cnt_all-cnt_noimg))
    print("실패:" , cnt_noimg)


# 크롤링 필요한 신한카드 카드명(예시)
shinhan = ['신한Pay계좌결제 체크','11번가','마이홈플러스(체크)','S20(체크)',
           '국민내일배움 Simple','신세계백화점','My Shop S-Choice 체크',
           '워너원 SOL Deep Dream(체크)', '교직원복지 LOVE','Deep On Platinum+']
# 크롤링 실행
mydata_crawling()
shinhan_crawling(shinhan)
```

### 결과
추가 수집이 필요한 카드들이 많은 경우 유용함

다만, 카드사 홈페이지에 등록되지 않은 카드들(제휴카드)은 홈페이지에서 Crawling 불가능\
검색결과 없는 카드들은 Googling을 통해 추가 이미지 수집이 필요함
