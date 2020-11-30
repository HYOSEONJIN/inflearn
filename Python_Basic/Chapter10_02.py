# chapter10_02
# hangman(행맨) 미니게임제작(2)
# 프로그램 완성 및 최종 테스트.


import time
import csv
import random
import winsound

# 처음인사
name = input("what is your name?")

print("hi, "+ name, "time to play hangman game!")

print()

time.sleep(1) #뭔가있는 것처럼 보이기 위해 1초쉼

print("Start Loading..")
print()
time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 csv 파일 로드.

with open('./resource/word_list.csv','r') as f :
    reader = csv.reader(f)
    # 헤더스킵
    next(reader)
    for c in reader :
        words.append(c)


# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

# 정답 단어 / 공백제거
word = q[0].strip()

# 추측단어

guesses = ''

# 기회
turns = 10

# 핵심 while Loop
# 찬스 카운트가 남아있을 경우
while turns > 0 :
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word :
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses :
            # 추측단어 출력
            print(char, end='')
        else :
            # 틀린경우 대시로 처리
            print("_", end='')
            failed +=1
    #단처 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        # 성공사운드
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations!')
        # while문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character.")

    # 단어더하기
    guesses += guess

    # 정답 단어에 추측한 문어가 포함되어 있지 않으면
    if guess not in word:
        # 기회횟수 감소
        turns -=1
        # 오류메세지
        print("oops! wrong")
        # 남은 기회 출력
        print("You have", turns, 'more guesses!')


        if turns == 0 :
            # 실패사운드
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 실패 메세지
            print("you failed ! bye!")
