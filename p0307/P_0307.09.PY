# list=[
#     [0,0,0],[0,0,0],[0,0,0]
# ]

# 일차원 리스트에 1-9까지 입력하세요
list=[]
for i in range(9):
    list.append(i+1)
print(list)

list2=[n for n in range (9)]
print(list2)

list3=[[0]*3 for n in range(3)]
print(list3)

numList =[num*num for num in range(1,6)] #제곱근 이다.
print(numList)







#1-9까지 2차원 리스트에 숫자를 넣으세요
# [1,2,3]
# [4,5,6]
# [7,8,9]
# a_lists=[]
# for i in range(3):
#     a_list=[]
#     for j in range((3*i)+j+1):
#         a_list.append(j) #[0,1,2]
#     a_lists.append(a_list) #[0,1,2] ,[0,1,2] ,[0,1,2] 

# print(a_lists)



# for i in list:
#     for f in i:
#         print(f,end="\t") 
#     print()