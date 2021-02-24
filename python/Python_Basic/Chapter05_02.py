# chapter05_02
# 파이선 사용자 입력
# Input 사용법
# 기본 타입(Str)

# 예제1

name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company : ")

print(name, grade, company)

# 예제2

number = input("enter number :")
name = input("enter name : ")
print("type : ", type(number), type(name)) #둘다 str로받는다.

# 예제3 (계산)
first_number = int(input("number 1 : "))
second_number = int(input("number 2 : "))

print("두수의 합 : " , first_number+second_number)

# 예제4
float_num = float(input("enter float number : "))
print("num : " float_num)
print("type : " type(float_num))

# 예제5
print("FirstName - {0}, LastName - {1}"
.format(input("enter first name : "),input("enter second name : ")))
