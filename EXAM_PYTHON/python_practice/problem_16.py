'''
16. 입력받은 정수 2개에 대한 공약수를 모두 출력하는 함수를 만들어 주세요.
-약수란?
특정한 수를 다른 수로 나누었을 때, 그 나머지가 0이되는 수
-공약수란?
두 수가 공통으로 갖고 있는 약수
'''
# set 교집합
def divisor(num1, num2):
    num1set = set()
    num2set = set()
    for i in range(1, num1+1):
        if not(num1 % i):
            num1set.add(i)
    for i in range(1, num2+1):
        if not(num2 % i):
            num2set.add(i)
    print(f"{num1}과 {num2}의 약수 : {sorted(num1set.intersection(num2set))}")
n1, n2 = map(int, input("약수 구하고 싶은 수 : ").split())
divisor(n1, n2)