import oracledb


#sql
conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #db와 연결되어 지시자 생성(명령어를 기다린다.)

# stu_score에서 avg가 90점이상은A ,80점은 B, 70점은 C,60점 미만은F
# 학번 이름 합게 평균 학점 출력하시요

# sql='''select name,avg, case
#     when avg>=90 then 'A'
#     when avg>=80 then 'B'
#     when avg>=70 then 'C'
#     when avg>=60 then 'D'
# ELSE 'F'
# END AS grade
# from stu_score
# '''

sql="select * from stu_score"
#평균을 가지고 파이썬에서 프로그램을 학점을 출력하시요
#학번,이름,합계,평균,학점을 프로그램을 출력하시요



cursor.execute(sql)      #cursor에 select한 결과값을 저장(결과갑:list)
data = cursor.fetchall() # fetchall()은 모든 데이터를 가져와라 . fetchone()은 1개의 데이터만 가져옴

print("[모든 데이터 출력]")
    
for d in data[:5]:
    print("_"*45)
    print("학번 : ",d[0])
    print("이름 : ",d[1])
    print("합계 : ",d[5])
    print("평균 : ",d[6])
    if d[6]>=90:
        print("grade : ","A")
    elif d[6]>=80:
        print("grade : ","B")
    elif d[6]>=70:
        print("grade : ","C")
    elif d[6]>=60:
        print("grade : ","D")  
    else:
        print("grade : ","F")     

    
print("_"*45)
print("타입 : ",type(data))
#---------------------------------------------

#셀러리 평균을 찍어보세요
sql="select round(avg(salary),2)as salary from employees"
cursor.execute(sql)      
data = cursor.fetchone()
print(data[0])

conn.close()