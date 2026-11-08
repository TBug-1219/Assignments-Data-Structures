#Victoria Buckner
#Week 14 Assignment

array = [6, 4, 12, 9, 45, 23, 2, 43, 56, 17, 20, 11, 7]

print("Array before swap: ", array)

smallIndex = 0
largeIndex = 0

for i in range(1, len(array)):
    if array[i] < array[smallIndex]:
        smallIndex = i
    if array[i] > array[largeIndex]:
        largeIndex = i

array[0], array[smallIndex] = array[smallIndex], array[0]

if largeIndex == 0:
    largeIndex = smallIndex

array[-1], array[largeIndex] = array[largeIndex], array[-1]

print("Array after swap: ", array)