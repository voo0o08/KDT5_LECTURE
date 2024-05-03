
'''
6. 문자열 리스트와 정수 1개를 입력하면 아래와 같이 출력하는 함수를 구현해 주세요.
['askde', 'beach', 'surf'] n=2
['home','pitch','python'] n=1
'''
def sortWord(datas):
    n = int(datas[-1])
    words = []
    temp = ""
    for i in datas:
        if i.isalpha():
            temp += i
        else:
            words.append(temp)
            temp = ""
    result = [] # 입력에서 단어만 뽑아낸 리스트
    for idx, w in enumerate(words):
        if len(w) > n:
            result.append(words[idx])
    print("n번째로 정렬 안한 상태", result)

    words_dict = {} # key = n번째 요소 / value = 해당 단어
    for word in result:
        words_dict[word[n]] = word
    # print(words_dict)
    nList = sorted(list(words_dict.keys())) # n번째 알파벳들끼리 정렬
    # print(nList)

    result2 = []
    for nAlpha in nList:
        result2.append(words_dict[nAlpha])
    print(result2)

datas = input("datas : ")
sortWord(datas)
