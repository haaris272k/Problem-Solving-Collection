# This method could be used to find the runtime of your solution (for Python code).
# You can use it to check the efficiency of your solutions.

import time

def measure_runtime(func, *args, **kwargs):
    """
    Measure the runtime of a function with the given arguments.

    Args:
        func (callable): The function to be measured.
        args: Positional arguments to be passed to the function.
        kwargs: Keyword arguments to be passed to the function.

    Returns:
        The return value of the function.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Runtime: {runtime:.6f} seconds")
    return result
