# 1~10까지 출력
nums = list(range(1, 11))

for n in nums:
    print(n, end=" ")

print()
for n in nums:
    print(n, end="-" if n != 5 else "\n")

print()
for i in range(1, 5):
    print("*"*i)

