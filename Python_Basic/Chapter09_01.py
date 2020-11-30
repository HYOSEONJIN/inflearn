# chapter09_01
# 파일 읽기 및 쓰기

# 읽기 모드 r 쓰기모드 w 추가모드 a 텍스트모드 t 바이너리모드 b
# 상대경로('../, ./') 절대 경로("C:\django\example..")

# 파일 읽기, 읽기 작업(read)
# 예제1)
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글깨짐 방지

f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

# 속성확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일이름
print(f.name)
# 모드 학인
print(f.mode)

cts=f.read()
print(cts)

#반드시 clos
f.close()


print('--------------------------------------')

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
    # with문에서는 알아서 close해준다.

print('--------------------------------------')


# 예제3
# read() : 전체 읽기, read(10) : 10byte만 읽어옴
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c) # 다음 20byte를 읽어봄. 내가 마지막에 어디까지 읽었는지 내부적으로 기억.
    c = f.read(20)
    print(c)
    f.seek(0,0) # 처음으로 from 0 to 0
    c = f.read(20)
    print(c)
print('--------------------------------------')

# 예제4
# readline : 한줄씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    line = f.readline()
    print(line)
    line = f.readline()
    print(line) #반복문 안에서 읽어오는 것이 좋다.
print('--------------------------------------')

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    cts = f.readlines()
    print(cts)
    print(cts[0])

    for c in cts :
        print(c, end='')

print('--------------------------------------')


# 파일쓰기 (write)

# 예제1
with open('./resource/contents1.txt', 'w') as f :
    f.write('I love Python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f :
    f.write('I love Python\n')       # w로하면 덮어쓰기 a 뒤에추가 (append)

# 예제3
# writelines : 리스트 > 파일로 한줄씩
with open('./resource/contents2.txt', 'w') as f :
    list=['orange\n', 'Apple\n', 'banana\n','melon\n']
    f.writelines(list)

# 예제4
with open('./resource/contents3.txt', 'w') as f :
    print('Test Text Write', file=f) #콘솔이 아니라, 파일로 출력
