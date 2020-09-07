# Chapter04-02
# 시퀀스 형
# 컨테이너(Container : 서로다른 자료형[list, tuple, set, dictionary, collections.deque])
# ex) a = [3, 3.0, 'A']
# 플랫 (Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변( list, bytearray, array.array, memoryview, deque )
# 불변( tuple, str, bytes )

# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9)) # divmod 몫과 나머지를 반환, result : (11, 1)
print(divmod(*(100, 9))) # *() --> Unpacking, result : (11, 1)
print(*(divmod(100, 9))) # result : 11, 1

print()

x, y, *rest = range(10) # 차례대로 x, y 값이 할당되고 나머지 값이 패킹 되어 rest에 할당된다.
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5 # 괄호없이 그냥 선언하면 Tuple
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25) # Tuple : 가변
m = [15, 20, 25] # List : 불변

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l)) # 불변 자료형을 다룰때 불변 자료형은 변경이 불가능하므로 새로운 주소값에 저장된다
print(m, id(m)) # 동일한 주소값에서 처리된다.

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환, 원본 변경 X
f_list = ['orange', 'apple', 'mango', 'coconut', 'lemon', 'strawberry', 'papaya']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True)) # defult = False 역 정렬 출력
print('sorted - ', sorted(f_list, key=len)) # 변수의 길이에 따라 정렬
print('sorted - ', sorted(f_list, key=lambda x : x[-1])) # 익명함수를 사용하여 정렬기준 설정, 역 정렬 출력 
print('sorted - ', sorted(f_list, key=lambda x : x[-1], reverse=True))


print(f_list)

print()
# sort : 정렬 후 객체(원본)를 직접 변경

# 반환 값 확인 (None)
print('sort - ', f_list.sort(), f_list) # .sort() 까지만 쓰면 원본 변경만 하고 출력은 안됌 출력값 : None
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x : x[-1], reverse=True), f_list)


# List vs Array 적합한 사용 설명서
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)