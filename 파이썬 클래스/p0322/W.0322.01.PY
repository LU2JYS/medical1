import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup)
s_all = soup.find("div",{"class":"box_type_l"}) #큰 틀부터 들고온다
tr_list = s_all.find_all("tr") #안에 정보를 다 가져온다


#----------
for i in range(2,15):
    print("-"*50)
    stock = tr_list[i]#삼성은 tr리스트에 3번째에 존재
    td_list = stock.find_all("td")  #삼성의 td리스트를 다 가져온다
    if len(td_list) == 1 : continue
    
    print("순위 : ",td_list[0].text) #td리스트의 첫번째는 순위.text
    print("종목명 : ",td_list[1].find("a").text) #td리스트안에 두번째에 "a"의텍스트만 찾아줘
    print("검색비율 : ",td_list[2].text)
    print("현재가 : ",td_list[3].text)
    print("PER : ",td_list[10].text)
    print("ROE : ",td_list[11].text)
    
    print("-"*50)
