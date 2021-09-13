# *********************** Multiplication of Two Matrices *******************************

# This is the practice on how to multiply two matrices by using python
""" This programme will give us the multiplication of any length of matrix if possible..! """

# This will take input of matrix from the user
def Take_Matrix(row, column):
    matrix = []
    for i in range(row):
        print(f"This is row {i + 1}...!")
        raw_row = []
        for j in range(column):
            number = int(input(f"Enter the number {j + 1}: "))
            raw_row.append(number)
        matrix.append(raw_row)
    for m in matrix:
        print(m)
    return matrix

# This will multiply the matrix from the user
def Multiply_Matrix(A, B):
    Matrix = []
    for i in range(len(A)):
        Row = []
        for j in range(len(B[0])):
            number = 0
            for k in range(len(B)):
                number = number + A[i][k]*B[k][j]
            Row.append(number)
        Matrix.append(Row)
    for M in Matrix:
        print(M)


if __name__ == '__main__':
    choice = 0
    while True:
        try:
            row = int(input("\nEnter the number of rows you want in your matrix: "))
            column = int(input("Enter the number of columns you want in your matrix: "))
        except Exception as E:
            print("Only integers are allowed...!")
        else:
            try:
                if choice % 2 == 0:
                    A_column = column
                    print("\nMatrix A: \n")
                    print(f"\nThis is the A matrix:\n")
                    A = Take_Matrix(row, column)
                    choice += 1
                    continue
                else:
                    B_row = row
                    print("\nMatrix B: \n")
                    print(f"\nThis is the B matrix:\n")
                    B = Take_Matrix(row, column)
                    choice += 1
            except Exception as E:
                print("Invalid Input...!")
            else:
                try:
                    if (A_column != B_row):
                        print("\nNumber of column of A matrix must be equal to row of B matrix")
                        continue
                    else:
                        print('\nMultiplying Two Matrices...')
                        print(f"Multiplication of two matrices:")
                        Multiply = {Multiply_Matrix(A, B)}
                except Exception as E:
                    print("\nMultiplication does not occur...! Something Went Wrong...!")
                else:
                    print("\nMultiplication is done...!\n")
                finally:
                    print("\n ** Thanks for your valuable time ** \n")
        continue


