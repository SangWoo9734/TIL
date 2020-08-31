#chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트에 적합
# 규모가 큰 푸로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Park
    Date : 2020.08.30
    """
    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def  __init__(self, company, details):
        self._company = company #인스턴스 변수(인스턴스 각각 가지는 값)
        self._details = details
        self.car_count = 10
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

car1 = Car('car1', {'color' : 'white','horsepower' : 400, 'price' : 8000})
car2 = Car('car2', {'color' : 'black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('car3', {'color' : 'silver', 'horsepower' : 300, 'price' : 6000})

# ID확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

#Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info() #메소드 내 print 가 있으니까 쓸필요 없음
car2.detail_info()

#비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))
print()

#에러
# Car.detail_info(car2)
car2.detail_info()
Car.detail_info(car2)
print()

# 클래스 변수 실행
print(car1.car_count)
print(Car.car_count)
print()

del car2
# 삭제 후 car_count 확인
print(car1.car_count)
print(Car.car_count)


# 인스턴스 네임 스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성가능 (인스턴스 내에서 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))