'''
[과제]
자율주행 자동차 class를 상속을 활용하여 만들기
자율비행 자동치 class를 상속을 활용하여 만들기
'''

'''
자동차 클래스
클래스 명 : Car
클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(유일한 클래스 속성 나머지는 인스턴스 속성)
            12 / 빨강 / 1111 / 새단 / 현대
            15 / 노랑 / 6481 / SUV / 현대
클래스 기능 : 주행한다, 정지한다
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

# print(id(Car))
# print(id(myCar),id(myCar.__init__), id(myCar.driving), id(myCar.stop))


'''
자율 주행 자동차 Class 생성하기
클래스 명 : autoCar
상속 클래스 명 : myCar

클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(유일한 클래스 속성 나머지는 인스턴스 속성)
            12 / 빨강 / 1111 / 새단 / 현대
            15 / 노랑 / 6481 / SUV / 현대
            추가할 속성 : x
클래스 기능 : 주행한다, 정지한다
            추가할 기능 : 자율주행 한다
'''

class autoCar(Car):
        # 클래스 속성

        # 생성자 메서드 => 객체 즉, autoCar 인스턴스 생성 메서드
        def __init__(self, wheel, color, number, kind):
            # 상속이면 부모 객체를 불러와야함
            super().__init__(wheel, color, number, kind)

        def driving(self, where): # 오버라이딩
            print(f"{where}에 {self.number}차량이 자율주imim행 중")