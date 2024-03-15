import P0315_2

member=P0315_2.idpw()
print(member)

#mem.txt 파일에
#aaa,1111 저장하시요

#파일열기
file =open("mem.txt","w",encoding="utf-8")
#파일쓰기

for m in member:
    file.write("{},{}\n".format(m[0],m[1]))

#파일닫기
file.close()
print("파일이 저장되었습니다.")
