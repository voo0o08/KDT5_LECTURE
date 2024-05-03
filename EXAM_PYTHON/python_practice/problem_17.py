
'''
17. 입력 받은 메시지 중에서 중복 없이 숫자만 출력하는 함수를 만들어 주세요.
- 입력 받는 기능은 함수 안에 넣지 않음
Happy New Year 2023!
홍길동 010-1111-2222
'''
def setNums(msg):
    nums = set()
    for ch in msg:
        if ch.isdigit():
            nums.add((ch))
    nums = list(nums)
    result = ""
    for i in range(len(nums)):
        result += f"{nums[i]}, " if i < len(nums)-1 else f"{nums[i]}"
    print(result)
usermsg = input("메시지 입력 : ")
setNums(usermsg)