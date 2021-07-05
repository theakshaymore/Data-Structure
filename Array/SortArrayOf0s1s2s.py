arr = [2,0,1,1,0]
n = len(arr)
count0 = 0
count1 = 0
count2 = 0

for i in arr:
    if(arr[i] == 0):
        count0 =  count0 + 1
    if(arr[i] == 1):
        count1 =  count1 + 1
    if(arr[i] == 2):
        count2 =  count2 + 1
k = 0
for i in range(0,count0):
    arr[i] = 0
for i in range(count0 , (count0 + count1)):
    arr[i] = 1
for i in range((count0 + count1), n):
    arr[i] = 2
print(arr)



