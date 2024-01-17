# def add(*args):
#     summ = 0
#     for n in args:
#         summ += n
#     return summ


# def calculate(**kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     print(kwargs["add"])
#
#
# calculate(add=5, multiply=7)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="nissan")
print(my_car.model)
