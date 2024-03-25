class Student:
    stucount = 0 #클래스변수 #저장장소가 하나이므로 공통이다.
    stuNo = 0 #인스턴스 변수
    
    
        #생성자:__init__
        #클래스에 대해 객체선언
    def __init__(self,stu_name= "",kor=0,eng=0,math=0): #둘다 된다 #매개변수가 들어있다.
        self.stu_name=stu_name
        
        if kor>100:
            self.kor=100
        else:
            self.kor=kor #100점 초과점수 불가능하는방법~
        
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg="{:.2f}".format(self.total/3)
        self.rank=0
        Student.stucount +=1
        self.stuNo = Student.stucount
        
    def s_print(self):
        print(self.stuNo,self.stu_name,self.kor,
            self.eng,self.math,self.total,self.avg,self.rank,sep="\t")
    def __str__(self):
        return f"{self.stuNo},{self.stu_name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"


#홍길동 학생의 성적 넣기
s1=Student("홍길동",100,100,99) #매개변수가 있는 객체(인스턴스)선언
# s1.s_print()    
        
s2=Student("유관순",99,99,99)
# s2.s_print()  

print(s1) # __str__함수호출 없으면 주소값 출력
print(s2)