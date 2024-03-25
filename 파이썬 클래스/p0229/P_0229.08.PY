member=[]
cnt=0
#이름을 입력받아서 [1.홍길동],[2.유관순]
while True:
    print("-"*35)
    print("1.입력")
    print("2.출력")
    print("3.검색출력")
    print("4.검색삭제")
    print("5.수정")
    print("0.종료")
    ch=input("원하는 번호를 입력하세요")
    print("-"*35)
    ch=int(ch)
    if ch==1:
        print("입력")
        name = input("이름을 입력하세요")
        cnt=cnt+1
        m=[cnt, name]
        member.append(m)
    
    elif ch==2:
        print("출력")
        print(member)
        print('번호\t이름')
        for s in range(len(member)):
            print("{}\t{}".format(member[s][0],member[s][1]))
    
    elif ch==3:
        print(" 검색출력")
        searchName=input("원하는 학생를 입력해주세용>>>")
        for i, stu in enumerate(member):
                if searchName in m:
                    print("{}\t{}".format(member[i][0],member[i][1]))
            
    elif ch==4:
        
        delName =input("삭제하고 싶은 학생의 이름을 입력하세요.")
        for i, m in enumerate(member):
            if delName in m:
                del(member[i])
                print("{}이 삭제 되었습니다.".format(delName))          
    
    elif ch==0:
        print("종료") 
        break
    
    elif ch==5:
        print("수정입니다") 
        rename=input("수정하고 싶은 학생의 이름을 입력하세요>>>")
        for i, m in enumerate(member):
            if rename in m:
                print(rename,"님을 선택하셨습니다.")
                ch_num=input("수정하고싶은 항목을 선택해 주세요(1. 번호수정, 2.이름수정)")
                if ch_num =="1":
                    print(rename,"님의 번호를 수정하였습니다.")
                    print(rename,"님의 이름은 ",member[i][0],"입니다")
                    stu_num =input("새로운 번호를 입력해주세요")
                    stu_num=int(stu_num)
                    member[i][0]=stu_num
                elif ch_num =="2":
                    print(rename,"님의 번호를 수정하였습니다.")
                    print(rename,"님의 이름은 ",member[i][1],"입니다")
                    stu_num =input("변경할 이름을 입력해주세요")
                    member[i][1]=stu_num
                else:
                    print("잘못입력했어")
                    pass

    else:
        print("다시입력")