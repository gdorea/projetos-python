def add(*args):
    return sum(args)

print(add(2, 43, 17))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.make)