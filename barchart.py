import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, 
                      **kwargs)
        end_time = time.time()
        print(f"Result time of {func.__name__} call:"
              f"{end_time - start_time} sec.")
        return result
    return wrapper

@timer
def some_func():
    time.sleep(2)

some_func()