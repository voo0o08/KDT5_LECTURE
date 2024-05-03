'''
25.7 연습문제: 평균 점수 구하기
'''
maria = {"korean": 94,
         "enlish": 91,
         "math": 89,
         "science": 83}
avg = sum(maria.values())/len(maria)
print(avg)

'''
22.8 심사문제: 딕셔너리에서 특정 값 삭제하기
alpha bravo charlie dalta
10 20 30 40
'''
# keys = input().split()
keys = "ialpha bravo charlie dalta".split()
# values = map(int, input().split())
values = map(int, "10 20 30 40".split())

x = dict(zip(keys, values))

x.pop("dalta")
key30 = [k for k, v in x.items() if v == 30]
x.pop(key30[0])

print(x)
