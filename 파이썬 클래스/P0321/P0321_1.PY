class Student:
    name=""
    kor=0
    
    def __init__(self,name=""):
        pass
    def stu_print(self):
        print("학생성적 출력")
        
def s_print():
    print("class밖에 있는 함수")

s= Student()
print(s)

s_print()

s.stu_print() #클래스 내에 있는 함수는 꼭 객체선언을 해야 사용가능