import pandas as pd
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
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
# # list 타입 저장
# list1 = []
# list1.append(10)
# list1.append(20)
# list1.append(30)
# list1.append(40)
# # dict 타입 저장
# m_dict = {}
# m_dict['viewer']=list1
# print(m_dict)
# year, title , viewer, rating
m_dict = {}
year_list = []
title_list = []
viewer_list = []
rating_list = []
print('-'*60)
for year in range(2019,2024):
    print("연도 : ",year)
    year_list.append(year)
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,"lxml")
    # year = browser.find_element(By.XPATH,f"//a[text()={year}]")
    # time.sleep(2)
    # year.click()
    movie_list = soup.find("div",{"class":"pdt2"})
    # 제목
    title = movie_list.find("strong",{"class":"tit-g clamp-g"}).text.strip()
    print("영화제목 : ",title)
    title_list.append(title)
    # 관객 수
    viewer = movie_list.find("p",{"class":"conts-desc clamp-g"})
    viewer = int(viewer.text.strip()[3:-2].replace(",",""))
    print("관객수 : ",viewer)
    viewer_list.append(viewer)
    # 영화 제목 찾아 클릭
    # elem = browser.find_element(By.XPATH,'//*[@id="mor_history_id_0"]/div/div[1]/div/div[1]/c-flicking-item/c-layout/div/c-list-doc/ul/li[1]/c-doc/div/div[2]/div[1]/c-title/strong')
    elem = browser.find_elements(By.XPATH,'//strong[@class="tit-g clamp-g"]')[0]
    time.sleep(2)
    elem.click()
    time.sleep(2)
    # 평점
    rating = browser.find_element(By.CLASS_NAME,'gem-star-point')
    rating = float(rating.text[2:5])
    print("평점 : ",rating)
    rating_list.append(rating)
    
# print(year_list)
# print(title_list)
# print(viewer_list)
# print(rating_list)

#dict 저장
m_dict['year'] = year_list
m_dict['title'] = title_list
m_dict['viewer'] = viewer_list
m_dict['rating'] = rating_list
print(m_dict)
df = pd.DataFrame(m_dict)
print(df)
