# Chapter06-03
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
# 코루틴(Coroutine)

# 코루틴 : 단일(싱글) 쓰레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 쓰레드
# yield, send : 메인 < - > 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행 (흐름 제어)
# 코루틴 : 루틴 실행 중 정지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글 쓰레드 -> 멀티 쓰레드 -> 복잡 -> 공유되는 자원 -> 교착상태 발생 가능성, 컨텍스트 스위칭 비용이 발생, 자원 소비 가능성 증가
# def -> async, yield -> await

# 코루틴 Ex1
# 함수랑 코루틴이랑 비슷하게 생겼음

def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴
# 제너레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)
# next(cr1) result : >>> coroutine received : None ... StopIteration -> next 했을 때 더이상 나올게 없어서 none 값이 나오면서 StopIteration이 작동함

# 기본 전달값 None 전달
# 값 전송
#cr1.send(100) # result : >>> coroutine received : 100 -> send() 가 next의 기능도 가지고 있다.

# 잘못된 사용
# cr2 = coroutine1()
# cr2.send(100)

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine started : {}'.format(y))
    z = yield x + y
    print('>>> coroutine started : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))
print(next(cr3))

print(getgeneratorstate(cr3)) # Generator의 상태를 출력한다

cr3.send(100)
# cr3.send(100) 여기서 Generator가 끝나지만 StopIterator 오류가 먼저나와서 GEN_CLOSED는 출력되지 않는다.
print()
print()

# 코루틴 Ex3
# StopIteration 자동처리(3.5 -> await)
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1)) StopIteration

t2 = generator1()
print(list(t2))

print()
print()

def generator2():
    yield from 'AB'
    yield from range(1, 4)

t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
#print(next(t3)) StopIteration

