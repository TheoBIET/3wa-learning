from random import (randint as ri, shuffle as sh)
class Matrix: 
    def __init__(self, row, col, min=0, max=100):
        self._row = row
        self._col = col
        self._matrix = [[ri(min, max) for i in range(col)] for j in range(row)]

    @property
    def row(self):
        return self._row
    
    @property
    def col(self):
        return self._col
    
    @property
    def matrix(self):
        return self._matrix
    
    def __str__(self):
        return str(self.matrix)

    def shuffle_row(self):
        sh(self.matrix)


matrix = Matrix(9, 9)
print(matrix)
matrix.shuffle_row()
print(matrix)


