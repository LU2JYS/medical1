#medical_1을 읽어와서 출력하시요
#특정 선택만해서 총 합계를 해보시요
f=open("medical_1.csv","r",encoding="utf8")
f_list=[]
cnt=0
sum=0
while True:
    content =f.readline()
    if cnt ==0:
        cnt+=1
        continue
    f_list = content.split(",")
    if content=="": break
    f_list[1]=int(f_list[1])
    sum+=f_list[1] # 총 더하기를 해보시요>>>>>>>>>
    print(f_list[1])
print("전체 수: ",sum)    
f.close()