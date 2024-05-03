import oracledb


#sql
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)


#employees에서 사번 이름 월급 실제 수령금액(월급+(월급*커미션)),월급*1410 원화로 계산해서 출력
#1000단위 표시해서 출력하시요

sql='''select employee_id,emp_name,salary,
salary+(salary*nvl(commission_pct,0)),
to_char(salary*1410,'L999,999,999') from employees
'''

cursor.execute(sql)      #cursor에 select한 결과값을 저장(결과갑:list)
data = cursor.fetchall() # fetchall()은 모든 데이터를 가져와라 . fetchone()은 1개의 데이터만 가져옴

print("[모든 데이터 출력]")
#print(data)
for d in data:
    print("-"*45)
    print("사원번호 : ",d[0])
    print("이름 : ",d[1])
    print("월급 : ",d[2])
    print("실수령 월급 : ",d[3])
    print("월급(원화) : ",'￦'+d[4].strip())
print("-"*45)
conn.close()