import requests
from bs4 import BeautifulSoup

url = "https://jumin.mois.go.kr/ageStatMonth.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 서울특별시, 인천직할시, 경기도
population_seoul = soup.find_all("td", {"class": "td_admin th1"})[1].get_text()
total_seoul = int(soup.find_all("td", {"title": "2024년 03월 / 계"})[2].get_text().replace(",", ""))

population_incheon = soup.find_all("td", {"class": "td_admin th1"})[4].get_text()
total_incheon = int(soup.find_all("td", {"title": "2024년 03월 / 계"})[3].get_text().replace(",", ""))

population_gyeonggi = soup.find_all("td", {"class": "td_admin th1"})[9].get_text()
total_gyeonggi = int(soup.find_all("td", {"title": "2024년 03월 / 계"})[4].get_text().replace(",", ""))


print( population_seoul, total_seoul)
print( population_incheon, total_incheon)
print( population_gyeonggi, total_gyeonggi)


total_population = total_seoul + total_incheon + total_gyeonggi

print("-" * 40)
print("합계:", total_population)


# tds = trs[1].find_all("td")
# kg=tds[2].text()
# print("서울 인구수 : ",kg)

# tds = trs[4].find_all("td")
# kg=tds[2].text()
# print("인천 인구수 : ",kg)


# tds = trs[9].find_all("td")
# kg=tds[2].text()
# print("경기도 인구수 : ",kg)


