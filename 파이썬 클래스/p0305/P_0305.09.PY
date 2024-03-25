#학번은 1000, 이름 홍길동 학과 컴퓨터공학과
#딕셔너리
student={"학번":1000,"이름": "홍길동","학과": "컴퓨터 공학과"}
for key in student:
    print("{} : {}".format(key,student[key]))
#print(student)
print("-"*50)
#연락처 추가하기
student["연락처"]="010-1234-4678"
print(student)

#수정하는법>>>>>>>>>>>>>>>>>>>>>>
student["이름"]="유관순"
print(student)

student["학과"]="화학과"
print(student)

# 다른 방법이 있다>>>>>>>>>>>>>>>>>>>>>>>>
print(student["이름"]) #key의 value값 출력
print(student.get("이름"))
# print(student["성별"]) #key 값이 없어서 에러
print(student.get("성별")) #key 값이 없을때 none, 에러가 안난다.>>>>>>>>>>>>

if "이름" in student:
    print("이름 키값을 가진다.")
    print("이름:",student["이름"])
else:
    print("이름 키값이 없습니다.")
    
if "성별" in student:
    print("성별 키값이 있습니다")
    print(student["성별"])
else:
    print("성별 키값이 없습니다.")
    
for i in student.keys():
    print(i)
#student.keys() 딕셔너리의 모든 key를 출력>>>>>중요!!!!!!!!!!!!!
print(type(student.keys()))
print(student.keys())
print(list(student.keys())) #형변화을 해야 리스트 타입으로 변환됨
print("-"*60)

#student.values() 딕셔너리의 모든 value를 출력
print(student.values())
print(list(student.values()))

for i in student.values():
    print(i)
    
#items() 튜플형태로 데이터를 리턴 >>>수정이나 삭제가 안된다.
print(student.items())

if "이름" in student:
    print("키값이 있습니다.")
else:
    print("키값이 없습니다")

