#strip() >>공백제거를 한다
s1="   파이      썬      "
s2="    파이썬   "
print(s1.lstrip()) #왼쪽 공백만 제거
print(s1.rstrip()) #오른쪽 공백만 제거
print(s1.strip()) #양쪽 공백 제거

#replace 빈 공백 없애기

print(s1.replace("파이","py")) #다른걸로 대채하는 시스템이다.
print(s1.replace(" ","")) #

s_input=input("배우고있는 과목은?").strip()

if s_input==s2:
    print("정답입니다")
else:
    print("틀립니다")

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다." \
    
print(news.replace(" ",""))
    





    