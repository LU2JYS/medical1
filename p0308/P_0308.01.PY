# list=[]
# #1에서 10까지들어가는
# for i in range(1,11):
#     list.append(i)

#컴프리헨션 방법    >>>>>속도가 제일 빠르다......
list=[i for i in range(1,11)]
print(list)

list=[0]*10 #공간을 미리 만들어놓고 넣는다.
for i in range(0,10):
    list[i]=i+1
print(list)



    
    