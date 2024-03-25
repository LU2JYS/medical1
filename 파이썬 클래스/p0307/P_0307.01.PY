# 딕셔너리 
student={"stuNo":1,"stuname":"홍길동","kor":100} #앞에 있는걸 key 뒤에있는걸 value
'''
list=[1,2,3]
list.append(4) #>>>>>>>>>>>>>>>>추가
print(list)
del list[0]   #>>>>>>>>>>>>>>>>삭제
print(list)
list[0]=100   #>>>>>>>>>>>>>>>>수정
print(list)
list[2]=1000
print(list)
'''

student["eng"]=100 #>>>>>>>>>>>>>없는걸 넣으면 추가
print(student)

student["kor"]=50  #>>>>>>>>>>>>있는걸 넣어주면 수정이 된다.
print(student)

del student["stuname"] #>>>>>>>>특정 부분만 삭제
print(student)

# 타입 list, dict,int,float,str
print(list(student.keys())) #>>>>>>>>>딕셔너리에 키값만 추출
print(list(student.values()))  #>>>>>>>>>딕셔너리에 value값만 추출
print(list(student.items())) #>>>>>>>>>딕셔너리에 키,value값 둘다 추출

#토플 : 수정,삭제가 불가능!!!!!!!!!!

