class Student:
    name=""
    total=0
    def  __init__(self,name,total):
        self.name=name
        self.total=total
    def __str__(self):
        return f"이름 : {self.name}, 총점 : {self.total}"
    
    def __del__(self):
        return "클래스가 소멸될때 실행" 
    
    def __add__(self,s):
        return self.total+s.total
    
    def __gt__(self,s): #크거나 같다라고 비교할때 #비교기준이 없다
        return self.total >s.total
    
    def __eq__(self,s): #크거나 같다라고 비교할때 #비교기준이 없다
        return self.name == s.name and self.total == s.total
#----------       
s1= Student("홍길동",100)
s2= Student("유관순",90)
s3= Student("이순신",95)
s4= Student("홍길동",100)
    
print(s1)  #클래스를 출력 할때, str함수 호출

print(s1+s2) #클래스를 더하기 할때, add함수 호출

print(s1>s2) #비교 기준을 정의 해줘야함
print(s2>s3)

print("s1==s4 : ",s1==s4) #둘이 비교를 해준다.
print("s2==s3 : ",s2==s3)




    