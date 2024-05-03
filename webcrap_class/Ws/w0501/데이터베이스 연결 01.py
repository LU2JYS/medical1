import oracledb

#데이터베이스 연결
def connection():
    conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)
    return cursor

#실행
sql="select * from member"
cursor = connection()
cursor.execute(sql)
data = cursor.fetchall()

for d in data:
    print(d)

conn.close()