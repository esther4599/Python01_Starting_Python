number = 20
greeting = "안녕하세요"
place = "문자열 포맷의 세계"
welcome = "환영합니다"

#old way
print(number, "손님", greeting, ",", place, "에 오신 것을", welcome, "!")

#new way
base = "{}번 손님, {}. {}에 오신 것을 {}!"
new_way = base.format(number, greeting, place, welcome)
#format = {}를 다른 값으로 변경해주는 기능. base에 포함된 기능이다.
#""를 사용하는 변수 = string
print(base)
print(new_way)

mine = "가위"
yours = "바위"
result = "졌다..."
print("나는 {}, 너는 {}, 그래서 {}".format(mine, yours, result))
# 주의 : format()의 경우 {}와 문자열의 수가 다르면 오류가 발생하기도 안하기도 함.
