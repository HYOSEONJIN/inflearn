# 모듈 사용 실습

import sys
import time

print(sys.path)
print(type(sys.path))

## 모듈 경로 삽입 (영구등록방법아님.)
# sys.path.append('D:/JAVA/inflearnPython/math')
#
# print(sys.path)
# import test_module (math안에 06_02를 테스트용으로 복사해서 만들었음)
#
# # 모듈 사용.
# print(test_module.power(10,3))

import Chapter06_02
print(Chapter06_02.add(10,1000000))
