import oracledb


#sql
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)


#부서별  평균월급, 최대월급,최소월급을 출력

sql='''select department_id,round(avg(salary),2),max(salary),min(salary) from employees
where department_id is not null
group by department_id
order by department_id
'''

cursor.execute(sql)      #cursor에 select한 결과값을 저장(결과갑:list)
data = cursor.fetchall() # fetchall()은 모든 데이터를 가져와라 . fetchone()은 1개의 데이터만 가져옴



print("[모든 데이터 출력]")
#print(data)
for d in data:
    print(d)

conn.close()