#str.txt 파일의 내용을 모두 출력하시요


#중요!!!다른파일에 있는 내용을 퍼와서 다른파일을 생성해서 붙여넣기



#파일읽기
f=open("str.txt","r",encoding="utf8")

#파일 오픈
while True:
    content=f.readline()
    if content.strip()=="": break #공백있으면 끝내라!! 공백지우기는 >> strip
    print(content,end="")
#파일닫기
f.close()


#str.txt 파일의 내용을 읽어와서

#str1.txt에 그 내용을 추가해보세요
f=open("str.txt","r",encoding="utf8")
ff=open("str1.txt","a",encoding="utf8")

while True:
    content = f.readline() #파일 내용을 읽어오기
    if content.strip()=="":break
    ff.write(content)      #파일 내용추가하기
f.close()    
ff.close()


