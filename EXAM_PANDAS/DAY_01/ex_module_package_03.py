'''
사용할 모듈 로딩
import 패키지명.모듈명
# from 패키지명 import 모듈명
'''
import urllib.request as req
from http.client import HTTPResponse # from 패키지.모듈 import 클래스

from urllib import  error, parse

dataObj = req.urlopen("https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
print(dataObj)