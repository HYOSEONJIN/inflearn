#chapter02-1
#파이썬 완전 기초
#print 사용법

#기본출#
print('Python Start')
print("Python Start")
print()
print()
print('''Python Start''')
print("""Python Start""")
print()


#seperator 옵션
print('p','y','t','h','o','n',sep='')
print('010','1111','7777',sep='-')
print('python','google.com',sep='@')
print()


#end옵션
print('welcome to', end='      ')
print('IT News', end='')
print('Web Site')


#File 옵션
import sys

print('Learn Pythone', file=sys.stdout) #stdout=콘솔아웃
print()

#format 사용 (d=정수, s=문자열, f=실수, o, x)
print('%s %s' %('one', 'two')) # 정확하게 문자열만 와야한다
print('{} {}'.format('one','2')) #포맷함수가 내부적으로 String인지 숫자인지 구별해줌
print('{1} {0}'.format('one','two')) #INDEX

print()

# %s
print('%10s' % ('nice')) #숫자가오면 자릿수를 의미
print('{:>10}'.format('nice'))

print('%-10s' % ('nice')) #음수가 오면 오른쪽으로 채운다
print('{:10}'.format('nice')) #생략하면 오른쪽을 공백으로 채운다

print('{:*>10}'.format('nice')) # 공백이 *로 채워진다
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print()


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))
print()


# %f

print('%f' % (12.123445677777)) #소수 여섯재 짜리까지 나온다.
print('%03.10f' % (10002.123445677777))
print('{:f}'.format(12.123445677777))
print('%06.3f' % (12.123445677777))
print('{:06.2f}'.format(12.123445677777))
print()
