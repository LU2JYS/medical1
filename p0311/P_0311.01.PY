students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]

cnt = len(students)+1
# 학생번호 사용
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice=input("원하는 번호를 입력해보세요")
    print("-"*45)
    if not choice.isdigit():
        print("숫자만 입력가능합니다")
        continue
    choice=int(choice)
    
    
    
    # 1. 학생성적입력
    if choice == 1 :
        while True:
            name=input(f"(len(student)+1)안에 학생이름을 입력하세요 (0. 취소)")
            print("학생 이름을 취소합니다")
            break
        student={} #학생성적 초기화
        student["stuNo"]="S"+"{:03d}".format(cnt)
        student["name"]=name
        kor=int(input("국어성적을 입력하세요"))
        student["kor"]=kor
        eng=int(input("영어성적을 입력하세요"))
        student["eng"]=eng
        math=int(input("수학성적을 입력하세요"))
        student["math"]=math
        total=kor+eng+math
        avg=total/3
        student["avg"]=float("{:2f}".format(avg))
        students.append(student)
        cnt+=1
        print("입력데이터 : ",student)
        print(students)
        
            
        
    # 2. 학생성적전체출력
    elif choice == 2 :
        count =input("학생전체를 출력하시겠습니까? (1. 확인 0.취소)")
        if count =="0":
            break
        print("\t [ 학생성적전체 출력]")
        print("-"*45)
        print("학번\t이름\t국어\t수학\t영어\t총점\t평균")
        print("-"*45)
        for s_dic in student:
            for s_key in s_dic:
                print(s_dic[s_key],end="\t")
            print()
        print("-"*45)
        print()
            
    # 3. 학생검색
    elif choice == 3 :
        pass
        
    
    #4. 학생수정
    elif choice == 4:
        s_title=["","국어","영어","수학"]
        search=input("찾고자 하는 학생의 이름을 입력하세요. (0. 취소)")
        chk=0
        if search =="0":
            break
        for s_dic in students:
            if s_dic["name"] == search:
                break
            chk=1
            
        print("찾고자 학생의 위치 :",chk)
        
        if chk==len(students):
            print(f"{search} 학생은 없습니다. 다시입력해주세요.")
        else:    
            print(f"{search} 학생을 찾았습니다.")
            while True:
                print("[수정 할 과목을 선택하세요]")
                print("-"*45)
                print("1. 국어  2. 영어  3. 수학")
                s_input=int(input("수정할려는 과목을 선택하세요 (0. 취소 )>>"))
                if s_input ==1:
                    s_1="kor"
                    print("[{} 수정]".format(s_title[s_input]))
                    print(" 현재 {}점수 : {}".format(s_title[s_input].students[chk][s_1]))
                    print("-"*45)
                    score=int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                    students[chk][s_1]=score
                    students=[chk]["total"]=students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                    students=[chk]["avg"]=float("{:2f}".format (students[chk]["total"]/3))
                    
                    print("{}점수: {}점으로 수정이 완료 되었습니다.".format(s_title[s_input],students[chk][s_1]))
                    print(students[chk])
                    
                elif s_input ==2:
                    s_1="eng"
                    print("[{} 수정]".format(s_title[s_input]))
                    print("현재 {}점수 : {}".format(s_title[s_input].students[chk][s_1]))
                    print("-"*45)  
                    score=int(input ("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                    students[chk][s_1]=score
                    students=[chk]["total"]=students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                    students=[chk]["avg"]=float("{:2f}".format (students[chk]["total"]/3))
                    
                    print("{}점수: {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                    print(students[chk])
                    
                elif s_input ==3:
                    s_1="math" 
                    print("[{}수정]".format(s_title[s_input]))
                    print(" 현재 {}점수 : {}".format(s_title[s_input].students[chk][s_1]))
                    print("-"*45)
                    score=int(input("수정할 {}점수를 입력하세요".format(s_title[s_input])))
                    students[chk][s_1]=score
                    students=[chk]["total"]=students[chk]["kor"]+students[chk]["eng"]+students[chk]["math"]
                    students=[chk]["avg"]=float("{:2f}".format(students[chk]["total"]/3))
                    
                    print("{}점수: {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                    print(students[chk])
                    break
                
                
                    
    # 5. 등수처리
    elif choice == 5:
        for i,s_dic in enumerate(students): #순서처리를 한다
            rank_cnt=1
            for i_dic in students:
                if s_dic["rank"]<i_dic["total"]:
                    rank_cnt +=1
            s_dic["rank"]=rank_cnt
        print("등수처리가 완료되었습니다")  
        print(students)      
        
    # 6. 학생삭제          
    elif choice == 6:
        while True:
            search=input("찾고자 하는 학생의 이름을 입력하세요. (0. 취소)")
            chk=0
            if search =="0":
                break
            for s_dic in students:
                if s_dic["name"]==search:
                    break
                chk+=1
                
            print("찾고자 하는 학생의 위치:",chk)
            
            if chk>=len(students):
                print("찾고자 하는 학생이 없습니다")
            else:
                print("{} 학생을 찾았습니다".format(search))
                s_input=input("{} 학생 성적을 삭제하시겠습니까? (1. 실행 0.취소)".format(search))
                
                if s_input !="1": #1이 아니면 취소이므로 실행이 안됨..
                    print("삭제를 취소합니다")
                    break
                else:
                    del students[chk] #반대이므로 1.실행이므로 성적이 삭제가 된다...
                    print('{}학생성적이 삭제되었습니다.'.format(search))
                    print(students)
                    
                
        