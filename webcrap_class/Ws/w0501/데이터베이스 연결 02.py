import oracledb

#데이터베이스 연결
def close(cursor,conn):
    conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)
    return cursor

#실행
# employees이름으로 검색하는 부분 로직을 구현하시오.
# 무한반복, -1 프로그램 종료
while True:
    print("1. 이름으로 검색")
    print("2. 이름으로 같은 부서에서 근무하는 사원 조회")
    choice=input("원하는 번호를 입력하세요.>>>")
    
    if choice == '-1':
        print("프로그램을 종료합니다.")
        break
    elif choice=='1':
        search =input("이름을 입력하세요")
        sql=f"select * from employees where emp_name like '%{search}%'"
        conn,cursor = connection()
        cursor.execute(sql)
        data=cursor.fetchall()
        for d in data:
            print(d[0],end="\t")
            print(d[1],end="\t")
            print(d[4],end="\t")
            print(d[5],end="\t")
            print(d[6],end="\t")
            print(d[9])
        print("-"*30)
        close(cursor,conn)
    elif choice =='2':
        search =input("같이 근무하는 사원의 이름을 입력하세요.>>>")
        sql=f"{search}"
        print("-"*30)    
print("프로그램 종료합니다")
    