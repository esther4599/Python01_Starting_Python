import my_module

selected = my_module.random_rsp()
print(selected)
print('가위?', my_module.SCISSOR == selected)

'''
맥북 기준
만약 만든 모듈이 import가 안된다면 메뉴에서 pycharm > preferences > project structure
에서 해당 모듈이 존재하는 파일 선택 > 우측 클릭 > sources 선택
'''