s = '가위'
r = '주먹'
p = '보'

win = '승리'
draw = '비김'
lose = '패배'

mine = s
yours = r

if mine == yours :
    print(draw)
elif mine == s : #else if = elif
    if yours == p :
        print(win)
    else:
        print(lose)
elif mine == r :
    if yours == s :
        print(win)
    else:
        print(lose)
else:
    if yours == r :
        print(win)
    else:
        print(lose)