#isdigit
print("1234".isdigit()) #숫자로 치환이 가능한가  >>>>>>>>>>>>>중요
print("abc".isalpha()) #영문으로 치환이 가능한가
print("1234bc".isalpha()) #섞이면 치환 불가능    >>>>>>>>>>>>>>>>중요
print("abc".islower()) #소문자인지 판별
print("ABC".isupper()) #대문자인지 판별
print("     ".isspace()) #문자열이 공백인지/ 있으면 true   >>>>>>>>>>>>>>>>중요
print("  ABC   ".isspace()) #문자열이 있으므로 false