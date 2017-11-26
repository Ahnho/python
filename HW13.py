# -*- coding: utf-8 -*-

# 매개변수, 풀기,변수

from sys import argv
# import ㅡㅡ> 스크립트에서 필요한 기능을 가져다 쓰는 방법
# argv ㅡㅡ> 실행인자 변수 입니다. 스크립트를 실행할때 전달 했던 실행인자가 담겨있습니다.

(script, first, second, third) = argv

print("스크립트 이름:", script)
print("첫 번째 변수:", first)
print("두 번째 변수:", second)
print("세 번째 변수:", third)

# ValueError: not enough values to unpack (expected 4, got 1) : 이 에러가 뜨는데  왜 압축할 값이 충분하지 않은지 모르겠음
