

def fun(a, *args):
    
    print("hello world", a, args)
    
def fun2(a,b,c,d,e):
    print(a,b,c,d,e)

def fun3(a=0, b=0):
    print(a,b)
    
def fun4(a, b=0, *args, **kwargs):
    print(a, b, args, kwargs)

def function(positional, kw=0, *args, **kwargs):
    print(positional, kw, args, kwargs)

fun4(1, 2,3,4, c=6, d=8)

arguments = [1,2,3]
fun4(arguments)
    
someargs = {'a': 10, 'b': 100}
fun3(**someargs)
    
print("ignore the rest")
    
fun(1, 2)
fun(1)
fun(1,2,3)

arguments = [2,3,34,5,5]
fun(1, *arguments)
fun2(*arguments)

fun3(1,2)
fun3(a=2, b=3)
fun3(b=3, a=2)

fun(1, b=2)