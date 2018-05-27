#Insertion Sort o(n2)
# Sort a given array by using Insertion SOrt Algorithm


def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j-1
        while i >= 0 and key < array[i]:
            array[i+1] = array[i]
            i = i-1
        array[i +1 ] = key

arr = [12,10,2,100,23,1243,3,24,56,765,3,23,]
insertionSort(arr)
print (arr)
