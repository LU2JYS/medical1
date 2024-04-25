# https://jumin.mois.go.kr/ageStatMonth.do
# 서울특별시, 인천직할시, 경기도 3개의 인구를 웹스크래핑해서
# 서울특별시 : 인구
# 인천직할시 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오.
import requests
from bs4 import BeautifulSoup
url = "https://jumin.mois.go.kr/ageStatMonth.do"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")





#서울,인천,경기도 인구를 웹스크래핑해서 
#서울 : 총인구
#인천 : 총인구
#경기도 : 총인구
#합계 : 인구



section = soup.findAll("td",{"class":"td_admin th1"})[1]
for text in section:
    print(text.get_text())
total_p = soup.findAll("td",{"title":"2024년 03월 / 계"})[2]
for text in total_p:
    print(text.get_text())
    
    section = soup.findAll("td",{"class":"td_admin th1"})[4]
for text in section:
    print(text.get_text())
total_p = soup.findAll("td",{"title":"2024년 03월 / 계"})[3]
for text in total_p:
    print(text.get_text())
    
    section = soup.findAll("td",{"class":"td_admin th1"})[9]
for text in section:
    print(text.get_text())
total_p = soup.findAll("td",{"title":"2024년 03월 / 계"})[4]
for text in total_p:
    print(text.get_text())
    
print("-"*40)
for text in total_p:
    print("합계 :", text.get_text())





