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

url = f"https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(4)

# text소스를 html소스로 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

trs = soup.find_all("tr", {"id": "lst50"})
print("개수 : ", len(trs))

for idx, music in enumerate(trs):
    print(f"[ {idx+1} 번째 ]")
    
    rank_element = music.find("span", {"class": "rank"})
    rank = rank_element.text.strip() if rank_element else None
    print("순위 : ", rank)

    v_rank_element = music.find("span", {"class": "rank_wrap"})
    v_rank = v_rank_element['title'] if v_rank_element else None
    if v_rank == "순위동일":
        v_rank = 0
    else:
        v_rank = 1
    print("순위변동 : ", v_rank)

    img_element = music.find("img")
    img = img_element['src'] if img_element else None
    print("이미지 : ", img)

    r_title_element = music.find("div", {"class": "ellipsis rank01"})
    title = r_title_element.find("a").text.strip() if r_title_element else None
    if title:
        print("제목 : ", title)

    r_singer_element = music.find("div", {"class": "ellipsis rank02"})
    singer = r_singer_element.find("a").text.strip() if r_singer_element else None
    if singer:
        print("가수 : ", singer)

    r_likeNum_element = music.find("button", {"class": "button_etc like"})
    likeNum = r_likeNum_element.find("span", {"class": "none"}).nextSibling.strip().replace(',', '') if r_likeNum_element else None
    if likeNum:
        print("좋아요 수 : ", likeNum)
        
    # DB저장
    if all([rank, v_rank, img, title, singer, likeNum]):  # 모든 데이터가 있을 때만 DB에 삽입
        sql = f"INSERT INTO MELON VALUES (MELON_seq.nextval, :rank, :v_rank, :img, :title, :singer, :likeNum)"
        cursor.execute(sql, {'rank': rank, 'v_rank': v_rank, 'img': img, 'title': title, 'singer': singer, 'likeNum': likeNum})
        print("DB에 저장되었습니다.")
    else:
        print("누락된 데이터가 있어 DB에 저장되지 않았습니다.")

    print("-" * 30)

print("-" * 30)

cursor.execute('commit')
cursor.close()
conn.close()










