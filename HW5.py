# -*- coding: utf-8 -*-

# 변수와 출력

my_name =("Sangho Ahn")
my_age = 19
my_height = 000 #cm
my_weight = 55 #kg

print("%s에 대해 이야기해 보죠." % my_name)
print("키는%d 센티미터고요." % my_height)
print("몸무게는%d 킬로그램이에요."%my_weight)
print("조금씩 계속 찌고있습니다.")

# 이줄은 조금 까다롭다고 합니다.
print("%d, %d, %d를 모두 더하면 %d랍니다." % (
    my_age,my_height,my_weight,my_height+my_age+my_weight))


# 궁금한것: %s 는 문자를 불러오는것 , %d 는 숫자를 불러올때 쓰는것입니까? %r은 언제쓰이는거죠?
