txt="파이썬 파일 중에 a.txt 가 파이썬 폴더에 존재합니다.hwp"
print(txt.find("자바")) #없으면 -1
print(txt.find(".")) #있을때는 위치값 리턴
print(txt.count("파이썬")) #전체에 있는 갯수
print(txt.count(".py")) #없으면 0
print(txt.endswith("hwp")) # 제일 뒤에 있는단어가 일치하면 true
print(txt.endswith(".")) #제일 뒤에 있는 단어랑 일치하지 않으면 false