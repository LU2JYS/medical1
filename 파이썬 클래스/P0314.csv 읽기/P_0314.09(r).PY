#read

#파일열기
file=open("memo.txt","r",encoding="utf-8")


#파일읽기
content=file.read() #메모장에 있는 모든 글을 읽어옴.
content=content.strip() #<<<문자열 공백제거 strip() 
print(content)

#문자열을 쉼표로 분리하여라> type:list
stuNo,name,kor,eng,math=content.split("\n")
c_list=[0]*5
c_list[0]=int(stuNo)
c_list[1]=name
c_list[2]=int(kor)
c_list[3]=int(eng)
c_list[4]=int(math)
print(c_list)
#파일닫기
file.close()

