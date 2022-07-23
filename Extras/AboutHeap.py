import heapq

# input list
nums = [1000, 2000, 30, 20, 10]

# converting list to heap
# Note : by default the heap is min heap (Sorted in ascending order)


heapq.heapify(nums)
print("Converted to heap", nums)

# pushing new element to heap
# will be pushed to the start of the heap (on right side)


heapq.heappush(nums, 40)
print("Pushed new element to heap", nums)


# popping the element from heap
# it will be always the minimum element
# will be popped from the end of the heap (on left side)


pooped_ele = heapq.heappop(nums)
print("Popped element is", pooped_ele)
print("Popped element from heap", nums)

# to find kth smallest element in the heap


let_k = 3
kth_smallest_ele = heapq.nsmallest(let_k, nums)
print("Kth smallest element is", kth_smallest_ele)

# to find kth largest element in the heap

kth_largest_ele = heapq.nlargest(let_k, nums)
print("Kth largest element is", kth_largest_ele)
