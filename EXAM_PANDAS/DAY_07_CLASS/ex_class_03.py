'''
상속을 볼거랍니다~

2차원 점 클래스
클래스 이름 : pint2D
클래스 속성 : x, y, color, shape, size
클래스 기능 : 주행한다, 정지한다, 후진한다, 그리기
'''
import ex_class_02 as e2
class Point2D:
    # class 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, color, shape, size):
        print("point2D")
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    def draw(self):
        print(f"좌표 ({self.x}, {self.y}) 그리기")

    def printInfo(self):
        print("2D")
        print(f"위치 : {self.x}, {self.y}")
        print(f"색상 : {self.color}")
        print(f"형태 : {self.shape}")

class Point3D(Point2D, e2.Car): # 부모 선언
    # 클래스 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, z, color, shape, size):
        print("point3D")
        # 상속이면 부모 객체를 불러와야함 유후
        super().__init__(x, y, color, shape, size)
        self.z = z

    # 상속받은 부모의 메서드를 나의 취향에 맞게 수정 => 오버라이딩(상속관계에서만 가능)
    def printInfo(self):
        print("3D")
        print(f"위치 : {self.x}, {self.y}, {self.y}")
        print(f"색상 : {self.color}")
        print(f"형태 : {self.shape}")

p2 = Point2D(10, 10, 'y', "cir",(10, 10))
p3 = Point3D(5, 5, 5, 'y',"rec", (3, 3, 10))

print()
p3.printInfo() # 이게 2D거지만 상속받은 거라서 실행 가능