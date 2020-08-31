#chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트에 적합
# 규모가 큰 푸로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Park
    Date : 2020.08.30
    Description : Class, Static, Instance Method
    """
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def  __init__(self, company, details):
        self._company = company #인스턴스 변수(인스턴스 각각 가지는 값)
        self._details = details
        #self.car_count = 10


    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price')* Car.price_per_raise)

    #Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print("Succeed! Price increased.")

    #Static Method
    @staticmethod #self, cls 처럼 전달받는 인자가 없음
    def is_car1(inst):
        if inst._company == "car1":
            return "OK! This car is {}".format(inst._company)
        return 'Sorry. This car is not Car1'

car1 = Car('car1', {'color' : 'white','horsepower' : 400, 'price' : 8000})
car2 = Car('car2', {'color' : 'black', 'horsepower' : 270, 'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()


# 가격 정보
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 정보(인상 후)
# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 클래스 메소드 실행
Car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())

# Staticmethod 실행
print(car1.is_car1(car1))
print(car2.is_car1(car2))
print(Car.is_car1(car1))