selected = None # None = Null

# not in() : 안에 없으면 true, if의 경우 반복없이 한번만 실행
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중 선택하세요> ')
print(selected)

patterns = ['가위', '바위', '보']
# for pattern in patterns:
#     print(pattern)

# for i in len(patterns):
#     print(patterns[i])

length = len(patterns)
i = 0
while i < length : #여기에 for 쓰면 error, for 은 위에 닶은 형식으로
    print(patterns[i])
    i += 1