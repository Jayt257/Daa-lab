def bubbleSort(elements):
    n = len(elements)
    for i in range(n-1):
        for j in range(n-i-1):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]

elements=[39,12,18,85,72,10,2,18]
print("\nUnsorted list is")
print(elements)
bubbleSort(elements)
print("\nSorted list is")
print(elements)