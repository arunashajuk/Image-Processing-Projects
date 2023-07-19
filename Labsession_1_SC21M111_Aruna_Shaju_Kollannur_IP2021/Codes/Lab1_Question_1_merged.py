"""
Question 1 )Write a Python program to

(a) Find the largest and smallest element in a matrix and print the values along with
their position.
(b) Input two arrays and output the common values between the two.
(c) Do element wise addition, subtraction, multiplication and division with and without
built-in functions.

"""

import numpy as np

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

def array_input():
    
    """ Takes in input of 2 1-D arrays and returns the arrays with respective array lengths"""
    array1_length = int(input('Input length 0f 1-D array 1 '))
    print('\nEnter elements for array 1 ')
    array1 = []
    
    
    for j in range(array1_length):
            array1.append(int(input()))
            
    array2_length = int(input('Input length 0f 1-D array 2 '))
    print('\nEnter elements for array 2 ')
    array2 = []
    
    
    for j in range(array2_length):
            array2.append(int(input()))       
            
   
    return array1, array1_length,array2, array2_length


def largest_smallest():
    
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
        
            
def common():
    
    array1, array1_length,array2, array2_length = array_input()
    common_element= []
    print(f'Array 1 =\n{array1}')
    print(f'Array 2 =\n{array2}')
    
    #Running loop to find common elements between two arrays and adding same to a new array if that element is not already present
    
    for array1_element in array1 :
        if (array1_element in array2) and (array1_element not in common_element) :            
            common_element.append(array1_element)
    print(f'The common elements in array 1 and 2 are :\n{common_element}')
    
def array_operations():
    array1, array1_length,array2, array2_length = array_input()
    
    Add = []
    Sub = []
    Mul = []
    Div = []
    
    if ( array1_length > array2_length):
        array1, array2 = array2, array1 
        array1_length, array2_length = array2_length, array1_length
    
    # Appending the smaller array with trailing zeros for easier computation
    
    for i in range(array2_length - array1_length):
        array1.append(0)
    
    print(f'Array 1 =\n{array1}')
    print(f'Array 2 =\n{array2}')
    
    # Running the loop to perform element-wise operations
    for i in range(array2_length):
              
        Add.append(array1[i] + array2[i])
        Sub.append(array1[i] - array2[i])
        Mul.append(array1[i] * array2[i])
        Div.append(array1[i] / array2[i])
        

    print('The element-wise operations on array 1 and array 2 without inbuit function are :')
    print(f'Addition-\n{Add}')
    print(f'Subtraction-\n{Sub}')
    print(f'Division-\n{Div}')
    print(f'Multiplication-\n{Mul}')

    array1_np = np.array(array1)
    array2_np = np.array(array2)
    
    print('The element-wise operations on array 1 and array 2 without inbuit function are :')
    print(f'Addition-\n{np.add(array1_np , array2_np)}')
    print(f'Subtraction-\n{np.subtract(array1_np , array2_np)}')
    print(f'Division-\n{np.divide(array1_np , array2_np)}')
    print(f'Multiplication-\n{np.multiply(array1_np , array2_np)}')
    
    print(np.subtract(array1_np , array2_np))

selection = input("-Enter 'a' to find the largest and smallest element in a matrix \n-Enter 'b' to output common values between two arrays\n-Enter 'c' for element-wise addition, subtraction, division and multiplication of two matrices\n")
                   
if (selection == 'a'):
    largest_smallest()
    
elif (selection == 'b'):
    common()
    
elif (selection == 'c'):
    array_operations()
    
else:
    print('Invalid Selection')
    
