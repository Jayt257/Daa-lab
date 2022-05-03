# binary search function have object arr,low,high,x
def binary_search(arr,low,high,x):
    # make sure that high always greater than low for this algo
    if high>=low:
        # find mid point of array
        mid = (high+low)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else :
            return binary_search(arr,mid+1,high,x)
    else:
        return -1
    
arr=[3,5,7,10,34,54,32,45]
x = 10
result = binary_search(arr,0,len(arr)-1,x)
if result != -1:
    print("Element present in array at index ",str(result))
else:
    print("Element not present in array")
