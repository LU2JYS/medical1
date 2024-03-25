fruits=["딸기","사과","자몽","포도","수박","자몽"]
'''
print(fruits)
fruits.remove("자몽")
print(fruits)
'''
del(fruits[5]) #특정위치를 지워준다.
print(fruits)

for index, elem in enumerate(fruits):
    print("{}는{}번째에 있습니다.".format(elem,index))