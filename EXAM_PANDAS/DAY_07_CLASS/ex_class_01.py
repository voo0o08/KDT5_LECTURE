# ------------------------------------------
# 사용자 정의 클래스
# ------------------------------------------

# 모든 것이 속성이 있 는 것은 아니다
# 모든 것이 메소드가 있는 것은 아니다

# 클래스 정의 : 밤하늘의 별을 저장하는 데이터 / 새로운 데이터 타입이라고 생각하면 될 듯하다
# 클래스 이름 : star
# 클래스 속성 : 크기, 색상, 밝기 => 속성(attribute), 필드(field) => 변수
# 클래스 기능 : 반짝거린다, 떨어진다. => 메서드(method) : 해당 클래스 전용의 함수를 뜻함

class Star:
    # 는 deco임 메서드 위에 적는, 함수가 이런 기능을 한다고 적어주는 것
    # 최상위 부모클래스 object로부터 상속 받은 함수 즉 메서드
    # 형태 def __XX__()
    # 나의 클래스에 맞도록 수정 즉 리모델링해서 사용 => 오버라이드

    # 여기다가 냅다 쓰는 건 해당 클래스로 생성된 객체(인스턴스)가 다같이 공유함 -> 메모리에  핵 이득
    timezone="밤"

    # 클래스 변수 비공개 변수로 만들기
    __privateVal = 7

    def __init__(self, size, color, brightness): # 상속받은 init을 오버라이딩 중
        print(f"__init__() : {size}, {color}, {brightness}")
        self.__size = size # 다시는 사이즈  수정 불가능
        self.color = color
        self.brightness = brightness

    # 별 클래스 기능
    def drop(self):
        print(f'{self.color} 별이 떨어지니 소원을 비세연')

    # 비공개 인스턴스 속성에 접근하기 위한 메서드 => getter/setter
    # 비공개 인스턴스 속성 읽어 오는 메서드 get속성명() => 속성값
    # 비공개 인스턴스 속성에 값 설정 하는 메서드 set속성명(새로운 값)
    def getSize(self):
        return self.__size
    def setSize(self, size):
        self.__size = size

    # 비공개 인스턴스 메서드 => 클래스 내부에서만 호출되는 메서드 = 인스턴스 메소드
    def __inner(self):
        print("나는 비공개 인스턴스 메서드")
# ---------------------------------------------
# 객체 생성 => 클래스에 정의된 속성 즉 변수와 함수들이 메모리 힙영역에 생성
# 생성 방법 => 클래스명(매개변수) 생성자 함수/메서드
#               매개변수는 0개부터 n개까지 다양함

myStar = Star(10, "yellow", 1)
print(myStar.color)
myStar.color=100
print(myStar.color)

myStar.drop()

print(f"클래스명.__dict__:{Star.__dict__}")
print(f"인스턴스명.__dict__:{myStar.__dict__}")
# 클래스 내의 메서드는 self가 알아서 보내주는 거임
myStar.size = 54445
print(myStar.size)
print(f"인스턴스명.__dict__:{myStar.__dict__}")

# 인스턴스 비공개 속성값에 접근해
print(myStar.getSize())
