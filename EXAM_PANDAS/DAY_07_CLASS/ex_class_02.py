'''
자동차 클래스
클래스 명 : Car
클래스 속성 : 바퀴, 색상, 차번호, 차종류, 무야호, 제조사(유일한 클래스 속성 나머지는 인스턴스 속성)
            12 / 빨강 / 1111 / 새단 / 현대
            15 / 노랑 / 6481 / SUV / 현대
클래스 기능 : 주행한다, 정지한다, 후진한다
'''
class Car:
    # 클래스 속성
    maker="현대"

    # 생성자 메서드 => 객체 즉, Car 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    def driving(self, where):
        print(f"{where}에 {self.number}차량이 가는 중")

    def stop(self, place):
        print(f"{self.number}차량이 {place}에 정차 중")

# 자동차 인스턴스 생성
myCar = Car(19, "red", "1111", "새단")
secondCar = Car(20, "hotpink", "7894", "SUV")

print(id(Car))
print(id(myCar),id(myCar.__init__), id(myCar.driving), id(myCar.stop))




'''
클래스 이름 : Love
클래스 속성 : kind
클래스 기능 : 새우까주기, 금융치료, 데려다주기, 같이아프기, 희생하기
'''
class Love:

    kind = "두근두근"

    def eat(self, food):
        print(f"{food} 먹여주기")
    def money(self, amount):
        print(f"{amount}가 입금되었습니다.")
    def die(self, cause):
        print(f"{cause}가 입금되었습니다.")

'''
클래스 이름 : cal
클래스 속성 : 브랜드, 종류, 색상, 크기
클래스 기능 : 더하기, 뺴기, 나누기, 곱셈
- 데이터 => 속성 또는 기능에서 매개변수
'''
class Calc:
    # 클래스 변수
    maker = "casio"
    __size = (7, 15) # 비공개 속성 __name : 클래스 밖에서 속성 읽거나/쓰기 불가능

    # 객체 즉 인스턴스 생성 메서드
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        self.price = price
        self.__info=info # 인스턴스 생성 시
        self.data = 0

    # 비공개 인스턴스 속성 읽기/쓰기 메서드(getter/setter 메서드)
    # 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self):return self.__info

    @info.setter # 위에 property랑 짝꿍인거임 info를 꼭 info라고 써야함 위에서 info라고 했으니꼐
    def info(self, info):
        self.__info=info

    def getInfo(self):
        return self.__info
    def setInfo(self, info):
        self.__info = info

    # 덧셈 기능
    def plus(self, nums):
        self.data += nums

    def minus(self, nums):
        self.data -= nums

    def multi(self, nums):
        self.data *= nums

    def div(self, nums):
        if not nums: return '0으로 나눌 수 없습니다.'
        self.data = self.data/nums

    def result(self):
        return self.data


'''
Calc 클래스로 인스턴스 생성 -> heap에 생성: 인스턴스 변수 + 클래스 변수 
                                        인스턴스 메서드 사용 가능
'''
c1 = Calc("공학용", "y" ,10000, "Hong")
# 인스턴스 속성 읽기
print(c1.data) #c1. 까지 치면 비공개 속성은 안보이는 것을 확인 할 수 있음
# 비공개 인스턴스 읽고 싶다고;;
print(c1.getInfo(), c1.info)
# 비공개 속성 변경은
c1.setInfo("내꼬><")
print(c1.getInfo(), c1.info)


c1.info = "와아아아"
print(c1.getInfo(), c1.info)

'''
Calc 클래스로 계산기 정보 확인 -> heap에 생성: 클래스 변수만 확인 가능 
                                          인스턴스 메서드 사용 불가능 -> self가 없어서
'''

