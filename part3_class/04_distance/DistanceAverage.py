from Distance import (Distance, Point)

class DistanceAverage():
    def __init__(self, *args):
        self._points = [ p for p in args ]
        self._precision = 2

    def euclidean (self, centroid):
        return round((sum( [ P.distance_euclidean(centroid) for P in self._points ]) / len(self._points)), self.precision)

    def absolute (self, centroid):
        return round((sum( [ P.distance_absolute(centroid) for P in self._points ]) / len(self._points)), self.precision)

    @property
    def precision(self):
        return self._precision
    
    @precision.setter
    def precision(self, value):
        self._precision = value

centroid = Point(3, 7)
A = Point(5, 7)
B = Point(7, 1.3)
C = Point(10, 11)
D = Point(0.9, 11)
E = Point(3, 8)

distanceAvg = DistanceAverage(A, B, C, D, E)

print(distanceAvg.euclidean(centroid))
print(distanceAvg.absolute(centroid))