# Capter05-03
# 일급 함수 (일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# Closure 사용
def closure_ex1():
    # Free variable : 함수영역 바깥에서 선언된 변수
    # 클로저 영역
    series = [] 
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series, len(series)))
        return sum(series)/len(series)
    return averager # 함수 결과 반환 가능(return) 05_01 참고


avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars) # return : ('series',)
print(avg_closure1.__closure__[0].cell_contents)

print()
print()

# 잘못된 클로저 사용
def closure_ex2():
    # Free Variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1        # 현재 함수 내에 cnt, total 변수의 선언이 안되어있음.
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()

print(avg_closure2(10)) # UnboundLocalError: local variable 'cnt' referenced before assignment\

print(avg_closure2(15))
print(avg_closure2(35))
print(avg_closure2(40))
