#예외-프로그램 실행시 알수없는 오류로 인한 프로그램종료를 방지하기 위해
#프로그램 애러- 프로그램 실행하면서 수정을 해야함






#try :프로그램 오류가 발생 될거같은 소스
# except : 예외 발생시 처리 구문 소스
#except Exception as e: 예외 발생시 어떤 예외가 발생이 되었는지 확인 가능
#예외 종류별로 except 처리가능
# ValueError,IndexError,ZeroDivisionError,.... 최고부모 :Exception
#print(e)
#else : 예외발생이 되지 않을 시 처리 소스
# finally : 무조건 실행되는 소스
#raise :예외를 강제로 발생 시킴>>>>> raise는 "메모내용"








print("1.학생성적입력")
print("2.학생성적출력")
print("3.학생성적수정")

num=int(input("숫자를 입력하세요>>"))
if num==1:
    print("학생성적입력 완성")
elif num ==2:
    # print("김과장이 해야 할 부분")
    raise "김과장에게 소스 받아야함" #raise: 알림, 위치를 알려준다.
elif num ==3:
    print("이대리가 해야 할 부분")
    
    
