import os 

# 파일생성 방법1
f= open("students.txt","w",encoding="utf-8")
f.write("1, '홍길동', 100, 100, 99, 299, 99.67,1\n")
f.write("2,'유관순',98,93,87,278,92.67,3")
f.close() #파일닫기

# f.close() #파일 닫기를 꼭해야한다.

# # 파일생성 방법2 >>>>>>>>>>>>>with사용하면 f.close() 사용하지 않아도됨
# with open("student.txt","w") as f:
#     f.write("1, '홍길동', 100, 100, 99, 299, 99.67,1")

#파일 읽어오기    
t_list=[]
out_f=open("student.txt","r",encoding="utf-8")  
while True:
    txt = out_f.readline()        #한줄씩 읽어온다
    # print(type(txt))
    if txt=="":
        break
    print(txt,end="") 
    t_list.append(txt)
print()   
print(t_list)

#파일 삭제
os.remove('students.txt')
        
    
    
    
    
    
    
    
    
#폴더가 존재하는지 확인 방법
# if not os.path.exits("hello"):
#     os.mkdir("hello")
# else:
#     os.rmdir("hello")
    

