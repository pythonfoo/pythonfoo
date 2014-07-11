
def wrong_fun(item, ls=[]):
    ls.append(item)
    return ls

def right_fun(item, ls=None):
    if ls is None:
        ls = []
    ls.append(item)
    return ls

def fib(n, CACHE={}):
    if n in CACHE:
        return CACHE[n]
    else:
        if n < 1:
            return 1
        else:
            val = fib(n-1) + fib(n-2)
            CACHE[n] = val
            return val

print( wrong_fun(1, []) )  # --> [1]
print( wrong_fun(1, [0,0,0,0])  )

print( wrong_fun(9) )     # --> [1]
print( wrong_fun(1) )     # --> [1]

print(right_fun(9))
print(right_fun(1))