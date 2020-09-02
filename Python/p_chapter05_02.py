# Capter05-02
# 일급 함수 (일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) NameError: name 'b' is not defined

#Ex2
b = 20 # 전역변수

def func_v2(a): # 지역 변수
    print(a)
    print(b)

func_v2(10)

# Ex3
c = 30

def func_v3(a): # 지역 변수
    print(a)
    # print(c) UnboundLocalError: local variable 'c' referenced before assignment
    c = 40
    print(c)

print('>>', c)
func_v3(10)
print('>>>', c)

# Closure(클로저) 사용이유
# 지역 변수의 경우 scope를 벗어나면 소멸된다. Closure는 이러한 변수들을 '기억'한다.
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 한정된 메모리 공간에 여러 자원이 접근 -> 교착 상태 (Dead Lock)에 빠지는 것을 방지
# 메모리를 공유하지 않고 메세지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점
# Point !! --> Closure 는 상태를 기억한다. 불변 상태

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적 (함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = [] # 여기서 이전 상태를 함수가 종료 되어도 계속 가지고 있음

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()

print(dir(averager_cls))

# 누적
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(103))