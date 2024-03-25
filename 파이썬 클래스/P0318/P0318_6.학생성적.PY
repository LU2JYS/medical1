class Student:
    stuNo=0
    stu_name= ""
    kor=0
    eng=0
    math=0
    total=0
    avg=0
    rank=0
    
    def __init__(self,stuNo=0,stu_name= "",kor=0,eng=0,math=0,total=0,avg=0,rank=0): #둘다 된다
        self.stuNo=stuNo
        self.stu_name=stu_name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=total/3
        self.rank=0
        
        
c1=Student(1 , "홍길동" , 99 , 99 , 87 , 285 , 95 , 1)
c2=Student(2 , "유관순" , 98 , 93 , 87 , 278 , 92 , 3)
c3=Student(3 , "이순신" , 88 , 76 , 30 , 194 , 64 , 6)      

print(c1.stuNo,",",c1.stu_name,",",c1.kor,",",c1.eng,",",c1.math,",",c1.total,",",c1.avg,",",c1.rank)
print(c2.stuNo,",",c2.stu_name,",",c2.kor,",",c2.eng,",",c2.math,",",c2.total,",",c2.avg,",",c2.rank)
print(c3.stuNo,",",c3.stu_name,",",c3.kor,",",c3.eng,",",c3.math,",",c3.total,",",c3.avg,",",c3.rank)
#홍길동,김유신,이순신


c1=Student()
c1.stuNo=1
c1.stu_name="홍길동"
c1.kor=99
c1.eng=99
c1.math=87
c1.total=c1.kor+c1.eng+c1.math
c1.avg=c1.total/3
c1.rank=1
print(c1.stuNo,",",c1.stu_name,",",c1.kor,",",c1.eng,",",c1.math,",",c1.total,",",c1.avg,",",c1.rank)

c2=Student()
c2.stuNo=2
c2.stu_name="유관순"
c2.kor=98
c2.eng=93
c2.math=87
c2.total=c2.kor+c2.eng+c2.math
c2.avg=c2.total/3
c2.rank=3
print(c2.stuNo,",",c2.stu_name,",",c2.kor,",",c2.eng,",",c2.math,",",c2.total,",",c2.avg,",",c2.rank)

c3=Student()
c3.stuNo=3
c3.stu_name="이순신"
c3.kor=88
c3.eng=76
c3.math=30
c3.total=c3.kor+c3.eng+c3.math
c3.avg=c3.total/3
c3.rank=6
print(c3.stuNo,",",c3.stu_name,",",c3.kor,",",c3.eng,",",c3.math,",",c3.total,",",c3.avg,",",c3.rank)