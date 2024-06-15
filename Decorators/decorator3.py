import time


def cache(func):
    cache_value = {}

    # The print statement is not needed here for functionality, but can be used for debugging if required.
    # print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper  # No parentheses here


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(3, 2))  # This will take 4 seconds to run
print(long_running_function(3, 2))  # This will return immediately with the cached result
