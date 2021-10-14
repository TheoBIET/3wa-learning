from math import sqrt

class Distance:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def euclidean(self):
        return round(sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2), 2)

class Point(Distance):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def distance(self, other):
        return Distance(self, other).euclidean()

A = Point(5, 7)
B = Point(15, 1)
distance = Distance(A, B)

print(distance.euclidean())
print(A.distance(B))