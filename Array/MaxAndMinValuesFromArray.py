
# Find Minimum and Maximun from given Array
arr = [5,2,56,32,4]

max = arr[0]
min = arr[0]

for i in range(1, len(arr)) :
    if (arr[i] > max) :
        max = arr[i]
    if (arr[i] < min) :
        min = arr[i]

print(min, max)