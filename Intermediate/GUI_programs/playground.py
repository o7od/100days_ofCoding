# Unlimited positional arguments   *args collects arguments into a tuple
def add(*args):
    print(args)
    return sum(args)


total_num = add(1, 2, 34, 5312, 323, 1231, 421, 222)
# print(total_num)

# Unlimited keyword arguments **kwargs collects into a dictionary
def calculate(n, **kwargs):
    result = n + kwargs["add"]
    result = result * kwargs["multiply"]
    print(result)


calculate(20, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

car = Car(make="Nissan")
print(car.model)