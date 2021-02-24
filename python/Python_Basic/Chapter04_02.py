# chapter04_02
# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글깨짐 방지


for v1 in range(10) : # 0-9까지 10개.
    print('v1 is :', v1)

for v2 in range(1, 11) : # 1-10까지
    print('v2 is :', v2)

for v3 in range(1,11,2) : # 1-11까지 2개씩 점프
    print('v3 is :', v3)

# 1~1000합을 구하자

sum1 = 0

for v in range(1,1001):
    sum1 += v

print('1-1000까지의 합 :  ',sum1)

# range 함수
print('1-1000까지의 합 : ', sum(range(1,1001)))
print('1-1000까지 4의 배수의 합 : ', sum(range(4,1001,4)))
print(type(range(1,11)))


# iterables : 반복할 수 있는 객체
# iterables data 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip


# 예제1
names = ['kim','pakr','cho','lee','choi','yoo']

for name in names :
    print ('You are : ', name)

# 예제2
lotto_number = [12, 19, 21, 28, 36, 37]

for n in lotto_number :
    print ("current number : ", n)

# 예제3
word = "beautiful"

for s in word :
    print('word : ', s)

# 예제4
my_info = {
    "name" : "lee",
    "age" : 33,
    "city" : "seoul"
}

for k in my_info:
    print('key :', k , my_info[k])

for v in my_info.values():
    print('value :', v)


# 예제5
# if와 for같이쓰기

name = 'FineAppLE'

#isupper 대문자인지 / islower 소문자인지
for n in name :
    if (n.isupper()):
        print(n)
    else:
        print(n.upper()) #대문자로 출력

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34 :
        print ('Found 34!')
        break; #36, 38 은 실행되지 않도록.
    else :
        print('Not Found :', num)


# continue

lt = ["1", 2, 5, True, 4.2, complex(4)] #여러가지자료형
#boolean을 빼고 출력하기
for v in lt :
    if type(v) is bool:
        continue #들여쓰기 생각해놓자 JAVA와다름.
    print("current type :", v,"의 타입은 ", type(v))
    print("multiply by 2:", v*3) # 참고로 true*3=1

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers :
    if num == 49 :
        print("Found : 49")
        break
else :
    print("Not Found: 49")
    # for문이 다돌고 break를 만나지 않으면(이 경우 49를 찾지못하면)
    # 마지막에 for-else가 실행된다.

# 구구단 출력 2~9단
for i in range(2,10):
    for j in range(1,10):
        #print(i,"*",j,"= ", i*j)
        print('{:4d}'.format(i*j), end='') #4자리 정수로 출력, end=''
    print()

# 변환 예제
name2 = 'Aceman'
print('reversed :', reversed(name2))
print('reversed :', list(reversed(name2)))
print('Tuple :', tuple(reversed(name2)))
print('set :', set(reversed(name2))) #순서X
