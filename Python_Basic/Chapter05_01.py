# Chapter05_01
# 파이썬 함수(Function)
# 파이썬 함수식 및 람다

# 함수 정의방법
# def function_name(parameter):
#   code

# 예제1)
def first_func(w):
    print("Hello,", w)

word = "Good boy"
first_func(word)



# 예제2
def return_func(w):
    result = "Hello," + str(w)
    return result

x = return_func('goodgirl')
print(x)


# 예제3 (다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3  # 이런 리턴도 가능!

x, y, z =  func_mul(10)
print(x, y ,z)


# 튜플리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) #팩킹해서 튜플로!

q = func_mul2(20)
print(type(q), q)

# 리스트리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul2(30)
print(type(p), p)

def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1 , 'v2' : y2 , 'v3' :y3}

d = func_mul2(40)
print(type(d), d, d.items(), d.keys())



# 증요
# *args, **kwargs

# *args(언팩킹)
# *뒤에 단어는 아무거나 가능, 여러개 받기 가능. 튜플에자주사용.

def args_func(*args) :
    for i, v in enumerate(args) :
        print('Result : {}'.format(i), v)
    print('--------')

args_func('Lee')
args_func('Lee','Park','Jin')

# **kwargs
# 딕셔너리로 이해.
def kwargs_func(**kwa) :
    for v in kwa.keys():
        print("{}".format(v), kwa[v])
    print('--------')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park', name3='Jin')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)


# 중첩함수
# 함수안의 함수는 바깥에서 사용 불가.
def nested_func(num):
    def func_in_func(num):
        print(num) #2
    print("In func") #1
    func_in_func(num+100) #2

nested_func(100)


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 > 리소스(메모리) 할당
# 람다는 즉시 실행 함수 (heap초기화) > 메모리 heap초기화
# 남발 시 가독성이 오히려 감소.
