money = input("교환할 돈을 입력하세요")
money= int(money)
c10000,c5000,c1000 = 0,0,0
c10000 = money//10000
c5000 = (money%10000)//5000
c1000 = ((money%10000)%5000)//1000
print("입력한금액 :{}장".format(money))
print("10000원 :{}장".format(c10000))
print("5000원 :{}장".format(c5000))
print("1000원 :{}장".format(c1000))
