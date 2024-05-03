'''
리스트 안에 모든 원소를 더한 합계 출력
'''
datas = ['1', '4', '9']

datas = list(map(int, datas))
print(datas)


datas = ['1', '4', '9']

# 원소에 *100한 값을 리스트에 저장하기
datas = list(map(lambda x: int(x)*100, datas))
print(datas)

def greeting():
    print("반갑습니다~")
greeting()

print((lambda : "반갑습니다.")())