# chapter06_03
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리) .(현재 디렉토리) > 모듈 내부에서만 사용

#__pycache__ : 파이캐시 빠른실행을 위해 파이썬이 만듦 삭제가능 > 어차피 실행하면 또생김

#__init__.py : python3.3부터는 없어도 패키지로 인식
# 과거에는 init 파일이 없으면 import를 할 수 없었다.
# > 단 하위 호환을 위해 작성 추천,


# 예제1

import sub.sub1.module1 # 같은 경로일떄는 이렇게 가져오기도.
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 #별칭 alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *
from sub.sub2 import *
# 전체가져오기 > 하지만 필요한 것만 가져오는 것이 좋다.

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()
