import random

def idpw():
    eng = "abcdefghijkmnopqrstuvwxyz"
    pw="1234567890"
    
    member=[["aaa","1111"]]
    for i in range(10):
        temp1=random.choice(eng)
        temp2=random.choice(eng)
        temp3=random.choice(eng)
        tt1=temp1+temp2+temp3
        temp4=random.choice(pw)
        temp5=random.choice(pw)
        temp6=random.choice(pw)
        temp7=random.choice(pw)
        tt2=temp4+temp5+temp6+temp7
        member.append([tt1,tt2])
        
    return member

    # p_list=[]
    # for i in range(10):
    #     temp1=random.choice(pw)
    #     temp2=random.choice(pw)
    #     temp3=random.choice(pw)
    #     p_list.append(temp1+temp2+temp3)
    # print(p_list)

    # # for i in range(eng):
    # #     e_list[i]=i
    # # e_list=[[0]*3 for i in range(eng)]