'''
10. 숫자와 콤마로만 이루어진 문자열 data가 주어지면 이때, data에 포함되어있는 자연
 수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
'123,42,98,18'
'1,234'
'''
def sumMinMax():
    data = input("data=")
    dataList = [int(i) for i in data if i.isdigit()]
    #     cnt = numList.count(2)
    print(f'"{data[1:-1]}"의 합 : {sum(dataList)}, 가장 큰 수 : {max(dataList)}, 가장 작은 수 : {min(dataList)}')

sumMinMax()
