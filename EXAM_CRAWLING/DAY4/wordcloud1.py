'''
mask는 nd-array type만 받음!!
'''

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

text = open("test.txt", encoding="utf-8").read()
okt = Okt() # open korean text 객체 생성

# okt함수를 통해 읽어들인 내용의 형태소를 분석한다
sentences_tag = []
sentences_tag = okt.pos(text)
# [('우리나라', 'Noun'), ('의', 'Josa'), ('경우', 'Noun'), ('보통', 'Noun')...]


noun_adf_list = []
for word,tag in sentences_tag:
    if tag in ["Noun", "Adjective"]:
        noun_adf_list.append(word) # 명사와 형용사만 추가

# 가장 많이 나온 단어 50개
counts = Counter(noun_adf_list) # group by 같은 거임
tags = counts.most_common(50)
# print(tags)

if	platform.system()	==	'Windows':
    path	=	r'c:\Windows\Fonts\malgun.ttf'
elif	platform.system()	==	'Darwin':	#	Mac	OS
    path	=	r'/System/Library/Fonts/AppleGothic'
else:
    font	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

img_mask = np.array(Image.open("cloud.png"))
wc = WordCloud(font_path=path, width=400, height=400,
               background_color="white", max_font_size=200,
               repeat=True, colormap="inferno", mask=img_mask)
# repeat False하면 알짜들만 듬성듬성 나옴

cloud = wc.generate_from_frequencies(dict(tags))
#	생성된 WordCloud를 test.jpg로 보낸다.
# cloud.to_file('test.jpg')
plt.figure(figsize=(10, 8))
plt.axis('off') # 그래프가 아니라서 축은 필요없음
plt.imshow(cloud)
plt.show()