from random import (randint)
from math import (pi, dist)

class Circle:
    shoot_number = 1000
    circle_position = (0, 0)

    def __init__(self, radius, target_size=20):
        self._radius = radius
        self._target_size = target_size
        self.simulate()

    def simulate(self):
        size = self.target_size
        shoots = [(randint(size / 2 * -1, 0), randint(0, size / 2)) for shoot in range(self.shoot_number)]
        correct = [shoot for shoot in shoots if dist((0, 0), shoot) <= self.radius]
        return len(correct) / len(shoots) * 100

    def theory_value(self):
        target_area = self.target_size * self.target_size
        circle_area = pi*self.radius**2
        return (circle_area / target_area) * 100

    @property
    def radius(self):
        return self._radius
    
    @property
    def target_size(self):
        return self._target_size


circle = Circle(2)
print(f"Impact Ratio for {circle.shoot_number} shoot(s): {round(circle.simulate(), 3)}%")
print(f"Theoric Value : {round(circle.theory_value(), 3)}%")