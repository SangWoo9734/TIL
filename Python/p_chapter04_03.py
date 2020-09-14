# Chapter04-03
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, set, dictionary, collections.deque])
# ex) a = [3, 3.0, 'A']
# 플랫 (Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변( list, bytearray, array.array, memoryview, deque )
# 불변( tuple, str, bytes )

# 해시 테이블
# Key에 Value를 저장하는 구조를 의미 python의 기본적 저장 형태 -> 예) __dict__
# 파이썬 dict -> 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조
# Google hash table 검색

# 해시 함수(Hash Function) : '키'를 해시로 변경해주는 함수
# 즉, 문자열로 들어온 인풋 데이터를 해시 함수를 통해 숫자열로 변경해주고,
# 이 숫자를 키 값으로 삼아 배열에 값을 저장하는 구조

# 문제점
# 해시 충돌 (Hash Collision)
# 인풋 데이터를 해시 값으로 바꿔주는 과정에서 두 데이터가 다른 문자열임에도
# 불구하고, 같은 숫자로 변환되는 경우

# 해결 방법
# 오픈 해싱 (Open Hashing) == 체이닝 기법 (Separate Chaining)
# 해시 값이 중복될 경우, 먼저 저장된 데이터에 링크드 리스트를 이용하여 데이터 연결
# 링크드 리스트가 아니더라도 이중 리스트 구조로 해결 가능하다.
# Dict 구조

# 클로즈드 해싱(Closed Hashing) == Linear Probing, Open Addressing
# 해시 값이 중복되는 경우
# 나중에 들어온 해시의 키값을 해당 해시 값 부터 순차적으로 빈 공간을 검색
# 저장 효율이 가장 높은 방법

print(__builtins__.__dict__)

# Hash 값 확인 --> 고유하다
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50]) # -> 리스트는 가변형 데이터이므로 해시값 할당이 불가능하다

print(hash(t1))
# print(hash(t2)) 예외 발생 

print()
print()

# Dict Setdefault 예제 -> tuple 에서 dict 로 변환시 빠르게 변환 가능
# 설명 : 키 값과 값 하나를 인자로 받고 키값이 있다면 키값을 반환, 없으면 두번쨰 인자를 반환
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


# Use Setdefault -> 
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의 사항 -> 반복될 때마다 값이 덮어진다.
new_dict3 = {k : v for k, v in source}

print(new_dict3)