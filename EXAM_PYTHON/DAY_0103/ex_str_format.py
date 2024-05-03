'''
출력 예쁘게 하는 방법
- 데이터 출력하는 칸 수, 정렬 방향, 빈 칸수 채우기 ...
'''
count = 1
print(f"파일명 : img_{count:#^5}.jpg")

count = 21
print(f"파일명 : img_{count:*<5}.jpg")

count = 101
print(f"파일명 : img_{count:>5}.jpg")
# ^가운데 <왼쪽 >오른쪽(default)
