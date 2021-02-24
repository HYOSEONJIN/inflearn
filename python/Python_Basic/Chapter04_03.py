# chapter04_03
# 파이썬 반복문
# while 실습

# while <expr>:
#   <statement(s)>

# 예제1

n=50
while n > 0:
    n-=1
    print(n)


# 예제2
a = ['foo', 'bar','baz']

# while a: = while True :

while a:
    print(a.pop(0))



# 예제3
# break, continue

n = 5

while n>0 :
    n-=1
    if n==2:
        break
    print(n)
print('Loop Ended.') # 4, 3

# 예제4
m = 5

while m>0 :
    m-=1
    if m==2:
        continue
    print(m)
print('Loop Ended.') # 4, 3, 1, 0

# 예제5 - if 중첩

i = 1
while 1 <=10:
    print('i : ',i)
    if i == 6:
        break
    i += 1

# 예제6 while - else

n = 10
while n>0 :
    n-=1
    print(n)
    if n==5:
        break
else :
    print('else out.')


# 예제7
a = ['foo', 'bar', 'baz','qux']
s = 'qux'

i = 0

while i < len(a) : # i < 4
    if a[i] == s:
        print(s, 'found')
        break
    i+=1
else :
    print(s, 'not found in list')


#  무한반복
# while True :

# 예제8

a = ['foo','bar','baz']

while True :
    if not a :
        break
    print(a.pop())
