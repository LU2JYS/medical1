import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Launch the Chrome browser
browser = webdriver.Chrome()

# URL to navigate
url = "https://news.naver.com/main/ranking/popularDay.naver"

# Navigate to the URL
browser.get(url)


time.sleep(3)


soup = BeautifulSoup(browser.page_source, "lxml")


list_ul = soup.find("ul", {"class": "rankingnews_list"})


lis = list_ul.find_all("li")
print("-" * 40)
for li in lis:
    print("-" * 40)
    print("순위 :", li.find("em", {"class": "list_ranking_num"}).text)
    print("내용 :", li.find("div", {"class": "list_content"}).text)


browser.quit()





