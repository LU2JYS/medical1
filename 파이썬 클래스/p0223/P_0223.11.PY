# list
# 대괄호 안에 감싸서 나타내며 0개 이상의 원소가 저장될수있습니다.
num=1
num=2
print(num)

listA =[1,2]
listB =[]

n1=1
n2=2
n3=3
n4=4
n5=5

list1 = [1,2,3,4,5]
list2 = ["사과","복숭아","포도","멜론","딸기"]
#           0      1       2      3     4
#           -5      -4     -3      -2     -1
#python의 경우 여러형태의변수를 섞어서 사용할수있다.
list3 = [1,"홍길동",100.0001]# 문자 정수 실수를 넣을수 있다.

print(list1[4])
print(list2[2])
print(list3[2])
print(list1[-1]) #-1하면 마지막꺼를 출력을 도와준다

# 리스트의 길이를 출력 >>>나중에 반복문에서의 범위를 알고싶을때 바로바로 길이를 파악해서 출력가능
a=len(list2)
print(a)
print(len(list2))

#딸기을 출력해보세요

print(list2[4])
print(list2[-1])
print(list2[len(list2)-1])

#리스트 슬라이싱
aa=[0,1,2,3,4,5,6,7,8,9,10]
#   0 1 2 3 4 5 6 7 8 9 10
print(aa)
print(aa[1:4]) #1이상 4미만
print(aa[1:8]) #3이상 8미만
print(aa[2:]) #2번부터 끝까지
print(aa[:7]) #처음부터 7미만까지
print(aa[:]) #처음부터 끝까지
print(aa[1:-1]) #1이상 끝바로앞까지 가져오깅

#요소확인 : 내부에 포함되어 있는지 확인되는 방법을 제공해줌
# in, not in
print("포도" in list2)
print(11 in aa) #존재 하냐 판별!
print(0 not in aa) #존재 하지 않을때...

listC= [1,2,3,["a","b","c"],[4,5]]

print(listC[0])
print(listC[3])
print(listC[4])
print(1 in listC)
print(4 in listC)
print([4,5] in listC)
