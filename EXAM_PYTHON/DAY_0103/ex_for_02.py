print("Hello World")

# for in 반복문
# 여러개의 데이터를 가지고 있는 데이터에서 한 개씩 원소/요소를 읽어와줌

msg = "Happy New Year"
for ele in msg:
    print(ele)

# [실습1] "hello world" 100번 출력
for i in range(100):
    print("Hello World")

# [실습2] 좋아하는 음식명을 리스트에 저장하기 10개
foods = ["떡볶이", "찜닭", "닭발", "아이스크림", "돈가스", "족발", "짜장면", "카레", "베이클", "마라탕"]
for food in foods:
    print(food)

for food in foods:print(food) # 실행문이 한줄이면 이렇게 쭉 적어도 ㅇㅋ


