def linear_search(arr,x):
    '''
    Function to perform the linear_search 
    parameter arr :List to search 
    parameter x   :key_element to search
    '''
    
    # interation through the list
    for i in range(len(arr)):
        
        #checks the current element equal to the key_element
        if arr[i] == x:
            
            #Returns the index if kye_element is found
            return i
        
    #returns none if the elements if not foud
    return None


#Example

arr = [10,20,30,40,50,60,70,80,90,100]
x = 70
result = linear_search(arr,x)

if result != None:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in th e list")