ss="파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다"

#존재하는 문자가 몇번 나왔는지 출력
print(ss.count("공부")) #2번있다                      >>>>>>>>>>count를 많이쓴다.
print(ss.count("자바")) #없으면 0으로 출력

print(ss.find("공부")) #존재하는 열의 위치값이 출력된다.  >>>>>>>>>>find를 많이쓴다.
print(ss.find("자바")) #없으면 -1으로 출력
print(ss.find("공부",7)) #문자열 7번째 부터 검색 시작이되서 위치값이 출력된다.
print(ss.rfind("공부")) #반대쪽부터 검색위치를 알려준다.
print("-"*20)

print(ss.index("공부"))
# print(ss.index("자바")) #없으면 애러가 난다.
print(ss.index("파이썬"))
print(ss.index("재미"))
print(ss.rindex("공부")) #반대쪽부터 검색위치를 알려준다.

print(ss.startswith("파이썬")) # 맞으면 true
print(ss.startswith("자바")) # 틀리면 false

print(ss.endswith("재미")) # 마지막 문자가 틀리면 false
print(ss.endswith("않습니다")) # 마지막 문자가 맞으면 true
