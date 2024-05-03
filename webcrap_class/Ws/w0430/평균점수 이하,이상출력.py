import oracledb

#sql
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)

#평균 점수 입력받아 입력한 평균 점수 이상,이하의 학생을 출력하시요
#반복해서 진행하고 -1을 입력받으면 프로그램을 종료
while True:
    search=input("숫자를 입력해주세요 (-1 누르면 프로그램 종료)")
    
    if search == '-1':
        print("프로그램을 종료합니다.")
        break
    
    print("1. 점수이상")
    print("2. 점수이하")
    num_str=input("점수 이상 또는 이하를 선택하세요")
    if num_str =='1':
        sql=f"select * from stu_score where avg >= {search} order by no"
    else :
        sql=f"select * from stu_score where avg < {search} order by no"    
    

    cursor.execute(sql)      #cursor에 select한 결과값을 저장(결과갑:list)
    data = cursor.fetchall() # fetchall()은 모든 데이터를 가져와라 . fetchone()은 1개의 데이터만 가져옴



    print("[모든 데이터 출력]")
    #print(data)
    for d in data:
        print(d)

    print("프로그램을 종료합니다")
    conn.close()