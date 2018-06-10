def mergeSort(array, low, high):
    if low < high:
        mid =  int( (low + (high -1))/2)
        print(mid)
        mergeSort(array, low, mid)
        mergeSort(array, mid +1, high)
        merge(array, low, mid, high)

def merge(array, low, mid, high):
    leftArrayIndex = int( mid - low + 1)
    rightArrayIndex = int (high - mid)
    #print ("left array index = %d" %leftArrayIndex )
    #print("right array Index = %d" %rightArrayIndex)
    leftArray =   [None] *  leftArrayIndex
    rightArray =  [None] *  rightArrayIndex

    for i in range(0,leftArrayIndex):
        leftArray = array[low + i]
    print ("Left Array =%d" %leftArray)
    for j in range (0,leftArrayIndex):
        rightArray = array[mid + 1 + j]
    print("Right Array %d" %rightArray)

    i =0
    j=0
    k=1
    while (i < leftArrayIndex and j< rightArrayIndex):

        if int (leftArray[i]) <= int ( rightArray[j]):
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1

    while i < leftArrayIndex:
        array[k] = leftArray[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < rightArrayIndex:
        array[k] = rightArray[j]
        j += 1
        k += 1



array = [38,1,23,45,6,2]

n = len(array)
print( "length of array = %d" %n)
print ("Given array is")
for i in range(n):
    print ("%d" %array[i]),
mergeSort(array,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i])
