def quick_sort(arr):
    '''
    function to perform the bubble_sort 
    parameter arr :List to search 
    
    '''
    
    if len(arr) <= 1:                                        #checking if the len(arr) is lessthan or equal to 1
        return arr                                           #if True returns the sorted array
    
    
    else:                                                    #if multiple elements
        
        
        pivot = arr[0]                                       #first element as the pivot
        
        
        left = [x for x in arr[1:] if x < pivot]            #creating a new list from the array which are less than pivot 
        right = [x for x in arr[1:] if x >= pivot]          #creating a new list from the array which are greater than the pivot
        
        
        return quick_sort(left) + [pivot] + quick_sort(right)#combining the 'left' and 'right' with the pivot in between returns sorted array

# Example 
arr = [1, 7, 4, 1, 10, 9, -2]

#Dispalying the orginal array
print("orginal array    :",arr)

#calling the function
sorted_arr = quick_sort(arr)

#Dispalying the sorted array
print("Sorted Array     :",sorted_arr)

