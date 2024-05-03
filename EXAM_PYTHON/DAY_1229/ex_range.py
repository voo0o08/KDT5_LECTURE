# range 내장 함수
# 숫자의 범위를 생성해주는 함수
# return : range 타입 반환
# 범위에 포함되는 숫자 데이터 원소/요소라고 함 => 인덱싱

# 1~20으로 구성된 정수 데이터 생성
nums = range(20)
print(nums)
print(f"nums[0:5] => {nums[0:5]}")

numList = list(range(1, 101))
print(numList)

# range(start, end)
# start <= ~ < end

threes = list(range(100,2,-3))
print(threes)