import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Launch the Chrome browser
browser = webdriver.Chrome()

# URL to navigate
url = "https://jumin.mois.go.kr/ageStatMonth.do"


browser.get(url)
#서울,인천,경기도 인구를 웹스크래핑해서 
#서울 : 총인구
#인천 : 총인구
#경기도 : 총인구
#합계 : 인구

time.sleep(3)


soup = BeautifulSoup(browser.page_source, "lxml")


list_ul = soup.find("div", {"class": "tab_section current_table title_table_div"})


lis = list_ul.find_all("tr")
print("-" * 40)
for td in lis:
    print("-" * 40)
    print("서울 총인구수 : ", td.find("td", {"title": "2024년 03월 / 계"}))
    



browser.quit()





