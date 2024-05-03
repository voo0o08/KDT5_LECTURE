'''
1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
 출력하는 함수를 구현하세요.
['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']
'''
def min_max_str(words):
    words.sort(reverse=True)
    print(f"정렬 결과 : {words}")
    print(f"가장 높은 문자열 : {words[0]}, 가장 낮은 문자열 : {words[-1]}")
strList = input("msg=")[2:-2].split("', '")
# print(strList)
min_max_str(strList)
a = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']
