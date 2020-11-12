# Chapter03_03.py
# 리스트
# 자료구조에서 중요

# 리스트 자료형 (순서, 중복, 삭제 가능)



### 선언
a = []
b = list()
c = [ 70, 75, 80, 75] # print(len(c))=4
d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형도 가능
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 in 리스트
f = [21.42, 'foobar', 3, 4, False, 3.14159]



# 인덱싱
print('>>>>>>>>>')
print(' d - ', type(d), d)
print(' d - ', d[1])
print(' d - ', d[0] + d[1] + d[1])
print(' d - ', d[-1]) # 맨 오른쪽
print(' e - ', e[-1][1])
print(' e - ', list(e[-1][1])) # 문자열을 리스트 형태로 형변환 가능


# 슬라이싱
print('>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])


# 리스트 연산 (리스트+리스트=리스트)
print('>>>>>>>>>')
print('c + d =', c+d)
print('c * 3 =', c*3) #리스트*정수= 리스트, 리스트연산의 결과 = 리스트
# print("'Test' + c[0] = ", 'test'+c[0]) #type error
print("'Test' + c[0] = ", 'test'+str(c[0]))


# 값 비교
print('>>>>>>>>>')
print(c == c[:3] + c[3:])
print(c)
print(c[:3])
print(c[3:])

# 같은 identity(id)
print('>>>>>>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))    # 파이썬이 속도와 쾌적한 환경을 제공하기 위해 리스트도 같은값 = 같은id

# 리스트 수정, 삭제
print('>>>>>>>>>')
c[0] = 4
print('c - ', c)
print(c[1:2])  #c[1]
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1:2] = [['a', 'b', 'c']] # = c[1]=['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)

# 제거/삭제
print('>>>>>>>>>')
del c[2]
print('c - ', c)


# 리스트 함수
print('>>>>>>>>>')
a = [5, 2, 3, 1, 4]
print('a - ', a)
#a[5] = 10 에러, 추가시엔 append 함수!
a.append(10)
print('a - ', a)
a.sort() # 파이썬 리스트 오름차순 정렬
print('a - ', a)
a.reverse()  #역순으로 정렬 (내림차순 X)
print('a - ', a)
print('a - ', a.index(4), a[4]) # 인덱스로 가져오기
a.insert(2,7) #0,1,2번째(숫자론세번째)  자리에 7을 넣고 나머지는 뒤로 민다 (삽입)
print('a - ', a)
a.remove(1) #del a[6]와 같다. 인덱스 제거가 아닌 값으로 제거.
print('a - ', a)
print('a - ', a.pop())
#기존의 리스트에서 마지막에 있던 값을 꺼내오고 그 값을 삭제
# LAST IN FIRST OUT
# 접시를 쌓아놓고 맨 위에 쌓인(마지막에 놓은) 것을 먼저 쓰는 것을 생각하면 이해가 쉽다.
# ex) 웹 브라우저에서 뒤로가기를 누르면 바로 전 페이지로 가는 것과 같다
print('a - ', a)
print('a - ', a.count(4)) # 리스트 안에 값 '4'가 몇개인지, 있는지 없는지 확인할때 (=값 0)


ex=[8,9]
a.extend(ex) #뒤에 다른 리스트를 붙여줌
print('a - ', a)

#### 삭제 : remove, del, pop

# 반복문을 이용한 pop

while  a:
    data =a.pop()
    print(data)
