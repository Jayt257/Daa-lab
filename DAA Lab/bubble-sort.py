# Python program for implementation of Bubble Sort
def bubbleSort(elements):
    n = len(elements)
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        # traverse the array from 0 to n-i-1 Swap if the element found is greater than the next element
        for j in range(n-i-1):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]

# Driver code to test above
elements=[39,12,18,85,72,10,2,18]
print("\nUnsorted list is")
print(elements)
bubbleSort(elements)
print("\nSorted list is")
print(elements)
