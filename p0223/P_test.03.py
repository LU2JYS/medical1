stu1=[1,"홍길동",100,100,100,300,100.0,1]
stu2=[2,"유관순",90,90,90,270,90.0,2]

print("-"*35)
print("[학생성적프로그램]")
print("-"*35)
print("1. 학생성적입력")
print("2. 학생성적수정")
print("3. 학생성적삭제")
print("4. 학생성적전체출력")
print("5. 학생성적검색출력")
print("6. 등수처리")
print("0. 프로그램 종료")
choice= int(input("원하는 번호를 입력하시요"))
if choice==4:
    print("4. 학생성적전체출력")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7]))
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu2[0],stu2[1],stu2[2],stu2[3],stu2[4],stu2[5],stu2[6],stu2[7]))
elif choice==6:
    print("6. 등수처리")
    print("  {}등".format(stu1[7]))
    print("  {}등".format(stu2[7]))
elif choice==1:
    print("1. 학생성적입력")
    print("{}\t{}\t{}\t{}".format(stu1[1],stu1[2],stu1[3],stu1[4]))
    print("{}\t{}\t{}\t{}".format(stu2[1],stu2[2],stu2[3],stu2[4]))
    