class Student:
    count = 1 # 클래스 변수 사용
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count  # 클래스변수 사용
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = rank
    def __str__(self): #객체를 호출하면 출력됨.
        return f"학생성적 : {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
# 파일 불러와서 저장하기
students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    # 1,홍길동,99,99,87,285,95.0,1
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()
# 파일 불러오기 한후 학생수에서 +1추가
Student.count = len(students)+1
# # 리스트 출력
# for stu in students:
#     print(stu)
while True:
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("0. 종료")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1":
        while True :
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
            if(name=="0"):
                print("학생 입력을 취소합니다.")
                break
            kor = int(input("국어점수를 입력하세요."))
            eng = int(input("영어점수를 입력하세요."))
            math = int(input("수학점수를 입력하세요."))
            # list에 추가
            s = Student(name,kor,eng,math)
            students.append(s)
            print("입력 데이터 :",s) #list -> dict












