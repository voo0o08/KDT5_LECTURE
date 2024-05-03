# 자연어 처리 전처리 함수 모음(한국어 기준)
from collections import Counter # 단어 빈도수 카운트를 위함
import re
import numpy as np
import pandas as pd

# 1. 결측치 및 중복행 제거 input -> DF, output -> DF
def drop_row(DF):
    '''
    결측치 및 중복행 제거를 위한 함수
    :param DF:
    :return:
    '''
    DF = DF.dropna()
    DF = DF.drop_duplicates()
    DF = DF.reset_index(drop=True)
    # inplace가 가끔 안먹네...
    return DF

# 2. 정규식을 통한 제거
def regex_processing(before_text, re_pattern):
    '''
    정규식 패턴에 해당되면 제거됨
    :param before_text:
    :param re_pattern:
    :return:
    '''
    after_text = re.sub(re_pattern, "", before_text)
    if after_text == "":
        print("공백발생! drop_row 필요")
        return np.nan
    return after_text


# 등장 빈도 기준 정제 함수
def clean_by_freq(tokenized_words, cut_off_count):
    # 파이썬의 Counter 모듈을 통해 단어의 빈도수 카운트하여 단어 집합 생성
    vocab = Counter(tokenized_words)

    # 빈도수가 cut_off_count 이하인 단어 set 추출
    uncommon_words = {key for key, value in vocab.items() if value <= cut_off_count}

    # uncommon_words에 포함되지 않는 단어 리스트 생성
    cleaned_words = [word for word in tokenized_words if word not in uncommon_words]

    return cleaned_words


# 단어 길이 기준 정제 함수
def clean_by_len(tokenized_words, cut_off_length):
    # 길이가 cut_off_length 이하인 단어 제거
    cleaned_by_freq_len = []

    for word in tokenized_words:
        if len(word) > cut_off_length:
            cleaned_by_freq_len.append(word)

    return cleaned_by_freq_len


# 불용어 제거 함수
def clean_by_stopwords(tokenized_words, stop_words_set=set()):
    # %%
    # 불용어 제거
    stopwords_path = "../data/stop_word.txt"

    # 파일 열기
    with open(stopwords_path, encoding="utf-8") as f:
        stopwords = f.readlines()
    stop_words_set = {word.strip() for word in stopwords} | stop_words_set

    cleaned_words = []

    for word in tokenized_words:
        if word not in stop_words_set:
            cleaned_words.append(word)

    return cleaned_words

# 데이터 인코딩 함수
def idx_encoder(tokens, word_to_idx):
    '''

    :param tokens: 데이터 프레임의 토큰col의 한줄 한줄 list
    :param word_to_idx: 불용어/빈도 등 정제가 끝난 0은 unknown, 1은 결측치인 단어사전
    :return:
    '''
    encoded_idx = []

    for token in tokens:
        try:
            idx = word_to_idx[token]
            encoded_idx.append(idx)
        except KeyError:
            encoded_idx.append(0)

    return encoded_idx

