import datetime

# 현재 날짜 가져오기
today = datetime.date.today()

# 동일한 연도의 8월 16일을 설정
end_date = datetime.date(today.year, 8, 16)

# 두 날짜 사이의 차이 계산
d_day = end_date - today

# 결과 출력
print(f"8월 16일까지는 {d_day.days}일 남았습니다.")
