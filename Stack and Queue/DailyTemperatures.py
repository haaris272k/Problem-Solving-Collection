"""Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after
the ith day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]"""


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# idea is to find the dist bw curr and closest max ans[i]=idxofcurr-idxofmax
ans = [0] * len(temperatures)
stack = []
for idx, ele in enumerate(temperatures):
    # while stack is not empty and top of stack is less than curr
    while stack and ele > stack[-1][0]:
        # pop the top of stack and update ans[top]
        top, index = stack.pop()
        print(top, index)
        # print(temp, index)
        ans[index] = idx - index
        print(ans)
    # push curr and idx to stack
    print(ele, idx)
    stack.append((ele, idx))
print(ans)
