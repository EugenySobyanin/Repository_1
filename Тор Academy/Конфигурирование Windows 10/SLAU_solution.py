def printMatrix(matrix):
    """Функция печати матрицы на экран"""

    for row in matrix:
        print(row)


def sumMatrix(matrixA, matrixB):
    """Суммирование двух матриц"""

    result = []

    #На каждой итерации цикла будем формировать
    # очередной столбец результирующей матрицы
    for row in range(len(matrixA)):
        nextRow = []
        for column in range(len(matrixA[row])):
            nextRow.append(matrixA[row][column]+matrixB[row][column])
        result.append(nextRow)

    return result

#Пример генератора списка. Инструмент из функционального программирования
    #По сути сворачиваем привычный цикл
    # for i in range():
    #   numbers.append(i)
    # В лакончиную конструкцию

    #numbers = [number for number in range(2,100,2)] # натуральные четные числа до 100


def mulNumberAndMatrix(number, matrixA):
    """Умножение матрицы на число"""
    #Поэлементное копирование с помощью генератора списка
    result = [[column for column in row] for row in matrixA] 
      
    for row in range(len(result)):
        for column in range(len(matrixA[row])):
            result[row][column] *= number

    return result

def subtractMatrix(matrixA, matrixB):
    """Вычитание двух матриц"""

    #Определили вычитание как А + (-1)*В
    return sumMatrix(matrixA, mulNumberAndMatrix(-1,matrixB))

def mulMatrixAndMatrix(matrixA, matrixB):
    """Уможение двух матриц"""
    result = []

    #Результирующая матрица будет иметь размеры mA на nB,
    #где mA - количество строк матрицы A
    #nB - количество столбцов матрицы В
    for i in range(len(matrixA)):
        result.append([0]*len(matrixB[0]))

    #Первые два цикла - формируем каждый элемент результирующей матрицы
    #Вложенный цикл - умножение по столбцам и строкам
    for i in range(len(result)):
        for j in range(len(result[i])):
            for k in range(len(matrixA[0])):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
                
    return result

def minor(matrix,target_row,target_column):
    # TODO: Переписать решение с помощью генератора
    # return [[column for column in matrix if column != target_column] for row in matrix if row != target_row]
    
    rows = len(matrix)
    columns = len(matrix[0])
    minorMatrix = []
    for i in range(rows):
        if i != target_row:
            nextRow = []
            for j in range(columns):
                if j != target_column:
                    nextRow.append(matrix[i][j])
            minorMatrix.append(nextRow)

    return minorMatrix



def determinant(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    det = 0

    #Граничный случай - завершаем рекурсию для матрицы 1 на 1
    if rows == 1 and rows==columns:
        return matrix[0][0]
    
    #Разложение по первой строке
    for k in range(columns):
        minorTmp = minor(matrix,0,k)
        detTmp = determinant(minorTmp)
        det += ((-1)**k) * matrix[0][k] * detTmp
    
    return det


def replace_column(matrixA,matrixB,columnTo, columnFrom):
    """Заменить столбец columnTo в matrixA 
    на столбец columnFrom из matrixB"""
    answer = []

    for row in range(len(matrixA)):
        nextRow = []
        for column in range(len(matrixA[row])):
            if(column != columnTo):
                nextRow.append(matrixA[row][column])
            else:
                nextRow.append(matrixB[row][columnFrom])
        answer.append(nextRow)

    return answer

def solve_Kramer(matrix_coef, matrix_free):
    """Решение СЛАУ методом Крамера
    Возвращает список корней уравнения"""
    #TODO: Если main_det == 0 у СЛАУ нет корней
    main_det = determinant(matrix_coef)
    solution = []
    for column in range(len(matrix_coef[0])):
        next_det = determinant(replace_column(matrix_coef,matrix_free,column,0))
        solution.append(next_det/main_det)
    return solution    


#TODO: Нужно протестировать на ошибки
def parse_input(input:str):
    """Перевод строкового ввода пользователя 
    в матрицу свободных коэффициентов и матрицу свободных членов.
    Возвращает список, где нулевой элемент - матрица коэффициентов
    первый элемент - матрица свободных членов."""
    equations = input.strip().split('\n') #Разбили по уравнениям
    equation_length = len(equations[0].strip().split(' '))
    matrix_coef = []
    matrix_free = []
    for equation in equations:
        coefs = equation.strip().split(' ')
        if(len(coefs) != equation_length):
            return ["Ошибка ввода уравнений"]
        equation_length = len(coefs)
        nextRowCoef = []
        nextRowFree = []
        for element in range(len(coefs)):
            try:
                if( element != len(coefs)-1):
                    nextRowCoef.append(float(coefs[element]))
                else:
                    nextRowFree.append(float(coefs[element]))
            except ValueError:
                return ["Введено не число"]
        matrix_coef.append(nextRowCoef)
        matrix_free.append(nextRowFree)
    return [matrix_coef,matrix_free]
        

input = open('matrix.txt').read()
parsed = parse_input(input)
coefs = parsed[0]
print("Матрица коэффициентов:")
printMatrix(coefs)
free = parsed[1]
print("Матрица свободных членов:")
printMatrix(free)
#TODO: Красиво оформить вывод уравнения в виде: 5.0 * x1 - 6.0 * x2 + 13.5 * x3 = 150
print("Результат:")
print(solve_Kramer(coefs,free))


# a = [
#     [1,-2,3],
#     [4,0,6],
#     [-7,8,9]
#     ]


# b = [
#     [9,8,7],
#     [6,5,4],
#     [3,2,1]
#     ]

# print("Матрица А")
# printMatrix(a)
# print("Матрица B")
# printMatrix(b)

# print("A-B:")
# printMatrix(subtractMatrix(a,b))
# print("Матрица А")
# printMatrix(a)
# print("Матрица B")
# printMatrix(b)
# print("A*B:")
# printMatrix(mulMatrixAndMatrix(a,b))

# print("Минор А по 1-й строке и 2-му столбцу")
# printMatrix(minor(a,1,2))

# print("Определитель А")
# print(determinant(a))