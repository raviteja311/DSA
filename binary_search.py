def binary_search(arr,x):
    '''
    Function to perform the linear_search 
    parameter arr :List to search 
    parameter x   :key_element to search
    '''
    
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high + low) // 2 #mid is the middle value of the arr
        
        
        if arr[mid] == x:       #checking the mid with key_value
            return mid          #mid == key_value element found
        
        
        elif arr[mid] < x:      #if key_value is greater than mid
            low = mid + 1       #modify the low value into mid+1 and repeat the process
            
            
        elif arr[mid] > x:      #if key_value is lessthan mid
            high = mid - 1      #modify the high value into mid-1 and repeat the process
        else:                   #if elements not found else loop begins
            
            
            return -1           #element not found
    

# Example 
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result!= -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")