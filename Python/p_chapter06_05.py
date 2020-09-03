# Chapter06-05
# Futures 동시성
# 비동기 작업 실행
# 동기 실행 : A 작업이 끝나는동안 다른 작업이 시작될 수 없음 <-> 비동기
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상


# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩 / 멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소 , 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL : Global Interpreter Lock : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스하는 경우 => 문제점을 반지하기 위해 
#                                 GIL 실행, 리소스 전체에 락이 걸림 -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed, wait

WORK_LIST = [10000, 100000, 1000000, 10000000] #각 원소 까지 의 합을 구해보자

# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (제너레이터)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait
# as_complete
def main():
    # Worker Count
    # worker = min(10, len(WORK_LIST)) #  worker의 수가 미정일 때는 이렇게도 코딩한다.

    # 시작시간
    start_tm = time.time()
    # Futures
    futures_list = []
    # 결과 건수
    # ProcessPoolExcutor
    # with futures.ProcessPoolExecutor() as excutor :
    with ProcessPoolExecutor() as excutor :
        for work in WORK_LIST :
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print('Scheduled For {} : {}'.format(work, future))
            print()

        # # wait 결과 출력
        # result = wait(futures_list, timeout=7) # 작동시간을 7초 까지만 출력
        # # 성공
        # print('Completed Tasks : ' + str(result.done))
        # # 실패
        # print('Pending ones after waiting for 7seconds : ' + str(result.not_done))
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result =  future.result()
            done = future.done()
            cancelled = future.cancelled

            #future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))
    # 종료시간
    end_tm = time.time() - start_tm

    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_tm))

# wait : Future 인스턴스들이 완료할 때 까지 기다린다. 대기할 최대 시간(초)를 제어할 수 있다.
# as_completed : 먼저 끝나는대로 yield 된다. 

# 실행
if __name__ == '__main__':
    main()