# chapter03_02
# 파이썬 문자형

# 문자열 생성
str1= "I am Python"
str2= 'python'
str3= """How are you?"""
str4= '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1)) #문자열의 길이

# 빈문자열
str1_t1="" # or str_t1=''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2)) # 둘다 STR, 길이는 0


# 이스케이프 문자 사용 # 탈출 문자
# I'm Boy >> '
print("I'm Boy")  #print('I'm Boy')
print('I\'m Boy')
print('\' , \\ , \t tap, \n enter')
#등등등, 자바와 같은 느낌, 이스케이프 문자 검색해보기
escape_str1="do you have a \"retro games?\""
print(escape_str1)
escape_str2='what\'s on TV?'
print(escape_str2)
# 탭, 줄바꿈
t_s1= "click \t start!"
t_s2="new Lint \n check!"
print(t_s1)
print(t_s2)
print()
# Raw String -  있는 그대로 표시해준다
raw_s1=r'd:\python\test'
print(raw_s1)
print()

# 멀티라인 입력
# 역슬래시를 사용하면 유용하다
multi_str= \
"""
String
multi Line
test
"""
multi_str2="""
string
multi Line
test2
"""

print(multi_str)
print(multi_str2)
print()


# 문자열 연산 (String에서 in 연산자를 쓸 수 있다는 점을 기억하자)
str_o1= "python"
str_o2= "Apple"
str_o3= "How are you doing"
str_o4= "Seoul Daejeon busan"

print(str_o1 * 3 ) #세번반복되서 출력
print(str_o1 + str_o2)
print('y' in str_o1) # str_o1안에 y가 있어? (True/False) > 시퀀스 형에 사용가능
print('P' not in str_o2) #대문자 소문자 구별함
print()

# 문자열 형변환
print(str(66), type(str(66))) # 문자66을 의미.
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()


# 문자열 함수 (upper, iaalnum, startswith, count, endswith, isalpha ... )
print("Capitalize : ", str_o1.capitalize()) #첫글자를 대문자로 바꿔준다.
print("endswith? : ", str_o2.endswith("e")) #마지막 문자가 무엇인지 체크 boolean (ex 마침표)
print("replace : ", str_o1.replace("py","PPYY")) #바꿔줌
print("sorted : ", sorted(str_o1)) # 리스트 형태로 반환
print("split : ", str_o4.split(" ")) # 기준을 정해서 그것을 기준으로 리스트로 반환
print()

# 반복(시퀀스)
im_str= "good boy!"

print(dir(im_str)) #__iter__(반복) #im_str에서 사용하는 모든 것 나열

#출력 (슬라이스 가능)
for i in im_str :  print(i)
print()


# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))
# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2
print(str_s1[:3]) # 처음부터 세개. 위에거랑 같음
print(str_s1[5:11])
print(str_s1[5:]) # 5부터 끝까지, 위에거랑 같음
print(str_s1[:len(str_s1)]) #끝부분의 길이를 모를때는 len이용 #[:11]
print(str_s1[:len(str_s1)-1]) #[:10]
print(str_s1[1:9:2]) # 세번째 인수는 단위, 몇개단위로 출력
print(str_s1[-5:]) #뒤에서는 -1부터 시작한다
print(str_s1[1:-2])
print(str_s1[::2]) #처음부터 끝까지 2칸간격으로
print(str_s1[::-1]) #역으로 출력됨
print()

# 아스키코드(또는 아스키코드)
a ='z'

print(ord(a)) # 아스키코드로,
print(chr(122)) # 문자로,
