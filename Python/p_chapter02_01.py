#chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트에 적합
# 규모가 큰 푸로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량 1
car_company_1 = 'car1'
car_detail_1 = [
    {'color' : 'white'},
    {'horsepower' : 400},
    {'price' : 8000}
]

#차량 2
car_company_2 = 'car2'
car_detail_2 = [
    {'color' : 'black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

# 차량 3
car_company_3 = 'car4'
car_detail_3 = [
    {'color' : 'silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

# 자료가 많아질 수록 데이터의 양도 그에 따라 엄청나게 증가

# 리스트 구조 -> 시퀀스라고 도 한다 -> 순서가 있는 데이터의 모임
# 관리하기가 불편
# 인덱스로 접근시 실수 발생 가능성이 높음, 삭제 불편 (인덱스를 반드시 알아야 접근가능)
car_company_list = ['car1', 'car2', 'car3']
car_detail_list = [
    {'color' : 'white','horsepower' : 400, 'price' : 8000},
    {'color' : 'black', 'horsepower' : 270, 'price' : 5000},
    {'color' : 'silver', 'horsepower' : 300, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list, car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복이 지속, 중첩문제(키는 중첩을 허용하지 않음)
car_dicts = [
    {'car_compay': 'car1', 'car_detail': {'color' : 'white','horsepower' : 400, 'price' : 8000}},
    {'car_compay': 'car2', 'car_detail': {'color' : 'black', 'horsepower' : 270, 'price' : 5000}},
    {'car_compay': 'car3', 'car_detail': {'color' : 'silver', 'horsepower' : 300, 'price' : 6000}}
]


del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드를 활용

class Car():
    def  __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # 비공식적인, 사용자 입장에서의 출력을 원할 떄 사용
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): # 객체, 자료형의 타입에 따른 객체를 그대료 출력할 경우에 사용
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('car1', {'color' : 'white','horsepower' : 400, 'price' : 8000}) # 기본적으로 __str__ 을 출력, 없으면 __repr__ 출력
car2 = Car('car2', {'color' : 'black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('car3', {'color' : 'silver', 'horsepower' : 300, 'price' : 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__) # 객체의 attribute 값들을 출력해준다
print(car2.__dict__)
print(car3.__dict__)

print()
print()

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(x)