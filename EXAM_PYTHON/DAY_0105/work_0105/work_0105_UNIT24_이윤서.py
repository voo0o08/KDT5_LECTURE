'''
24.4 연습문제: 파일 경로에서 파일명만 가져오기
'''

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]

print(filename)

'''
24.5 심사문제: 특정 단어 개수 세기
'''
inputMsg = '''the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.'''
msgList = inputMsg.split()
cnt = 0
for word in msgList:
    if "the" in word and len(word) < 5:
        # print(word)
        cnt += 1
print(cnt)

'''
24.6 심사문제: 높은 가격순으로 출력하기
표준 입력
51900;83000;158000;367500;250000;59200;128500;1304000
길이 9에 오른쪽 정렬
'''
user = "51900;83000;158000;367500;250000;59200;128500;1304000"
numList = sorted(map(int,user.split(";")), reverse=True)
for num in numList:
    print(f"{num:>9,}")

