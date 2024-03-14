#파일 1개 생성

#파일 오픈
file = open("memo.txt","w",encoding="utf8")
try:
    #file write
    file.write("안녕하세요1.\n")
    file.write("안녕하세요2.\n")
    print(1/0)
    file.write("안녕하세요3.\n")
    file.write("안녕하세요4.\n")
except Exception as e: #exception: 예외설명을 출력
    print("저장시 애러가 났습니다.")
    print(e)
finally:
    file.close() #예외발생시, 하지않을시에도 무조건 실행
#파일 닫기