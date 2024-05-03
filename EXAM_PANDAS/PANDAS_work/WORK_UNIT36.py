'''
36.8 연습문제: 리스트에 기능 추가하기
'''

class AdvancedList(list):
    def replace(self, old, new): # 1이 self안에 있으면 new로 바뀌는 거임... index는 list라는 class이 method...
        while old in self: # 1이 3개 라서 3번 도는 거임
            self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

print()
'''
36.9 심사문제: 다중 상속 사용하기
Animal과 날개 클래스 Wing을 상속받아 새 클래스 Bird를 작성하여 
먹다/파닥거리다/날다 True, True가 각 줄에 출력되도록
'''
class Animal:
    def eat(self):
        print("먹다")

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print("날다")
b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))