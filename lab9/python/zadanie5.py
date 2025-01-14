class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def countS(self):
        return self.length * self.width

    def countP(self):
        return 2 * (self.length + self.width)

Rect1 = Rect(5, 3)
print("Pole:", Rect1.countS())
print("Obwód:", Rect1.countP())