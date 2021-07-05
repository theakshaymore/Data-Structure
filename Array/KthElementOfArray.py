
# Kth Smallest and Largest Element in Array 


# using complex logic
class Solution:
    def KthElement(self, arr,l,r,k):
        locs = 0
        max = 10000
        for i in range(k):
            max = 10000
            for j in range(r+1):
                if(arr[j] < max):
                    max = arr[j]
                    locs = j
            arr[locs] = 10000
        return max

obj = Solution()
l = 0
r = 4
k = 3
arr = [5,2,1,6,9]

obj.KthElement(arr, 0, 4, 3)




# using simple logic
# k = 3 
# arr = [4,5,1,2,7,3,56,23]

# arr.sort()
# print("Smallest ", arr[k-1])

# arr.sort(reverse=True)
# print("Largest ", arr[k-1])
