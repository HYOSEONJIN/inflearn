
#chapter02-2
#파이썬 변수

#기본선언
n=700
print(n)
print(n*700)
print(type(n)) #타입함수 자료형 알려줌
print()
#동시선언
x = y = z = 700
print(x,y,z)
print()

#선언과재선언
ver=75
ver ='changer value'
print(ver)
print(type(ver)) #마지막에 선언한 것이 재선언되서 덮어쓰기됨
print()

# Object Reperences
# 변수의 값이 할당 상태일 때

# 예1)
print(300)
#변수로 할당되지 않은 수 300
# 1.타입에 맞는 오브젝트를 생성하고 > print(int(300)) 이라고 자동으로해줌
# 2.값을 생성하고
# 3.콘솔출력

n=777
print(n, type(n))
print()


# Id(identity)확인 : 객체의 고유값 확인

m=800
n=655

print(id(m)) #Object의 고유값/id값
print(id(n))
print(id(m)==id(n)) #false
print()

m=800
n=800
print(id(m))
print(id(n))
print(id(m)==id(n)) #true
# 파이썬엔진은 이름은 다르지만 값이 같다면 하나의 인스턴스로 취급한다
# 원활하고 빠른 프로젝트 흐름을 위해서
print()


# 다양한 변수선언

# 1. camelCase 처음에는 소문자 단어시작마다 대문자 = method
# studentGrade
# 2. PascalCase 첫글자도 대문자 단어시작마다 대문자 = class
# StudentGrade
# 3. snakeCase 띄어쓰기는 _로 표현, 파이썬에서 많이 사용한다
#student_grade

age =1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age =6
age_ =7
_AGE_ = 8

#특수문자나 숫자로 시작하는 변수는 X


#예약어는 변수명으로 불가능
# ex) for, as, class,
# python reserved words list
