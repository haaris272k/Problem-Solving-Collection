def nth_fibonacci(n):
    if n <= 1:
        return n
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def nth_fibonacci(n):
    fib_series = [0, 1]

    for i in range(2, n + 1):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])

    return fib_series[n]


n = 9
print(nth_fibonacci(n))
