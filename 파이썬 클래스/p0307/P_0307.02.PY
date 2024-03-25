students={"stuNo":1,"stuname":"홍길동","tel":"010-1234-4567","gender":"male","id":"aaa","pw":1111}

if "studentNo" in students:
    print("key값이 없습니다.")
    students["studentNo"]=students["studentNo"]+1 #만약에 키값 없는값을 가져와서 수정을 불가능하다
    print(students["studentNo"])
else:
    print("키값이 존재하지않습니다")