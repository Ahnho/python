# 평균 구하는 코드 짜보기 1.

def Mean(list):  # ㅡㅡ> 함수이름을 Mean 이라고 함.
	v = 0
	for i in list:
		v += i # = v = v + i
	return v / len(list) # ㅡㅡ> len(list) = list 의 수.


# example
list = [1,2,3,4,5,6]
print("평균값 : {}".format(Mean(list))) # ㅡㅡ> .format = Mean값을 {} 사이로 넣어준다.

# 평균 구하는 코드 짜기 2.

def mean(list):
    return sum(list) / len(list) # 코드 만드는 것 대신 sum 을 이용함

# example
print("평균값 : {}".format(mean(list)))

# 평균 구하는 코드 짜기 3.
# 2번째꺼에서 예외 처리 를 해준것 .
def averige(list):
    if not len(list):
        return 0
    return sum(list) / len(list)

# example
print("평균값 : {}".format(averige(list)))

# sum 을 이용하니깐 엄청 편하다.
