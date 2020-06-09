from UnexpectedRSPValue import UnexpectedRSPValue
value = '가'
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue('가위 바위 보 중 하나의 값이어야 합니다.')
except UnexpectedRSPValue:
    print('error')

#파이썬에서는 예외도 class이다. 내가 원하는 error를 만들어 사용할 수 있다.


# 오류를 세밀하게 구분해 관리하면 오류처리가 쉽다.
def sign_up():
    '''회원가입 함수'''

try:
    sign_up()
# 다양한 오류별 처리
except BadUserName:
    print('아이디로 사용할 수 없는 입력입니다.')
except PasswordNotMatched:
    print('입력한 패스워드가 일치하지 않습니다.')