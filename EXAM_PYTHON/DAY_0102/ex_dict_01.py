'''
[질문] 10명 학생에 대한 학점을 저장하기
- 학생의 이름과 학점
'''

stdNums = ['std01', 'std02', 'std03', 'std04', 'std05']
stdJumsus = [90, 89, 100, 76, 34]

# 03번 학생의 학번과 점수를 출력하세요
idx = stdNums.index('std03')
print(f"{stdNums[idx]}학번 학생의 점수 {stdJumsus[idx]}")

stdNumsJumsu = [['std01', 98], ['std02', 89], ['std03', 100], ['std04', 76], ['std05', 34]]

# -------------------------------------------
# dict 자료형
# -연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관 배열
# -형태 = key:value (주민번호:이름, 학번:전공) key가 중복이 안되도록!! => 연관배열
# -------------------------------------------

stdNumsJumsu = {'std01': 90,
                'std02': 89,
                'std03': 100,
                'std04': 76,
                'std05': 34}
print(f"개수 = {len(stdNumsJumsu)} 데이터 타입 = {type(stdNumsJumsu)}")
# 원소 읽는 방법 => 변수명[key]
print(f"{stdNumsJumsu['std03']}")

# -------------------------------------------
# 원소/요소 추가 방법 => 변수명[새로운 키] = 데이터
# -------------------------------------------
# 학번 10인 학생, 점수 99.8 저장하기
print(stdNumsJumsu)
stdNumsJumsu["std10"] = 99.8
print(stdNumsJumsu)

# -------------------------------------------
# 원소/요소 데이터 삭제 => del 변수명[키]
del stdNumsJumsu['std01']
print(stdNumsJumsu)