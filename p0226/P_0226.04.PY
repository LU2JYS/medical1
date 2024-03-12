'''
stu = ["홍길동","유관순","이순신","김구","강감찬"]
print(stu[2])

stu[3]="안창호"
print(stu)

print(stu[1:])

stu.append("왕건")
print(stu)

stu.remove("홍길동")
print(stu)
'''
'''
f=["사과","복숭아","딸기","배","포도","수박"]
print(f[2])

f[4]="망고"
print(f)

print(f[3:])

print(f[1:3])

f.append("사과")
print(f)
f.append("감")
print(f)

if "수박" in f :
    print("수박이 있습니다.")
'''
'''
num=[10,20,30,40,50,]
if 60 not in num : 
    num.append(60)
    print(num)

if 20 in num:
    num.append(70)
    num.remove(20)
    print(num)
'''
'''
aa=[[1,2],[3,4]]
print(aa[0][1])
print(aa[1][1])
a1=[1,2]
a2=[3,4]
a3=[al,a2]
'''
stu1=["홍길동",90]
stu2=["유관순",100]
student=[stu1,stu2]

print(student[0])

student[0][1]="80"
print(student)

stu3= ["이순신,95"]


if student[1][1]==100:
    print("100점입니다")
