import requests
from bs4 import BeautifulSoup
url="https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #text를 html파싱
# print(soup.prettify()) #html소스를 정렬해서 출력해 줌.


    
#print(soup)
num1=soup.find('p',{'class':'no1'}).text
print('베스트 순위 : ',num1)

num2=soup.find('a',{'class':'itemname'}).text
print('제목 : ',num2)

num3=soup.find('div',{'class':'s-price'}).text
print('가격 : ',num3)




