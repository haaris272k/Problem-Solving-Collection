# Google Tech Interview Question


"""You are given a function :-

f(n) = 3*n + 1, when n is odd,
f(n) = n/2, when n is even.

Find the minimum number of steps to reach 1.

7 -> 22 -> 11 -> 34 -> 17 ->52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -.> 2 -> 1

Minimum Steps = 16"""

# Simple mathematical simulation based approach
def min_steps(n):
    count = 0
    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n = n / 2
        count += 1
    return count


n = 22
print(min_steps(n))

# Follow up question:

"""You are given a range of numbers from 1 to N, 
find the number which will give maximum minimum number of steps using the above function.

Suppose N = 4

1 = 0 steps
2 -> 1 = 1 steps
3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 = 7 steps
4 -> 2 -> 1 = 2 steps"""

arr = [1, 2, 3, 4]  # Input
# making use of the above function
# storing the steps in a dictionary
# key = number, value = steps
# Finally, finding the max value in the dictionary and key associated with that value

NumStepmap = {}

for i in arr:
    num, step = i, min_steps(i)
    NumStepmap[num] = step

print(NumStepmap)

for k, v in NumStepmap.items():
    if v == max(NumStepmap.values()):
        print((k, v))
