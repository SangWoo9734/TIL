# Chapter04-04
# 시퀀스 형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 혀용 x, set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict --> 수정이 불가능한 Dict

from types import MappingProxyType
# MappingProxytype 은  직접적으로 수정/삭제가 이루어질 수 없으며
# 변경하기 위해서는 직접 객체를 복사하여 수정해야한다. 원본 수정 X
# 원본 데이터를 수정할 수있게 하고 싶지 않은 경우에 사용한다.

d = {'key1' : 'value1'}

# MappingProxyType을 사용함으로써 Read Only로 만들어준다.
d_frozen = MappingProxyType(d)

#hash(d) --> Dict 는 해쉬가 불가능
print(d, id(d))
print(d_frozen, id(d_frozen))


# 수정가능
d['key2'] = 'value2'
print(d)

# 수정 불가 'Read Only'
# d_frozen['key2'] = 'value2'
# result : TypeError: 'mappingproxy' object does not support item assignment

print()
print()

# Set
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = {} # reslut -> <class 'dict'>
print(type(s4)) 
s5 = set()
s6 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}) # Read Only

# 추가가능
s1.add('Melon')
print(s1)

# 추가 불가능
# frozenset 은 ReadOnly 이므로 추가 불가능
#s6.add("Melon") result -> AttributeError: 'frozenset' object has no attribute 'add'

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))
print(s6, type(s6))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print('--------------')
print(dis('{10}'))  # 실행 속도가 아래의 set([10]) 보다 비교적 빠름
print('--------------')
print(dis('set([10])'))

# 지능형 집합 (Comprehending Set)

print('-------------')

from unicodedata import name
# 들어온 값을 문자열로 바꾸고 해당 문자가 없는 경우에는 valueerror 또는 선언한 값으로 출력한다.
print({name(chr(i), '') for i in range(0, 256)})