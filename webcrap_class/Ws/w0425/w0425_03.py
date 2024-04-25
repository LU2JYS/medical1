import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #요소선택
from selenium.webdriver.common.keys import Keys #키워드검색
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url="https://flight.naver.com/flights/domestic/SEL-CJU-20240505/CJU-SEL-20240506?adult=1&fareType=YC"

browser=webdriver.Chrome()
browser.get(url)


























