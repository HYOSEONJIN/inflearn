# Chapter09_02
# csv 파일 읽기 및 쓰기

# csv : meme - text/csv;

import csv

# 예제1
with open('./resource/test1.csv','r') as f :
    reader = csv.reader(f)
    next(reader) #header (첫줄) skip

    # 객체확인
    print(reader)

    # 타입확인
    print(type(reader))

    # 속성확인
    print(dir(reader))
    print()

    # 내용 출력
    for c in reader :
        #print(c)
        #print(type(c)) #list~~
        print(''.join(c))


# 예제2
with open('./resource/test2.csv','r') as f :
    reader = csv.reader(f,delimiter='|') # 구분자

    for c in reader:
        print(c)
        # 리스트안에 각각 두개 ['나라','약자']로 가져옴

# 예제3
with open('./resource/test1.csv','r') as f :
    reader = csv.DictReader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        #print(c) #{'Name|Code': 'Zimbabwe|ZW'}
        for k,v in c.items():
            print(k,v)
        print('--------------------')


# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]
with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt=csv.writer(f)

    #dic확인
    #print(dir(wt))

    for v in w :
        wt.writerow(v) # 한줄씩 입력.row단위로.

# 예제5
with open('./resource/write2.csv', 'w', encoding='utf-8') as f:
    # 필드명
    fields = ['one', 'two','three']

    #DictWriter

    wt = csv.DictWriter(f, fieldnames=fields)
    #header Writer
    wt.writeheader()

    for v in w :
        wt.writerow({'one': v[0],'two':v[1],'three':v[2]})
