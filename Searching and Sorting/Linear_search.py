"""

Write a program to implement Linear Search

Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6


"""

a = list(map(int, input().split()))
k = int(input("Enter the num "))
if k in a:
    print(a.index(k) + 1)
else:
    print("Not found")
