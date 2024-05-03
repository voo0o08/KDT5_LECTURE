'''
자동차 클래스
- 역할 : 자동차 관련 데이터, 기능을 모두 저장 관리하는 클래스
- 문법
  class 클래스명 :
      <code>
- 엔진, 연료, 브랜드, 색상, 번호
- 전진, 후진, 좌회전, 우회전, 정지
'''
class Car:
    number = "123가1234" # 브랜드 공장이라면 브랜드명을 이렇게 선언해야함 : 바뀌지 않을 속성이니까
    # 클래스 생성 시 필수로 사용되는 메서드
    # 힙 메모리에 속성들의 값을 저장해주는 역할
    def __init__(self, engine_, maker_, color_,): # _는 별 의미없음 그냥 헷갈림 방지용, default값 가능
        print("__init__")
        # __init__ -> 초기화?!
        # 자동차 클래스가 가지는 속성을 메모리 힙에 저장해야함
        # self에 가서 넣어라 -> 알아서 넣음
        self.engine = engine_ #니가 준 engine_주소 값을 engine 메모리에 넣겠다.
        self.maker = maker_
        self.color = color_

    def go(self): # self 니가 부른 애의 정보를 그냥 주겠다!!!
        print(f"{self.number} 자동차 전진")

    def back(self):
        print(f"{self.number} 자동차 후진")

    def stop(self):
        print(f"{self.number} 자동차 정지")

MyCar = Car("전기", "현대", "노랑",)
MyCar2 = Car("뿡이다", "집갈래", "스껄한 하루~")

MyCar.go()