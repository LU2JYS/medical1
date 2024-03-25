#다른 파일에 있는 함수를 사용할때
#import math >>사용방법 math,floor() 이름, 함수명()
# from math import * #이름 생략가능
# # import lotto:
# from lotto import *


import math as m # 모듈명을 줄여서 사용가능. 별명(약어)부여
import lotto as lo




# l=[0]*45
# # while True:
# #     lotto.screen()
# lo.screen(1)
# lo.num_generate(l)


#>>>>>>>>>>>>>>>>>>>>>>>알아둬

# #  ceil-올림 >>>>무조건 올려줌
# print(m.ceil(12.2)) 

# #  floor -버림
# print(m.floor(12.9))

# # round- 반올림
# print(m.round(12.6))




print(dir(m))