"""
Question 1 )Write a Python program to

(b) Input two arrays and output the common values between the two."""

def array_input():
    
    """ Takes in input of 2 1-D arrays and returns the arrays with respective array lengths"""
    array1_length = int(input('Input length 0f 1-D array 1- '))
    print('\nEnter elements for array 1 ')
    array1 = []
    
    
    for j in range(array1_length):
            array1.append(int(input()))
            
    array2_length = int(input('Input length 0f 1-D array 2- '))
    print('\nEnter elements for array 2 ')
    array2 = []
    
    
    for j in range(array2_length):
            array2.append(int(input()))       
            
   
    return array1, array1_length,array2, array2_length

array1, array1_length,array2, array2_length = array_input()
common_element= []
print(f'Array 1 =\n{array1}')
print(f'Array 2 =\n{array2}')
    
    #Running loop to find common elements between two arrays and adding same to a new array if that element is not already present
    
for array1_element in array1 :
        if (array1_element in array2) and (array1_element not in common_element) :            
            common_element.append(array1_element)
print(f'The common elements in array 1 and 2 are :\n{common_element}')