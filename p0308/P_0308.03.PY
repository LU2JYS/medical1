# [0],[0],[0].....52개를 을 생성하세요





aa=[[0]*1]*52 #얕은복사이다 쓸수없음
bb=[[0]*2 for i in range(52)]

cc=[] #>>>>>>>>>>>>>>중요
for i in range(52):
    dd=[]
    for i in range(2):
        dd.append(0)
    cc.append(dd)
print(cc)
        






# #1차원 배열
# # [0,0,0,0,00,0,0,0,0,0,0........52개를 생성하세요]
# a_list=[0]*52
# c_list=[0 for i in range(52)]

# b_list=[]
# for i in range(52):
#     b_list.append(0)
    
# print(a_list)
# print(b_list)
# print(c_list)
    