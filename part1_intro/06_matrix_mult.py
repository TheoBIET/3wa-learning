
first_matrice = [[3, 12, 4], [5, 6, 8], [1, 0, 2]]
second_matrice = [[7, 3, 8], [11, 9, 5], [6, 8, 4]]

def matrix_multiply(a, b):
    result = []
    for a_col in range(len(a[0])):
        result_col = []
        for b_col in range(len(b[0])):
            calcSum = 0
            for a_row in range(len(a)):
                calcSum += a[a_col][a_row] * b[a_row][b_col]
            result_col.append(calcSum)
        result.append(result_col)
    return result

def matrix_multiply_fact(a, b):
    return [[sum(a[a_col][a_row] * b[a_row][b_col] for a_row in range(len(a))) 
        for b_col in range(len(b[0]))] 
        for a_col in range(len(a[0]))]

print(matrix_multiply_fact(first_matrice, second_matrice))