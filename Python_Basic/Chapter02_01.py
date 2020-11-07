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
print('{1} {0}'.format('one','two'))
