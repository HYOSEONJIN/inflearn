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
print()

# 딕셔너리 추가
print('>>>>>>>')
a['address'] = 'seoul'
a['name'] = 'jin'  # 원래 있던 값(name)을 추가하면 수정해버린다 (kim>jin)
a['rank'] = [1,2,3]
print('a  - ', a)
print()

# 딕셔너리 길이 확인
print('>>>>>>>')
print('a  - ', len(a)) #키의 갯수
print('b  - ', len(b))
print('c  - ', len(c))
print('d  - ', len(d))
print('e  - ', len(e))
print('f  - ', len(f))
print()


# dict_keys, dict_values, dict_items  : 반복문(__iter__)에서 사용가능
print('>>>>>>>')
# .keys() 키값들만 가져온다.
print('a  - ',  a.keys())
print('c  - ',  c.keys())
print('d  - ',  d.keys())
print('e  - ',  e.keys())
print('e  - ',  list(e.keys()))
print('a  - ',  list(a.keys()))
#.values 밸류값만 가져온다.
print('c  - ',  c.values())
print('d  - ',  d.values())
print('e  - ',  e.values())
#.itmes 키와 밸류값을 가져온다.
print('c  - ',  c.items())
print('d  - ',  d.items())
print('e  - ',  e.items())
print('e  - ',  list(e.items()))
print('d  - ',  list(d.items()))
print()
print('>>>>>>>')
print('a  - ', a.pop('name'))
print('a  - ', a)
print('c  - ', c.pop('arr'))
print('c  - ', c)
print()
print('f  - ', f.popitem())
print('f  - ', f)
print('f  - ', f.popitem())
print('f  - ', f)
print('f  - ', f.popitem())
print('f  - ', f)
print('f  - ', f.popitem())
print('f  - ', f)
print('f  - ', f.popitem())
print('f  - ', f)
print()
print('a  - ', 'birth' in a ) # birth라는 키가 a에 있는가.
print('a  - ', 'city' in b)


#수정.
print('>>>>>>>')
a['test']='test_dict'
print('a  - ', a)
a['test']='test_dict2'
print('a  - ', a)

a.update(test='test_dict3')
print('a  - ', a)

temp = {'test' : 'test_dict4'}
a.update(temp)
print('a  - ', a)
