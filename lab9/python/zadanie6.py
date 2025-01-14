class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

class Car(Vehicle):
    def move(self):
        print(f"Car {self.mark} {self.model} has moved.")

auto = Car("Toyota", "Corolla")
auto.move()