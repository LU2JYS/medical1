f=open("k001.csv","r",encoding="utf8")
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
    f_list[4]=int(f_list[4])
    sum+=f_list[4] # 총 더하기를 해보시요>>>>>>>>>
    print(f_list[4])
print("전체 수: ",sum)    
f.close()