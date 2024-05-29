import requests
from bs4 import BeautifulSoup
url=""
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #text를 html파싱
# print(soup.prettify()) #html소스를 정렬해서 출력해 줌.

