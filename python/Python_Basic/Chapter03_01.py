# chapter03_1
# 숫자형

# 파이썬 지원 자료형
"""

int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
:
:
"""

# 데이터타입

str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 != 10.0
int_v = 7
dict = {
    "name" : "Machine Learning",
    "Version" : 2.0
    # key : value
}

# 괄호모양에 따라 타입이 달라지므로 주의
tuple = (7, 8, 9)
tuple = 7, 8, 9
set = {3,5,7}
list = [str1, str2]

# 데이터타입출력

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(list))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))



# 숫자형 연산자
"""

+
-
*
/
// : 몫만
% : 나머지
abs(x) : 절대값
pow(x,y) : x의 y제곱 , x**y 도 같은뜻

"""
print()

# 정수선언
i=77
i2 = -14
big_int = 7777777777777777777777777777777777777777777777777777777777777
# 자바와 달리 큰수도 값을 집어넣을 수 있다

# 정수출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

# 실수출력
print(f)
print(f2)
print(f3)
print(f4)
print()




# 연산실습
i1=39
i2=939
big_int1 = 77777777777777777777777777777777777777777777777777777
big_int2 = 23948293482938492308490238490328490238490238490238492
f1 = 1.234
f2 = 3.23948293482938492308490238490328490238490238490238492

# +
print(">>>>>>>>>>> + ")
print("i1 + i2 : ", i1+i2 )
print("f1 + f2 : ", f1+f2)
print("big_int1 + big_int2 : ", big_int1+big_int2)

# *
print(">>>>>>>>>>> * ")
print("i1 * i2 : ", i1*i2 )
print("f1 * f2 : ", f1*f2)
print("big_int1 * big_int2 : ", big_int1*big_int2)
print()


# 형변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 데이터타입출력
print(type(a),type(b),type(c),type(d))

# 형변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True=1, False=0
print(float(False))
print(complex(3))
print(complex('3')) #문자형 > 숫자형으로 바꾼 다음에 실행됨 (똑똑)
print(complex(False))
print()

# 수치연산 함수
print(abs(-7))

x,y = divmod(100,8)
print(x,y) #몫과 나머지

print(pow(5,3))
print(5**3)
print()

# Math 외부 모듈

import math

print(math.pi)
print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수 
