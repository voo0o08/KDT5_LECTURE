

'''
ch30 함수에서 위치 인수와 키워드 인수 사용하기
'''
# def print_numbers(a, b, c):
#     print(a, b, c)
# x = [3, 6, 0]
# print_numbers(*x)

# 30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*sub):
    return max(sub)

max_score = get_max_score(korean, english, mathematics, science)
print("높은 점수: ", max_score)

max_score = get_max_score(english, science)
print("높은 점수: ", max_score)

# 30.7 심사문제: 가장 낮은 점수, 높은 점수, 평균 점수를 구하는 함수 만들기
korean, english, mathematics, science = map(int, input().split())
def get_min_max_score(*subs):
    return min(subs), max(subs)

def get_average(**subDict):
    return sum(subDict.values())/len(subDict)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
