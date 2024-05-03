'''
중요!!
finally는 예외 여부와 관계없이 무조건 실행
ex) 파일 닫기
'''

def calc(values):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print(f"인덱스 에러 : {err}")
    except Exception as err:
        print(err)
    else: # 에러가 없으면 수행
        print("에러 없음:", values)
    finally: # 무슨 일이 있어도 수행
        print(f"sum = {sum}")
calc([1,2,3])
calc([1,2])