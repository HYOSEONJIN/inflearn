# chapter03_06
# 집합(set)
# 집합 (순서X, 중복X, 추가 및 삭제 O)


# 선언

a = set()
print(a)
b = set([1,2,3,4])
c = set([1,4,5,6])
d = set([1,2,'pen','cap','plate'])
e = {'foo','bar','baz','foo','qux'} #key가없이 원소만 나열한다면 SET
f = {42, 'foo', (1,2,3), 3.14159}

# 출력
print ('a-',type(a),a, 2 in a )
print ('b-',type(b),b, 2 in b )
print ('c-',type(c),c)
print ('d-',type(d),d)
print ('e-',type(e),e)
print ('f-',type(f),f, 2 in f )


# 튜플 변환 (Set>>tuple)
print()
t=tuple(b)
print('t-',t)
print(type(t))
print('t-', t[0], t[1:3])


# 리스트 변환
l = list(c)
l2 = list(e)
print('l-', l, type(l))
print('l2-', l2, type(l2))


# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f)) #갯수/ 중복xxx


# 집합 자료형 활용
# 교집합.
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print('s1 & s2 :' ,s1 & s2)
print('s1 & s2 :' ,s1.intersection(s2))
# 합집합.
print('s1 | s2 : ', s1|s2)
print('s1 | s2 : ', s1.union(s2))
# 차집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))
# 중복원소가 있는지 알려주는 함수
print('s1 & s2 ', s1.isdisjoint(s2)) #False 일떄 교집함이 있다는뜻!! (dis)
# 부분 집합 확인
print('subset : ', s1.issubset(s2))
print('superset : ',s1.issuperset(s2))


# 데이터 추가/삭제.
s1 = set([1,2,3,4])
s1.add(5)
print(s1)
s1.remove(2)
print(s1)
# remove로 없는 원소를 삭제하려고 하면 Key error 라는 에러가 나타난다
s1.discard(3)
print(s1)
s1.discard(7) # 없는 원소를 삭제하려고 해도 에러X (예외발생X)
s1.clear() #전부삭제(리스트도마찬가지임)
print(s1)
