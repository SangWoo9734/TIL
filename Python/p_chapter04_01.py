# Chapter04-01
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, set, dictionary, collections.deque])
# ex) a = [3, 3.0, 'A']
# 플랫 (Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변( list, bytearray, array.array, memoryview, deque )
# 불변( tuple, str, bytes )

# 리스트 및 튜플 고급

# 지능형 리스트 (Comprehending lists)
chars = '+_)(*&^%$#@!)'

# char[2] = a -> str 상태의 데이터는 변경이 불가능하다.
code_list1 = []

for s in chars :
    #유니코드 리스트
    code_list1.append(ord(s)) # ord() -> 문자를 아스키 코드로 변환

print(code_list1)

# Comprehending lists
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
#filter((익명)함수, 처리할 데이터)
print(code_list4)


print()
print('전체 출력(유니코드)')
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print('전체 출력(문자)')
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

# Generator 생성 --> 연속되는 값을 만들어 낸다.
import array 

# Generator : 한 번에 한 개의 항목을 생성( 메모리 유지 X )
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars)) # --> 'I' == int
print(type(tuple_g))
print(next(tuple_g)) # --> next() 로 하나 씩 출력
print(type(array_g))
print(array_g)
print(array_g.tolist()) # --> array 상태를 리스트로 바꾸어 준다.

# Generator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s) # --> 하나하나 만들면서 하나하나 출력

# 리스트 주의 (deep copy, shallow copy)
marks1 = [['~'] * 3 for _ in range(4)] # 반복문 사용시 사용하지 않는 변수는 '_'로도 사용 가능하다.
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)
print()
# 수정
marks1[0][1] = 'X' # 새로운 주소에 할당 되어 여러번 반복된 값들의 주소는 중복이 발생하지 않는다.
marks2[0][1] = 'X' # 의도하지 않은 값의 변경이 발생한다 하나의 주소값이 여러번 복사되어 전체 데이터에 영향을 준다

print(marks1)
print(marks2)

# 확인
print([id(i) for i in marks1]) # result : [22038608, 22038568, 22038528, 22038488]
print([id(i) for i in marks2]) # result : [22038448, 22038448, 22038448, 22038448]
