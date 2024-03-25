import requests

#웹에 접근해서 html에 있는 소스를 가져옴.
# res=requests.get("https://www.google.com/")
# res=requests.get("https://www.daum.net/")
res=requests.get("https://www.melon.com/index.htm")
#200코드는 정상이다.  403,404 : 페이지 없음  500: 프로그램 에러
# 2xx(성공) : 요청을 성공적으로 받았으며 인식했고 수용하였습니다.
# 4xx(클라이언트 오류) : 요청의 문법이 잘못되었거나 요청을 처리할 수 없습니다.(자기 잘못)
# 5xx(서버 오류) : 서버가 명백히 유효한 요청에 대한 충족을 실패했습니다.(상대방 잘못)

print(res) #코드상태를 출력
print("코드 : ",res.status_code)
res.raise_for_status() #코드가 200이 아니면 오류처리해서 자동 멈춤
if res.status_code == requests.codes.ok:
    print("정상페이지 호출입니다.")
else:
    print("애러 코드발생")



#requests를 통해 html소스를 출력
print(res.text)