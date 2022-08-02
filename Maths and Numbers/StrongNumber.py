"""Strong Numbers are the numbers whose sum of factorial of digits 
is equal to the original number. Given a number N, the task is to check
if it is a Strong Number or not. Print 1 if the Number is Strong, else Print 0.

 

Example 1:

Input:
N = 145
Output:
1
Explanation:
1! + 4! + 5! = 145 So, 145 is a Strong
Number and therefore the Output 1."""


def facto(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial


number = 145
todis = list(map(int, str(number)))
s = 0
for i in range(len(todis)):
    s = s + facto(todis[i])

if s == number:
    print(1)
else:
    print(0)
