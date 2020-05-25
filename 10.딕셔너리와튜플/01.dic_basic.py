#wintable = 승리조건을 조장해둔 dictionary
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}
#HashMap과 유사. 앞에 적힌 부분은 key, 뒤에는 value
#print(wintable['가위']) #검색은 key 값으로

words = ['a','b','c']
#print(words[1]) #list는 검색을 index num으로 한다.

def rsp(mine, yours) :
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours :
        return 'win'
    else :
        return 'lose'
result = rsp('가위', '바위')

masseges = {
    'win' : '승리',
    'lose' : '패배',
    'draw' : '비겼다'
}

print(masseges[result])

dict = {
    "name" : [1,2,3]
}

print(dict['name'])
