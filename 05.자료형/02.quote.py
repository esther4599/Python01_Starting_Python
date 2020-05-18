string1 = "some txt"
string2 = "어떤 텍스트"
string3 = "{}도 {}도 지금 이것도 문자열".format(string1, string2)
#추상적 = 텍스트, 프로그램에서 = 문자열 이라고 부를 예정

print(string1, string2, string3)
# "", ''은 큰 차이가 없다.
# 한국어의 경우 인용문 출력시 '블라블라 "" 블라블라'라고 작성하기
# => "~~""~~" => 문자열이 중간에 끊겨서 인식

long_string = '''어쩌다가 긴 문장을 입력하면
이렇게 이렇게 길어지면 
어떻게 출력될까?'''
print(long_string)