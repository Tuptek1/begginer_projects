arr = [ 2, 3, 4, 10, 40 ]

def binary_search(numbers, guess):
    left = 0
    right = len(numbers) - 1
    counter = 0
    while left <= right:
        counter += 1
        
        middle_index  = int((left + right) / 2)     
         
        if numbers[middle_index] == guess:
            print("Found") 
            print("After "+str(counter)+" moves")
            return 1
        
        elif  numbers[middle_index] > guess:
            right = middle_index - 1
        
        else:
            left = middle_index + 1
    return -1

binary_search(arr, 10)
