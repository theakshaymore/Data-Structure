
# Kth Smallest and Largest Element in Array 
k = 3 
arr = [4,5,1,2,7,3,56,23]

arr.sort()
print("Smallest ", arr[k-1])

arr.sort(reverse=True)
print("Largest ", arr[k-1])
