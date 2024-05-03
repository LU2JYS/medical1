import oracledb


#sql
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)


#sql 명령어>>


#프로그램을 반복하는 형태로 -누르면 정지하시요
while True:
    search=input("찾고자 하는 이름을 검색하시요")
    
    if search == '-':
        print("프로그램을 종료합니다.")
        break
    
    #검색부분 한줄일땐 f넣기
    sql=f"select * from stu_score where name like '%{search}%'"
    cursor.execute(sql)      #cursor에 select한 결과값을 저장(결과갑:list)
    data = cursor.fetchall() # fetchall()은 모든 데이터를 가져와라 . fetchone()은 1개의 데이터만 가져옴

    print("[모든 데이터 출력]")
    #print(data)
    for d in data:
        print(d)
        
    print("검색된 데이터 개수 : ",len(data))

print("프로그램을 종료합니다.")
conn.close()