import requests
from bs4 import BeautifulSoup
url="https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&sca_esv=125395e02bc1fefe&sca_upv=1&ei=WwQiZrvdGJ-r0-kP-K2C8A4&udm=&ved=0ahUKEwj79u73yM2FAxWf1TQHHfiWAO4Q4dUDCBA&uact=5&oq=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&gs_lp=Egxnd3Mtd2l6LXNlcnAiDu2ZmOycqCAx64us65-sMgoQABiABBhGGIICMgUQABiABDIEEAAYHjIGEAAYHhgPMgYQABgFGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMhYQABiABBhGGIICGJcFGIwFGN0E2AEBSOUMUMsCWKMKcAF4AZABAJgBY6ABgAWqAQE3uAEDyAEA-AEBmAIHoALvBMICChAAGLADGNYEGEfCAgsQABiABBixAxiDAcICChAAGIAEGEMYigXCAgQQABgDwgIIEAAYgAQYogSYAwCIBgGQBgq6BgYIARABGBOSBwMzLjSgB-cj&sclient=gws-wiz-serp"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #text를 html파싱
# print(soup.prettify()) #html소스를 정렬해서 출력해 줌.
with open('google.html','w',encoding="utf8") as f:
    f.write(soup.prettify())
    



print(soup.find('title').text) #해당 타이틀 모두 출력시키기
print(soup.title.text) #같은방식이다

#해당태그의 특정송성값 1개 출력
print("미국 (달러) : ",soup.find("input",'lWzCpb ZEB7Fb').attrs['value'],"달러")

print("대한민국 (원) : ",soup.find("input",'lWzCpb a61j6').attrs['value'],"원")
