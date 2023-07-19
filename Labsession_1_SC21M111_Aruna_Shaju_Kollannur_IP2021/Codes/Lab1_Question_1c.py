"""
Question 1 )Write a Python program to

(c) Do element wise addition, subtraction, multiplication and division with and without
built-in functions.

"""
import numpy as np 

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
   