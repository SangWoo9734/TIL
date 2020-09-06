# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built in) 메소드

# 클래스 예제 2
# 벡터(x, y)
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50, 15)
# Max((5, 10)) = 10

# 패킹(Packing) : 여러개의 값을 하나의 변수에 저장, 대입 하는 것
# 언패킹(Unpacking) : 패킹되어있는 변수 내부의 값을 하나씩 꺼내여 대입, 사용하는 것

class Vector(object) :
    def __init__(self, *args): # Packing
        '''
        Create a vector, example : v = Vector(5, 10)
        ''' # __init__.__doc__

        # Unpacking
        if len(args) == 0:
            self._x, self._y = 0, 0
        else :
            self._x, self._y = args

    def __repr__(self):
        '''
        Return the vector imformations.
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''
        Return add Value of two vectors
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        # print("IF return False! It is (0, 0)")
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직 메소드 출력
print(Vector.__init__.__doc__) # 각 메소드의 코멘드를 출력
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 10)
print(v2 * 2)
print(bool(v1), bool(v2))
print(bool(v3))