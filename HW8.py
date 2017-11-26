# -*- coding: utf-8 -*-

# 출력하고 또 출력하기

formatter = ("%s %s %s %s")

print(formatter %(1,2,3,4))
print(formatter % ("하나","둘","셋","넷"))
print(formatter % (True,False,False,True))
print(formatter %(formatter,formatter,formatter,formatter))
print(formatter %(
    "난 이게 있죠.",
    "지금 막 써 주신 그것.",
    "하지만 '노래'하진 않아요.",
    "그러니까 잘자요."
))

formatter2 = ("%r %r %r %r")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~

# 궁금한것:포맷에 %s와 %r중 어는 것을 써야 하냐는 질문에서 포맷이 무엇이죠?
