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
