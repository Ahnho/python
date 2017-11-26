# -*- coding: utf-8 -*-

# 프롬프트와 넘기기

from sys import argv

(script,SanghoAhn) = argv
prompt = ('>')

print("안녕 %s, 나는 %s 스크립트야", % (SanghoAhn,script))
print("몇 가지 질문을 할게.")
lives =(input(prompt))
