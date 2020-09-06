# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built in, 이미 만들어 놓은) 메소드

# 파이썬 데이터 모델

# 기본형
print(int(10))
print(int) # result : <class 'int'>
print(float) # result : <class 'float'>

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100) # 내부적으로 .__add__  가 실행된 것이다.
print(n.__add__(100)) # 사실상 이렇게 동작 한다.
#print(n.__doc__) # int class에 대한 코멘트가 출력
print(n.__bool__(), bool(n)) # return : True
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제 1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def __str__(self):
        return "Fruit Class Info : {} , {}".format(self._name, self._price)

    def __add__(self, x):
        print("called __add__")
        return self._price + x._price
    
    def __sub__(self, x):
        print("called __sub__")
        return self._price - x._price

    def __le__(self, x): # 작거나 같다
        print("called __le__")
        if self._price <= x._price:
            return True
        else :
            return False

    def __ge__(self, x): # 크거나 같다
        print("called __ge__")
        if self._price >= x._price:
            return True
        else :
            return False

# 인스턴스 생성
s1 = Fruit('orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2) # 클래스 method 중 __add__ 가 사용된다. (s1 == self, x == s2)

# 일반적인 계산
# print(s1._price + s2._price)

# 매직 메소드
print(s1 >= s2) # __ge__
print(s1 <= s2) # __le__
print(s1 - s2) # __sub__
print(s2 - s1)
print(s1)
print(s2)

print()
print()

