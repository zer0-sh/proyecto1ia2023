def read_matrix_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        matrix = [[cell for cell in line.strip().split()] for line in lines]
        return matrix

# Imprimir matriz
def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=" ")
        print()

matrix = read_matrix_from_file("matriz.txt")
print_matrix(matrix)