# 1-100까지 더하는데 
# 총합이 100이 넘었을때 수를 출력하세요

'''
i=0
sum=0
while sum <100:
    i+=1

    continue
print(sum)
'''
sum = 0
for i in range(100):
	sum +=i
	if sum >= 100 :
		print("합이 100을 넘을 때의 합의 값 : ", sum)
		break

sum = 0
for i in range(10):
	sum +=i
	if sum >= 4 :
		print("합이 4을 넘을 때의 합의 값 : ", sum)
		break