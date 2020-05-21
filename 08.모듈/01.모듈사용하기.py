'''
math = 수학과 관련된 함수를 갖는 라이브러리
ex) math.pi

math 같은게 모듈이다. .~~로 해당 모듈에서 이미 만들어진 함수를 실행할 수 있음
사용하는 방법은 import 모듈명

무작위와 관련된 함수
var_name = random.choice(list_name)

인터넷에 있는 내용을 가져올 수 있음(아래 코드)
'''

def get_web(url) :
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('uft-8')
    return decoded

url = input('웹 페이지 주소?')
content = get_web(url)
# http://example.com/