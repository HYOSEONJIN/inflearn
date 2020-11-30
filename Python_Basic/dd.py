import time
import csv
import random
import winsound

# 처음인사
 #뭔가있는 것처럼 보이기 위해 1초쉼

print("Start Loading..")
print()

# csv 단어 리스트
words = []

# 문제 csv 파일 로드.

with open('./resource/word_list.csv','r') as f :
    reader = csv.reader(f)
    # 헤더스킵
    next(reader)
    for c in reader :
        words.append(c)


print(words)
print(words[0])
print(words[0][1])
