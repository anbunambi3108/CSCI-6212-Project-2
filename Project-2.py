#libraries:
import random
import time

# CODE FOR GENERATING CIRCULAR SHIFTERD ARRAY:
def generate_circular_shifted_array(size):
    # Generates a sorted array of random numbers
    original_array = [random.randint(1, 10000) for _ in range(size)]
    original_array.sort()
    # Chooses a random shift position
    shift_position = random.randint(0, size - 1)
    # Performs circular shift to create the shifted array
    shifted_array = original_array[shift_position:] + original_array[:shift_position]
    return shifted_array

# Size of the circular shifted array susch as 10,100,1000,10000,100000
array_size = 10
# Generates a circular shifted array
shiftedArray = generate_circular_shifted_array(array_size)

# Prints the circular shifted array
print("Circular Shifted Sorted Array:")
print(shiftedArray)

# CODE FOR FINDING MAXIMUM NUMBER IN CIRCULAR SHIFTED ARRAY:
start=time.time_ns()#computes the start time
def findMaxNumber(array,low,high):
    #case:1 If there is only one element in the array
    if(high==low): 
        return array[low]
    middle=(low+high)//2 
    #case:2 If the middle element is greater than previous element and next element
    if(array[middle]>array[middle-1] and array[middle] > array[middle+1]): 
        return array[middle]
    #case:3 If middle element is in 0th position and it is greater then the next element
    if(middle==0):
        if(array[middle]>array[middle+1]): 
            return array[middle]
    # deciding the direction     
    if(array[middle]<array[low]): #if the middle element less than low element
        return findMaxNumber(shiftedArray,low,middle-1) #goes to left half of the array
    else:
         return findMaxNumber(shiftedArray,middle+1,high) #goes to the right half of the array
        
#Prints the maximum number and total time taken:
print("Maximum Number in Circular Shifted Array: ",findMaxNumber(shiftedArray,0,len(shiftedArray)-1))
end=time.time_ns()#computes the end time
TimeTaken=end-start#computes the total time
print("Total time taken :",TimeTaken,"ns")