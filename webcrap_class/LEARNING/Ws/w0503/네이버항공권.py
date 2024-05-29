import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# DB연결부분
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# for i in range(5):
#     url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page={i+1}"
#     browser.get(url)
#     time.sleep(2)

#     # text소스를 html소스로 파싱
#     soup = BeautifulSoup(browser.page_source,"lxml")

#     #### find_all()
#     hotels = soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
#     print("전체 개수 : ",len(hotels))
#     title = hotels[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
#     print("제목 : ",title.text)

url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page=1"
browser.get(url)
time.sleep(2)

# text소스를 html소스로 파싱
soup = BeautifulSoup(browser.page_source,"lxml")


def sleep():
    time.sleep(random.random() + 1)
def longsleep():
    time.sleep(random.random() + 3)

url = 'https://www.naver.com'
# url = 'https://flight.naver.com/flights/domestic/SEL-CJU-20240505/CJU-SEL-20240507?adult=2&fareType=YC'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
# 네이버 항공권 검색
elem = browser.find_element(By.ID, 'query')
elem.send_keys('네이버 항공권', Keys.ENTER)
sleep()
# 항공권 사이트 링크 클릭
elem = browser.find_element(By.CLASS_NAME, 'link_name')
elem.click()
sleep()
# 새 창으로 이동
browser.switch_to.window(browser.window_handles[-1])
# 출발지역 선택
start = browser.find_element(By.CLASS_NAME, 'start')
start.click()
sleep()
domestic = browser.find_element(By.CLASS_NAME, 'autocomplete_Collapse__tP3pM')
domestic.click()
sleep()
seoul = browser.find_element(By.CLASS_NAME, 'autocomplete_Airport__3_dRP')
sleep()
seoul.click()
longsleep()
# 도착지역 선택
end = browser.find_element(By.CLASS_NAME, 'end')
end.click()
sleep()
domestic = browser.find_element(By.CLASS_NAME, 'autocomplete_Collapse__tP3pM')
domestic.click()
sleep()
jeju = browser.find_elements(By.CLASS_NAME, 'autocomplete_Airport__3_dRP')[1]
sleep()
jeju.click()
sleep()
# 가는날 선택
depart_date = browser.find_elements(By.CLASS_NAME, 'select_Date__1aF7Y')[0]
depart_date.click()
sleep()
# 5월 테이블 선택
depart_date = browser.find_elements(By.TAG_NAME, 'table')[1]
depart_date = depart_date.find_elements(By.TAG_NAME, 'button')[25]
depart_date.click()
# 오는날 선택
arrive_date = browser.find_elements(By.CLASS_NAME, 'select_Date__1aF7Y')[1]
arrive_date.click()
sleep()
# 5월 테이블 선택
arrive_date = browser.find_elements(By.TAG_NAME, 'table')[1]
arrive_date = arrive_date.find_elements(By.TAG_NAME, 'button')[26]
arrive_date.click()
sleep()
# 인원 선택
passenger = browser.find_element(By.CLASS_NAME, 'select_Passenger__36sFM')
passenger.click()
sleep()
add_passenger = browser.find_element(By.CLASS_NAME, 'searchBox_outer__9n6IB')
add_passenger.click()
sleep()
# 검색버튼 클릭
search_btn = browser.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3')
search_btn.click()
search_btn.click()
time.sleep(10)
# 출발 항공정보
longsleep()
depart_data = browser.find_element(By.CLASS_NAME, 'domestic_results__yNAgI')
# 스크롤 내리기
scroll = 0
for _ in range(10):
    browser.execute_script(f"window.scrollTo(0, {scroll})")
    sleep()
    scroll += 700
# 항공편 자료 수집
depart_data = depart_data.find_elements(By.CLASS_NAME, 'domestic_Flight__sK0eA')
data = []
cnt = 1
for depart_flight in depart_data:
    flight_data = { 'no' : '',
                    'company' : '',
                    'departure-time' : '',
                    'arrival-time' : '',
                    'flight_time' : '',
                    'price' : ''
                    }
    flight_company = depart_flight.find_element(By.CLASS_NAME, 'domestic_heading__3GS2v').text.split('\n')[0]
    time_data = depart_flight.find_elements(By.CLASS_NAME, 'route_time__-2Z1T') # [0] : 출발시각 [1] : 도착 시각
    time_cost = depart_flight.find_element(By.CLASS_NAME, 'route_info__1RhUH')
    airport_data = depart_flight.find_elements(By.CLASS_NAME, 'route_code__3WUFO') #[0] : 출발공항 [1] : 도착 공항
    price_data = depart_flight.find_element(By.CLASS_NAME, 'domestic_num__2roTW')

    flight_data['no'] = cnt
    flight_data['company'] = flight_company
    flight_data['departure-time'] = time_data[0].text
    flight_data['arrival-time'] = time_data[1].text
    flight_data['flight_time'] = time_cost.text
    flight_data['price'] = price_data.text
    data.append(flight_data)
    cnt += 1
    # print('항공사 : ', flight_company)
    # print(f'여정 : {airport_data[0].text} -> {airport_data[1].text}')
    # print(f'운항 시간 : {time_data[0].text} - {time_data[1].text} 소요 시간 : {time_cost.text}')
    # print(f'좌석 정보 : {seat_data.text} {seat_data1.text} {price_data.text}원')
    # print('-'*100)



# 출발 클릭
arrive_click = depart_data[0]
arrive_click.click()
# 도착 항공정보
time.sleep(5)
depart_data = browser.find_element(By.CLASS_NAME, 'domestic_results__yNAgI')
scroll = 0
for _ in range(3):
    browser.execute_script(f"window.scrollTo(0, {scroll})")
    sleep()
    scroll += 700
depart_data = depart_data.find_elements(By.CLASS_NAME, 'domestic_Flight__sK0eA')
for depart_flight in depart_data[:3]:
    flight_company = depart_flight.find_element(By.CLASS_NAME, 'domestic_heading__3GS2v').text.split('\n')[0]
    time_data = depart_flight.find_element(By.CLASS_NAME, 'route_Route__2UInh').text.split('\n')
    price_data = depart_flight.find_element(By.CLASS_NAME, 'domestic_prices__3N88F').text.split('\n')
    print('항공사 : ', flight_company)
    print('시간 정보 :', '출발 시각(출발공항) {} 도착 시각(도착공항) : {} 소요 시간 : {}'.format(*time_data))
    if(len(price_data) == 3):
        print('가격 정보 :', '{} {} {}'.format(*price_data))
    elif(len(price_data) == 2):
        print('가격 정보 :', '{} {}'.format(*price_data))
    else:
        print('가격 정보 :', '{}'.format(*price_data))
    print('-'*100)
    
    # DB 저장
    if all([]):  # 모든 데이터가 있을 때만 DB에 삽입
        sql = f"INSERT INTO DAUM_MOVIE VALUES (dno_seq.nextval, :title, :img, :audience, :ddate)"
        cursor.execute(sql, {'title': title, 'img': img, 'audience': audience, 'ddate': ddate})
        print("DB에 저장되었습니다.")
    else:
        print("누락된 데이터가 있어 DB에 저장되지 않았습니다.")

print("-" * 30)

conn.commit()  # 커밋 메서드가 execute() 메서드를 대신할 수 있습니다.
cursor.close()
conn.close()