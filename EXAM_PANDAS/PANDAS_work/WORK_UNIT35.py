'''
34.5 연습문제: 날짜 클래스 만들기
Date 클래스 완성하기
is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드
날짜에서 월은 12 / 일은 31까지
'''
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split("-"))
        return month <= 12 and day <= 31

if Date.is_date_valid("2000-10-31"):
    print("올바른 날짜 형식입니다.")
else:
    print("잘못된 날짜 형식입니다.")

'''
35.6 심사문제: 시간 클래스 만들기
표준 입력으로 시:분:초 형식의 시간 입력
Time 클래스 완성
from_string 문자열로 인스턴스를 만드는 메서드
is_time_valid는 문자열이 올바른지 검사하는 메서드
시간은 24 분은 59 초는 60까지 있어야함
'''
print("35.6\n\n")
class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    @classmethod
    def is_time_valid(cls, string):
        cls.h, cls.m, cls.s = map(int, string.split(":"))
        return cls.h <= 24 and cls.m <= 59 and cls.s<=60
        # return string.split(":")
    @classmethod
    def from_string(cls, string):
        return Time(cls.h, cls.m, cls.s)

time_string = "23:35:59"

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.h, t.m, t.s)
else:
    print("잘못된 시간 형식 입니다.")