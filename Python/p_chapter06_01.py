# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제너레이터 
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... : Iterable

# 반복 가능한 이유 : 내부적으로 iter(x) 함수가 호출 되었다.
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in t:
    print('>', c)


# while
w = iter(t)

print(next(w)) # result : A
print(next(w)) # result : B
print(next(w)) # result : C
print(next(w)) # result : D

while True :
    try :
        print(next(w))
    except StopIteration :
        break

print()

# 반복형 확인

from collections import abc

print(dir(t)) # dir 내에 __iter__ 확인
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()
print()

# next
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError :
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter("Do today what you could do tomorrow")

print(WordSplitter)

print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))  StopIteration: Stopped Iteration.

print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제너레이터 사용을 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터 yield 를 사용함으로써 index를 사용하지 않고도 다음 값의 위치전달 해준다(?)
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator("Do today what you could do tomorrow")

wt = iter(wg)

print(wt) # result : <generator object WordSplitGenerator.__iter__ at 0x000001DEA780ECF0>
print(wg) # result : WordSplitGenerator(['Do', 'today', 'what', 'you', 'could', 'do', 'tomorrow'])

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt)) Error : StopIteration

print()
print()