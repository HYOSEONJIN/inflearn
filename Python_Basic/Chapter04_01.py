# chapter04_01
# if 실습

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글깨짐 방지

# 기본형식
print(type(True)) #0이 아닌 수, "abc", [1,2,3..] (1,2,3..)
print(type(False)) # 0, "", [], (), {} 비어있음.

# 예1

if True : # if 'a',
    print('good')

if False : # if '',
    print('bad')


# 예2) if-else
if False :
    print('Bad!')
else :
    print('good!')


# 예3) 연산자와 if문

# 관계연산자
# >, <=, <, >=, ==, !=

x=15
y=10

# 양변이 같은 경우
print(x == y)
# 양변이 다른 경우
print(x != y)
# 왼쪽이 클 경우
print(x>y)
#오른쪽이 크거나 같을 경우
print(x <= y)

city=""

if city:
    print("You are in:", city)
else :
    print("please enter your city")



city2="seoul"

if city2:
    print("You are in:", city2)
else :
    print("please enter your city")


# 논리 연산자
# and, or, not


a = 75
b = 40
c = 10


print('and : ', a > b and b > c)
print('or : ', a > b or b > c);
print('not : ', not a > b)
print('not : ', not b < c)


# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 : ' , 3+12>7+3)
print('e2 : ', 5+ +10 *3 > 7+3*20)
print('e3 : ', 5+10 > 3 and  not 7+3==10)
# 1) 5+10, 7+3
# 2) 15>3 10==10
# 3) true and not True


sc1=90
sc2='A'

# 예4)
# 복수의 조건이 모두 참일 경우에 실행
# tap키 or 4번 space

if sc1 >=90 and sc2 =='A' :
    print('Paa')
else :
    print('Fail')

# 예5)
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 =='vip' or id2 =='admin' :
    print('관리자입장')

if id2 == 'admin' and grade == 'platinum' :
    print('최상위관리자')

# 예6)

num = 90

if num>=90 :
    print('Grade : A')
elif num >=80 :
    print('Grade : B')
else :
    print('과락')

# 예7)
# 중첩 조건문
Grade ='A'
total = 95

if Grade == 'A':
    if total >=90:
        print('장학금 100%')
    elif total >=80:
        print('장학금 80%')
    else :
        print('장학금 50%')
else :
    print('장학금 없음')


# in, not in.

q = [10,20,30]
w = {70,80,90,100}
e = {"name" : "Lee", "city" : "seoul", "grade" : "A"}
r = (10, 12,14)

print(15 in q)
print("seoul" in e.values())
