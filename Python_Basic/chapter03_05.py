# 챕터03_5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)


# 선언 / a= (튜플), [리스트], {딕셔너리}
ex = {'key': 'value'}
a = {'name' : 'kim', 'phone' : '01011111111', 'birth' : '870514'}
b = {0 : 'hello python'}
c = {'arr' : [1,2,3,4,5]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age'  : 20,
    'Grage': 'A',
    'status' : True
}

# 자주쓰이진 않지만 리스트안에 튜플 형태로 선언하기도 한다. (불편..)
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 20),
    ('Grage', 'A'),
    ('status', True)
])

f=dict(
    name='niceman',
    city='Seoul',
    age = 20,
    grade = 'A',
    status = True
)


# 타입
print('>>>>>>>')
print('a  - ', type(a), a)
print('b  - ', type(b), b)
print('c  - ', type(c), c)
print('d  - ', type(d), d)
print('e  - ', type(e), e)
print('f  - ', type(f), f)
print()

# 출력
print('>>>>>>>')
print('a  - ', a['name'])           # 키가 존재 X > 에러발생
print('a  - ', a.get('name'))       # 키가 존재 X > NONE으로 처리
print('b  - ', b[0])
print('b  - ', b.get(0))
print('f  - ', f.get('city'))
print('f  - ', f.get('age'))

#print('>>>>>>>')
#print()
