# raise : 사용자가 error를 직접 발생
# 많이 사용하면 코드가 복잡해진다. 꼭 필요한 경우에 사용

def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try:
    rsp('가위', '버')
except ValueError:
    print('값에 오류가 있습니다.')

school = {
    '1반' : [172, 185, 198, 177, 165, 199],
    '2반' : [165, 177, 167, 180, 191]
}

try:
    for num, s in school.items():
        for h in s:
            if h > 190:
                print(num, '에 190을 넘는 학생이 있습니다.')
                #break #1반과 2반 모두 한번씩 출력됨
                raise StopIteration #try 없이 실행하면 1반만 출력
except StopIteration:
    print('정상 종료')