"""
Question 1 )Write a Python program to

(a) Find the largest and smallest element in a matrix and print the values along with
their position."""

def Matrix_input():
    """ Takes in a 2-D Matrix from user and returns array with row and colum specification"""
    
    Matrix_rows = int(input('Input the row size of Matrix '))
    Matrix_colums = int(input('Input the column size of Matrix '))
    print('\nEnter the elements row-wise ')
    Matrix = []
    
    for i in range(Matrix_rows):
        row_temp = []        
        for j in range(Matrix_colums):
            row_temp.append(int(input()))
        Matrix.append(row_temp)
    print(f'Matrix =\n{Matrix}')
    return Matrix , Matrix_rows, Matrix_colums

Matrix, Matrix_rows, Matrix_colums = Matrix_input()    
max = min = Matrix[0][0]        
max_row = max_column = min_row= min_column = 0
    
# loop to mark the smallest and largest number in the matrix along with its row and column position
    
for i in range(Matrix_rows):
        for j in range(Matrix_colums):
            if(Matrix[i][j] > max):
                max = Matrix[i][j]
                max_row = i + 1
                max_column = j + 1
                                    
            if(Matrix[i][j] < min):
                min = Matrix[i][j]
                min_row = i + 1
                min_column = j + 1
                
print(f'The largest element is {max} at row {max_row} and column {max_column}')
print(f'The smallest element is {min} at row {min_row} and column {min_column}')