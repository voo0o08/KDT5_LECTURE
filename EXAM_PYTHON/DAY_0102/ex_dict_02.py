# ----------------------------------
# 다양한 dict 자료형 => key:value <- 데이터 덩어리
# - key로 데이터를 찾기/읽기/삭제/변경
# key는 중복 xxxxxxxxxxxx
# ----------------------------------

# 이름, 점수 저장하기
jumsuDict = {'hong': 100, 'Park': 98, 'Kim': 88, 'hong': 50, 'hong': 77}
print(jumsuDict) # 중복된 'hong' 중 제일 마지막 hong이 들어감

# jumsuDict = {['hong', 1]: 100, ['Park',3]: 98, ['Kim', 1]: 88, ['hong', 4]: 50, ['hong', 2]: 77}
# key값이 변경 가능하면 안되기때문에 튜플로 해야함
jumsuDict = {('hong', 1): 100, ('Park',3): 98, ('Kim', 1): 88, ('hong', 4): 50, ('hong', 2): 77}
# key값 데이터 타입 통일 안해도 됨

# 공 딕셔너리 생성
emDict = {} # bool 타입이면 0
print(f'{type(emDict)}, {len(emDict)}개')