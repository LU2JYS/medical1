# 숫자6개를 입력받아 출력하세요
#1.숫자를 5개 입력 #변수는 하나일때 하나만 쓰는게 좋다
#2. 숫자를 5개 출력
'''
nums=[]
for i in range(0,5):
    nums.append(int(input("숫자를 입력하세요"))) #input타입은 스트링 타입이다.
#5개의 합을 구하시요
sum =0
for num in nums:
    sum+=num
    print("합계:",sum)
'''
#2명의 학생의 이름 국어 영어 수학을 입력받아
# #>>> 하나의 그룹핑으로 가자는 식으로하자!!!
# 합계를 구하시요
students=[]
cnt=0
for i in range(0,2):
#kor=int(input("국어점수를 입력하세요>>>"))
    student=[]
    name =input("이름을 입력해주세요")
    if name=="-1":
        break
    cnt+=1
    student.append(cnt)
    student.append(name)
    student.append(input("이름를 입력하세요>>>>"))
    student.append(int(input("국어 점수를 입력하세요>>>>")))
    student.append(int(input("영어 점수를 입력하세요>>>>")))
    student.append(int(input("수학 점수를 입력하세요>>>>")))
    sum=student[2]+student[3]+student[4] #student[0]=이름
    student.append(sum)
    student.append(student)
print(student)
print(students)



#전체학생 출력
print("[학생성적 출력]")
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
                
for stu in students:
    for s in stu:   
        print(s,end="\t")
        print() 

