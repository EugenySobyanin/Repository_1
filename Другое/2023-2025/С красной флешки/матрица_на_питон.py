from random import randint

class Matrix():

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.matrix = [[None] * col] * row
        #[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        #[[None] * col] * row

    def generate_matrix(self):

        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] = randint(1, 10)

    def show_matrix(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j], ' ', end='')
            print()

small = Matrix(3, 5)
small.generate_matrix()

# print (small.matrix)
# small.show_matrix()

for el in small.__dict__.items():
    print(el)

#print(small.__dict__)
