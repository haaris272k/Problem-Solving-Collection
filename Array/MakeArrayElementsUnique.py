'''Given an array arr[ ] of N elements, your task is to find the minimum number of increment operations required to make all the elements of the array unique. ie- no value in the array should occur more than once. In an operation a value can be incremented by 1 only.'''

arr = [1, 1, 2, 3]
arr=[1,2,2]

arr.sort()
n=len(arr)

summ=sum(arr)
c_=0

for i in range(n):
    if i!=0 and arr[i]<=arr[i-1]:
        c_+=1
        arr[i]=arr[i-1]+1 
print(arr)
print(c_)
print(abs(summ-sum(arr)))