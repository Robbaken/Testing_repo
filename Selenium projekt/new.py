def fast_function():
    for i in range(10000000):
        i * i
    return fast_function
fast_function()