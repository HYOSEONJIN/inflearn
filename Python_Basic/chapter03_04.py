#chapter03_04
# 파이썬 튜플
# 리스트와 튜플 비교
# 튜플 자료형( 순서와 중복은 가능하지만, 수정과 삭제가 불가능(del/remove)_리뮤테이블

# 선언

t1 = ()
t2 = (1, 2)
t3 =(1,)  # 1개는 끝이 , 로 끝나야 tuple로 인식한다 (1)=int
t4  = 1, 2, 3



a=()
b=(1,)
c=(11,12,13,14)
d=(100, 1000, 'Ace', 'Base', 'Captain')
e=(100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>>>>>')
print('d - ' ,d[1])
print('d - ' ,d[0]+d[1]+d[1])
print('d - ', d[-1])
print('e - ', e[-1]) #튜플반환
print('e - ', e[-1][1])

print('chane list - ', list(e[-1][1]))


# 수정xxx
# d[0] = 1500

# 슬라이싱
print('>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>>>>>')
print('c+ d - ', c+d)
print('c * 3 - ', c*3)

# 튜플 함수
print('>>>>>>>>>')
a = ( 5, 2, 3, 1, 4)
print('a - ',a)
print('a - ', a.index(3)) #3의 위치
print ('a - ', a.count(2)) # 2의 갯수

# 팩킹 & 언팩킹

# 팩킹 ( 하나로 묶는다 )

t = ('foo','bar','baz','qux')
print(t)


# 언팩킹1
(x1, x2, x3, x4) = t #()없어도 가능, 하지만 언팩킹을 알려주기위해 ()를 쓰는편,
print(type(x1), type(x2), type(x3), type(x4) ) #str
print(x1, x2, x3, x4)


# 팩킹&언팩킹1

t2 = 1, 2, 3 #괄호가 없어도 튜플임
t3 = 4, 3
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
