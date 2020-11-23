# Chapter06_01
# 클래스 (ㅋㅋ붕어빵기계)
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수


# 클래스와 and  인스턴스의 차이를 이해하는 것이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유 (정수기! 공용화장실! 같은 것 ㅋㅋ)
# 인스턴스 변수 : 객체마다 별도 존재.

# 예제1)
# class dog():, class dog:, class(object):
class dog(): #object 상속
    # 클래스 속성
    specied = 'firstdog' #클래스 변수.

    # 초기화/인스턴스 속성 (java생성자)
    def __init__(self,name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(dog)

# 인스턴스화 (- 코드로 구현해서 메모리에 올라간 시점.)
a = dog('happy',15)
b = dog('micky',2)
c = dog('micky',2)
# 비교
print(a == b, id(a), id(b))
print(a == c, id(b), id(c))

# 네임스페이스
print('dog1',a.__dict__)
print('dog2',b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.specied == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.specied))

print(dog.specied) # 클래스에서도
print(a.specied) # 인스턴스변수에서도 바로 접근 공유 가능하다. (같은값.)


# 예제2) - self의 이해. (자바의super같은 느낌인듯)

class SelfTest:
    def func1():
        print('func1 called')
    def func2(self): #__init__이 없어도 알아서 생성해주는 똑쟁이 파이썬..
        print(id(self)) #f값.
        print('func2 called')

f = SelfTest()

print(dir(f)) #func1과 func2가 있음을 확인 가능
print(id(f))

# f.func1() 에러! 예외.
f.func2() # self가 있는 인스턴스 메서드
SelfTest.func1() # 클래스로바로 접근해서 접근. (매개변수가 없는 클래스메소드)
                # self가 있으면 인스턴스화 시킨 변수가 self로 넘어감.
# SelfTest.func2() 반대로 에러! 예외
SelfTest.func2(f)


# 예제3)
# 클래스 변수, 인스턴스 변수

class Warehouse:
    #클래스 변수
    stock_num = 0 #재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name=name
        Warehouse.stock_num +=1

    def __del__(self):
        Warehouse.stock_num -=1

user1 = Warehouse('Lee')
user2 = Warehouse('Jin')

print(Warehouse.stock_num) # 붕어빵 몇개구웠어! = 2개

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before>>',Warehouse.__dict__) #stock_num:2

del user1
print('after>>',Warehouse.__dict__)

# 예제4

class dog2():
    specied = 'firstdog'

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
d = dog2('july',4)
e = dog2('merry',10)

# 메서드 호출
print(d.info())
print(e.info())
print(d.speak('wal wal'))
print(e.speak('mung mung'))
