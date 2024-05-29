import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import random
def sleep():
    time.sleep(random.random() + 1)
def longsleep():
    time.sleep(random.random() + 3)
path = os.getcwd() + '\web_study\w0424\\'
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
depart_date = depart_date.find_elements(By.TAG_NAME, 'button')[4]
depart_date.click()
# 오는날 선택
arrive_date = browser.find_elements(By.CLASS_NAME, 'select_Date__1aF7Y')[1]
arrive_date.click()
sleep()
# 5월 테이블 선택
arrive_date = browser.find_elements(By.TAG_NAME, 'table')[1]
arrive_date = arrive_date.find_elements(By.TAG_NAME, 'button')[5]
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
                    'depart_airport-code' : '',
                    'arrive-airport-code' : '',
                    'depart-time' : '',
                    'arrive-time' : '',
                    'time-cost' : '',
                    'seat-type' : '',
                    'price' : ''
                    }
    flight_company = depart_flight.find_element(By.CLASS_NAME, 'domestic_heading__3GS2v').text.split('\n')[0]
    time_data = depart_flight.find_elements(By.CLASS_NAME, 'route_time__-2Z1T') # [0] : 출발시각 [1] : 도착 시각
    time_cost = depart_flight.find_element(By.CLASS_NAME, 'route_info__1RhUH')
    airport_data = depart_flight.find_elements(By.CLASS_NAME, 'route_code__3WUFO') #[0] : 출발공항 [1] : 도착 공항
    seat_data = depart_flight.find_element(By.CLASS_NAME, 'domestic_type__30RSq')
    seat_data1 = depart_flight.find_element(By.CLASS_NAME, 'domestic_txt__2YFi_')
    price_data = depart_flight.find_element(By.CLASS_NAME, 'domestic_num__2roTW')
    # price_data = depart_flight.find_element(By.CLASS_NAME, 'domestic_item__2B--k').text.split('\n')
    # price_data = depart_flight.find_element(By.CLASS_NAME, 'domestic_prices__3N88F').text.split('\n')
    flight_data['no'] = cnt
    flight_data['company'] = flight_company
    flight_data['depart_airport-code'] = airport_data[0].text
    flight_data['arrive-airport-code'] = airport_data[1].text
    flight_data['depart-time'] = time_data[0].text
    flight_data['arrive-time'] = time_data[1].text
    flight_data['time-cost'] = time_cost.text
    flight_data['seat-type'] = seat_data.text
    flight_data['price'] = price_data.text
    data.append(flight_data)
    cnt += 1
    # print('항공사 : ', flight_company)
    # print(f'여정 : {airport_data[0].text} -> {airport_data[1].text}')
    # print(f'운항 시간 : {time_data[0].text} - {time_data[1].text} 소요 시간 : {time_cost.text}')
    # print(f'좌석 정보 : {seat_data.text} {seat_data1.text} {price_data.text}원')
    # print('-'*100)
#json file로 저장
with open(path + 'flight.json', 'w', encoding='utf-8') as file:
    file.write('[')
    for idx, d in enumerate(data):
        if(idx != len(data) - 1):
            file.write(f'{{ "no" : {d['no']},"company" : "{d['company']}","depart_airport-code" : "{d['depart_airport-code']}","arrive-airport-code" : "{d['arrive-airport-code']}","depart-time" : "{d['depart-time']}", "arrive-time" : "{d['arrive-time']}","time-cost" : "{d['time-cost']}","seat-type" : "{d['seat-type']}","price" : "{d['price']}"}},\n')
        else:
            file.write(f'{{ "no" : {d['no']},"company" : "{d['company']}","depart_airport-code" : "{d['depart_airport-code']}","arrive-airport-code" : "{d['arrive-airport-code']}","depart-time" : "{d['depart-time']}", "arrive-time" : "{d['arrive-time']}","time-cost" : "{d['time-cost']}","seat-type" : "{d['seat-type']}","price" : "{d['price']}"}}')
    file.write(']')
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