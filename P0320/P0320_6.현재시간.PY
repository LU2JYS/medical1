#input을 입력받아 데이터를
#p0320.txt. 파일을 생성해서 저장하시요
#p_0320 현재날짜를 사용하시요

import datetime


# 파일 이름 정의
filename = "p0320.txt"

# 현재 날짜와 시간 가져오기
now = datetime.datetime.now()

# 파일을 쓰기 모드('w')로 열기. 파일이 이미 존재하면 내용을 덮어쓴다.

with open(filename, 'w') as file:
    # 파일에 현재 날짜와 시간을 문자열로 변환하여 쓰기
    file.write(now.strftime("%Y-%m-%d %H:%M:%S"))

# 현재 날짜와 시간 출력
print("현재 날짜와 시간 출력 :", now.strftime("%Y-%m-%d %H:%M:%S"))



