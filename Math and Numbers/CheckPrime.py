import math

# TC: O(sqrt(n))
# SC: O(1)
def checkprime(n):
    if n == 0 or n == 1:
        return False
    a = int(math.sqrt(n))
    print(a)
    for i in range(2, a + 1):
        if n % i == 0:
            return "Not a Prime"
            # return False
    return "Prime"
    # return True


n = 11
print(checkprime(n))
