import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #요소선택
from selenium.webdriver.common.keys import Keys #키워드검색
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url="https://www.naver.com/"

browser=webdriver.Chrome()
browser.get(url)

#요소선택,문자입력,엔터키,클릭,스크롤이동, 마우스 이동
elem=browser.find_element(By.ID,'query')
elem.send_keys('네이버항공권')
elem.send_keys(Keys.ENTER) #input박스에 엔터키 누르는것이다

time.sleep(3)



#네이버항공권더보기
elem=browser.find_element(By.CLASS_NAME,'main_title')
elem.click()
time.sleep(3)



#가는날 클릭
elem=browser.find_element(By.CLASS_NAME,'select_code__d6PLz')
elem.click()
time.sleep(3)

elem=browser.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF')
elem.send_keys('김포')
elem.send_keys(Keys.ENTER)

























