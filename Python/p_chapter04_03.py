# Chapter04-03
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, set, dictionary, collections.deque])
# ex) a = [3, 3.0, 'A']
# 플랫 (Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변( list, bytearray, array.array, memoryview, deque )
# 불변( tuple, str, bytes )

# 해시 테이블
# Key에 Value를 저장하는 구조를 의미 __dir__
# 파이썬 dict 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조

# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인 --> 고유하다
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) 예외 발생 

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
            ('k1', 'var2'),
            ('k2', 'var3'),
            ('k2', 'var4'),
            ('k2', 'var5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else :
        new_dict1[k] = [v]

print(new_dict1)


# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의 사항 -> 반복될 때마다 값이 덮어진다.
new_dict3 = {k : v for k, v in source}

print(new_dict3)