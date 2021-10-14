from Distance import Distance
from Distance import Point

class DistanceAverage():
    def __init__(self, *args):
        self._points = [ p for p in args ]

    def euclidean (self, centroid):
        return round((sum( [ P.distance(centroid) for P in self._points ] ) / len(self._points)), 2)

centroid = Point(3, 7)
A = Point(5, 7)
B = Point(7, 1.3)
C = Point(10, 11)
D = Point(0.9, 11)
E = Point(3, 8)

distance = DistanceAverage(A, B, C, D, E)

print(distance.euclidean(centroid))