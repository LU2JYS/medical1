

#파일복사하기>>>>>>>>>>>>>>>>>>>>>>>해보자

#파일 열기
in_file=open("C:/workspace/medical1/mem.txt","rb")
out_file=open("C:/a/m1.txt","wb")

#파일 읽기 쓰기
while True:
    bin =in_file.read(1)
    if not bin: break
    out_file.write(bin)

#파일 닫기
in_file.close()
out_file.close()
print("복사가 완료되었습니다.")
    