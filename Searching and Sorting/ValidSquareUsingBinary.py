"""Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt."""

num = 614
low = 0
high = num
while low <= high:
    mid = low + (high - low) // 2
    if mid * mid == num:
        print(mid, mid * mid, num, True)
        break
    elif mid * mid < num:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(False)
