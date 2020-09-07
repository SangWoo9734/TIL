# Chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플 값의 변경이 불가능 하다.
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)

# 네임드 튜플 ㅣ 클래스와는 다른 Collection 모듈의 일종, tuple 이면서 Dictionary 값을 가지고 있다.
# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)


l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # class 와 같이 예약어인 경우 변수 명으로 사용할 때 rename을 사용하여 재설정 한다. Default = False

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=12, y=321)
p2 = Point2(20, 40)
p3 = Point3(20 , y = 23)
p4 = Point4(10, 20, 30, 40) # 결과 : Point(x=10, y=20, _2=30, _3=40) -> 중복 되는 key 값이나 예약어는 알아서 난수를 생성하여 값을 할당.
p5 = Point3(**temp_dict) # dict 자료형을 unpacking하여 값을 할당

print()
print(p1)
print(p2)
print(p3)
# rename 테스트
print(p4)
print(p5)


# 사용
print(p1[0] + p2[1]) # 인덱스로 접근
print(p1.x + p2.y) # 키로 접근

x, y = p3 # unpacking
print(x, y)

# 네임트 튜플 메소드
temp = [52, 38]

#._make() : 새로운 객체를 생성
p4 = Point1._make(temp) # list 를 namedTuple로 만들어 주는 method -> _make, 변수의 개수를 맞춰 주어야 한다.

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict()) # result => OrderedDict([('x', 12), ('y', 321)])
print(p4._asdict())

# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)

Classes = namedtuple("Classes", ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()


# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers] # 총 80 명의 학생 객체 생성

# 추천
students2 = [Classes(rank, number)
                for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1, 21)]]

print(len(students))
print(len(students2))

# 출력
for s in students2 : 
    print(s)