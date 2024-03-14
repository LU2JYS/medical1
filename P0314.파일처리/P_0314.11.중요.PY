#파일 읽어오기

#1.파일 열기
#read() : 모든 문자열을 가져옴.
#reasline() : 1줄씩 가져옴.
#readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴.
#3. 파일 닫기
import os
if os.path.exists("str.txt"):

    # 모두불러오기>>>>>>>>>>>>>>
    with open("str.txt","r",encoding="utf8") as f: #변수명을 뒤에 씀
        txt_list=f.readlines() #리스트타입으로 저장
        
        for txt in txt_list:
            print(txt,end="")
        print()
    #f.close()생략 가능하다
else:
    print("파일이 존재하지 않습니다.")







# f=open("str.txt","r",encoding="utfp")
# txt_list = f.readlines()

# print(txt_list)
# print(txt_list[0])
# f.close()







# f = open("str.txt","r",encoding="utf8")
# while True:
#     txt = f.readline() #한줄씩만 넘어온다
#     if txt != "": break
    
    
#     print(txt)
    
# print("모든 파일을 읽어 왔습니다.")

