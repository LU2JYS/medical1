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


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
url = "https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=EAIaIQobChMIo-mchMjuhQMVNGwPAh0_OAGuEAAYASAAEgKHcPD_BwE"
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source,'lxml')

trs = soup.find_all("tr", {"id": "__next"})
print("개수 : ", len(trs))

elem = browser.find_elements(By.CLASS_NAME,'HomeSearchBar_searchBoxArea__1P61S')
elem[0].click()
time.sleep(1)
# browser.switch_to.window(browser.window_handles[1])
time.sleep(1)

#날짜검색창 클릭
elem = browser.find_element(By.XPATH,'//button[@class="NavFilterButton_container__20Hr2 NavFilterButton_collapse__3JGvV SearchInput_calendarButton__3sNMZ"]')
elem.click()
time.sleep(1)

#가는날 6/5일 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]')
elem.click()
time.sleep(1)

#끝나는날 6/6일 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[5]')
elem.click()
time.sleep(2)

elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button')
elem.click()
time.sleep(2)

#검색창에 호텔넣고 엔터키 누르기
elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
elem.send_keys('호텔')
elem.send_keys(Keys.ENTER)
time.sleep(5)

for idx, yanolja in enumerate(trs):
    print(f"[ {idx+1} 번째 ]")
    
    prev_height = browser.execute_script("return document.body.scrollHeight")
    print("최초 높이:",prev_height)
    cnt = 0
    while True:
        if cnt == 5: break
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        curr_height = browser.execute_script("return document.body.scrollHeight")
        if prev_height == curr_height:
            break
        prev_height = curr_height
        print('현재 높이 :',curr_height)
        cnt += 1
        
        if all([]):  # 모든 데이터가 있을 때만 DB에 삽입
            sql = f"INSERT INTO MELON VALUES (MELON_seq.nextval, :rank, :v_rank, :img, :title, :singer, :likeNum)"
            cursor.execute(sql, {'rank': rank, 'v_rank': v_rank, 'img': img, 'title': title, 'singer': singer, 'likeNum': likeNum})
            print("DB에 저장되었습니다.")
        else:
            print("누락된 데이터가 있어 DB에 저장되지 않았습니다.")
            
cursor.execute('commit')
cursor.close()
conn.close()