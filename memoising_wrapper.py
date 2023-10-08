from functools import wraps
def memoising(memory_cells):
    def wrapper(function):
        mem_dic = dict()
        order = []
        @wraps(function)
        def inner(arg):
            if arg not in mem_dic:
                order.append(arg)
                mem_dic[arg] = function(arg)
            if len(order) >= memory_cells:
                mem_dic.popitem()
                order.remove(order[0])
            return order
        return inner
    return wrapper

@memoising(3)
def func(x):
    """Multiply given arg (it should be number) by 10 and return result."""
    print('Calculating...')
    return x * 10

func(1)
func(2)
func(1)
func(2)
func(1)
help(func)