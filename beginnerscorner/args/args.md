# Python basics: Functions and arguments
> by shezi (Johannes Spielmann, jps@shezi.de)  
> A version of this also appeared on [shezi.de](http://shezi.de/index.php/2014/07/python-basics-function-syntax/)



I've recently talked to some guys and girls about functions in Python and how to define and call them. Here's the distillation of everything that's interesting about the topic. [Footnote: By the way, I won't put comments in all of my functions, because they are so very short and just for illustration. You should __*always*__ put documentation in _your_ functions, though!]

The first thing we do is define a function without any parameters. There syntax for this is:

    def fun():
        print("this is fun")
        
This defines a function `fun` that can be called and that prints out the string given in its _function body_. What's the "function body", you ask? It's all the indented lines following `def fun():` (which, coincidentally, is called _function head_), and it's those lines that are executed when you call the function. Let's try it out:

    >>> fun()
    this is fun
    
As you can see, you call functions by giving them a list of arguments in parentheses -- and in our case, that list is empty. If you omit the argument list (sometimes also called parameter list), something entirely different happens:

    >>> fun
    <function fun at 0x10796b440>
    
What does *that* mean? It means that instead of _calling_ the function, you _pointed_ at the function. Functions in Python behave like any other value, so you could assign them to a variable or pass them as a parameter to another function. But more about that later.

Our function doesn't _return_ anything, so calling it doesn't produce a value. Well, actually, "no value" in Python means `None`, and we can see that, too:

    >>> val = fun()
    this is fun
    >>> print(repr(val))
    None

One of the most important use cases of functions, however, is to compute something, which means we have to be able to indicate what the value of a function call should be. That's what the keyword `return` does. It works like this:

    def fun():
        print("this is still fun")
        return "enjoyment"

And we get the value back when we call the function:

    >>> val = fun()
    >>> print(repr(val))
    'enjoyment'


So let's say, we want to define a function that adds two variables. To do that, we need to tell Python that our function should accept two parameters:

    def add(a, b):
        return a + b
        
We already know what `return` means, but now the _argument list_ isn't empty any more. Instead, it has two entries, `a` and `b`, and that means you also have to call this function with two arguments:

    >>> add(2, 2)
    4

You can _not_ call the function with any other number of parameters, or you'll get an error:

    >>> add(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: add() missing 1 required positional argument: 'b'
    >>>
    >>> add(2, 3, 4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: add() takes 2 positional arguments but 3 were given
    
The arguments we defined here are so-called `positional` arguments. They are called this because their position, or order, is important. Calling a function with a different order of arguments changes the meaning, like this:

    def sub(a, b):
       return a - b
       
    >>> sub(3, 2)
    1
    >>> sub(2, 3)
    -1

Positional arguments, because they are identified by their position.

But what if we want to allow someone to only specify one argument, assuming that people always mean 0 when they don't say anything? In that case, we can turn one of our positional arguments into keyword arguments, or default arguments [Footnote: These two words actually have distinct, specific meanings in Python 3. However, this difference is not very important in most use cases, so I'll use them interchangeably.]. This means that we specify a value that should be used when the argument is absent in the call:

    def add(a, b=0):
       return a - b
       
I can now leave the value for `b` out of the call and Python will substitute a zero for it:

    >>> add(1)
    1
    >>> add(1, 2)
    3
    
This argument is now a _default_ argument, because it can be defined either by its position or by its default value. It can _also_ be identified by is name, and that's why it's not a positional argument any more (as you saw above, it's still positional, too, though). Have a look at this:

    def sub(a=0, b=0):
        return a - b

Both `a` and `b` are now default arguments that I can omit, or I can identify them by their name -- and then the order isn't important any more. Here's how you can call this new `sub` function:

    >>> sub(3, 2)
    1
    >>> sub(3)
    3
    >>> sub()
    0
    >>> sub(a=4)
    4
    >>> sub(b=2)
    -2
    >>> sub(a=4, b=2)
    2
    >>> sub(b=4, a=2)
    -2
    
As you saw here, we can call this function like we did before, with positional arguments. We can also skip any of the arguments and get a value of 0 for those. We can also identify the arguments by their name, regardless of the order. That's also why they're called keyword arguments -- instead of their position I can call them by their keyword, their name.

For most parts, this can get you very far. You can now create functions with as few or as many arguments as you need, and you can make some or all of these arguments with default values, so we can skip them or call them by their name.


## The hitch with keyword arguments

Of course, not all is easy in the land of computers, so there's a hitch that we have to look out for when using keyword arguments. These arguments are only initialized when the function is defined, so they become what other languages would call _static_, they don't change from call to call.

Well, what do I mean by that now?! It means that when you give a keyword argument a default value that can change, like a list, a dictionary or an object, you'll be surprised. Let's have a look:

    def wrong_insert(a, ls=[]):
        """Insert a into the given list."""
        ls.append(a)
        return ls
        
Now when you use `insert`, at first nothing surprising happens:

    >>> wrong_insert(2, [])
    [2]
    >>> wrong_insert(3, [1, 2])
    [1, 2, 3]
    >>> wrong_insert(1)     # we can omit the keyword argument here!
    [1]
    
However, now something completely strange appears:

    >>> wrong_insert(1)     # again!
    [1, 1]

Wait, what now?! Why is `1` twice in that list? Because you inserted twice into the same list. That default value is only created once when you define the function, so when you append something to the list, you append it _to the default value of that parameter_. So how do we do it right? We assign a default value that cannot be changed and test for it. There's one value that's perfectly suited for that task, and it's `None`:

    def right_insert(a, ls=None):
        if ls is None:
            ls = []
        ls.append(a)
        return ls
        
This one works as expected:

    >>> right_insert(2, [])
    [2]
    >>> right_insert(3, [1, 2])
    [1, 2, 3]
    >>> right_insert(1)
    [1]
    >>> right_insert(1)
    [1]

Be very, very careful when you see a list, a dictionary or an object as a default value. Changing that value will happen and you probably won't expect it.

There's more or less only one use case for putting a mutable value (like a dictionary) into a default value, and that's when you use it as a cache. You should certainly call it `CACHE` in that case, too! Here's an example:

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

That's a neatly encapsulated cache. Since we named it in ALL-CAPS, we know that it's sort-of global, so we'll be on the lookout when finding such a variable.

If you see any other list, dictionary or object as a default parameter value, be suspicious!


## varargs, lots of positional arguments

But what if you don't know the number of positional arguments beforehand? Say, you want to add two _or more_ numbers?
There's a way to do that and it's called `varargs`, from "variable number of arguments". The syntax for that in Python is:

    def adder(*args):
        result = 0
        for argument in args:
            result = result + argument
        return result
        
And let's try it out:

    >>> adder(1)
    1
    >>> adder()
    0
    >>> adder(1, 1, 2, 3, 5, 8, 13, 21)
    54
    
So what happens here is that any argument that is not positional gets stuffed into a list, and this list is called `args`, because we gave it that name with an asterisk in front of it in the function definition. Any other name works as well, but it's a pretty strong convention to use `args` here.
And as you see, we can have any number of arguments, even none at all. Of course we can still specify that we want positional arguments in front of it:

    def subber(start, *args):
        result = start
        for argument in args:
            result = result - argument
        return result
        
You can _not_ omit the first argument. It's a positional argument, so you cannot omit it. But we can omit the varargs:

    >>> subber(5, 2)
    3
    >>> subber(10, 1, 2, 3, 4)
    0
    >>> subber(10)
    10
    >>> subber()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: subber() missing 1 required positional argument: 'start'
    
Can you have more than one varargs?

    def subber(*args, *moreargs):
      File "<stdin>", line 1
        def subber(*args, *moreargs):
                          ^
    SyntaxError: invalid syntax
    
No, you can't. And what would be the meaning of that anyway? Which list should Python add the arguments to? No, no, that doesn't mean anything, so you it's a syntax error, as it should be.

Did you notice what simple trick Python does here for us? It takes the arguments that you pass into a function that don't go anywhere else, stuffs them into a list and gives us that list. It's really all that happens.

But interestingly enough, the trick works in reverse, too: When you have a list of values that you want to use as arguments to a function, you can tell python to do just that, and with the _same_ syntax, too:

    >>> arglist = [10, 5, 4]
    >>> subber(*arglist)
    1
    >>> subber(10, *arglist)
    -9
    >>> subber(100, 1, 2, 3, 4, *arglist)
    71

Don't forget that asterisk, though:

    >>> subber(10, arglist)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in subber
    TypeError: unsupported operand type(s) for +: 'int' and 'list'



## kwargs, lots of keyword arguments and lots of other arguments

So let's say you want to define a function that has a keyword argument, but you don't know what keyword that'll be, and you also don't know how many it should be. Sounds unlikely, but it's actually very useful when you do dynamic processing or datastructures you don't know much about.

Of course, there's a syntax for it as well, and it's pretty similar to the varargs we saw before. It's called kwargs, for keyword arguments, uses two asterisks and instead of a list of arguments you get a dictionary:

    def dynamic(**kwargs):
        print(kwargs)
        
And it works as expected:

    >>> dynamic(hello='world', goodbye='lonelyness')
    {'goodbye': 'lonelyness', 'hello': 'world'}

Just as we saw before, the same works in reverse: When I have a dictionary with values that I want to use to call a function, I can just tell Python to unpack them into arguments:

    def do_stuff(key=0, lock=1, **kwargs):
        print("doing stuff with key {} and lock {}".format(key, lock))
        print("and more arguments: {}".format(kwargs))

    >>> params = {'key': 10, 'lock': 'Locke', 'something': 'else'}
    >>> do_stuff(**params)
    doing stuff with key 10 and lock Locke
    and more arguments: {'something': 'else'}


So now we have all parts together and we can actually stick them together, so here's the full syntax for function definitions [at least in Python 2.7]:

def fun(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

Try it out for yourself!

Actually, there's one more thing: You _could_ add in keyword arguments in the middle, between `b` and `*args`, but it wouldn't work the way you expected it to, and *that* would be confusing and unintuitive. So don't do that!



## Functions are values!

So why is the `args` and `kwargs` dance so useful? Especially `kwargs` -- what good could it be when you don't know the parameters to your function?

To make this work for us, we have to know one more great thing about functions: they are values, just like everything else is. So you can rename functions, store them in variables, put them in lists and even pass them to other functions. Using `fun` from above, let's see:

    >>> fun(0, 0)
    (0, 0, [], {})
    >>> morefun = fun
    >>> morefun(0, 0)
    (0, 0, [], {})
    >>> funlist = [fun, morefun]
    >>> funlist[0](0, 0)
    (0, 0, [], {})
    >>> def funfun(f):
            print("calling f")
            f(0, 0)
    >>> funfun(fun)
    calling f
    (0, 0, [], {})

That last bit is really interesting: we can pass functions into functions. We can also return functions from functions -- because they're simply values that behave like any other.

And finally, we can also _define_ functions inside of functions. In a way, when you write `def f(...):...`, this is just shorthand for `f = <some function>`, and it will behave exactly like any other variable. Think of functions as any other variable, just one that you can call to get a new value.

So now let's put all this together. See if you can figure out what this next example does:

    def log_fun(f):
        def inside(*args, **kwargs):
            print("called with {} and {}".format(args, kwargs))
            result = f(*args, **kwargs)
            print("resulted in {}".format(result))
            return result
        return inside
        
Wow! We defined a function that takes a function, creates a function, uses a function inside the inner function, and then returns that inner function. So, what does it do? `log_fun` _wraps_ the function we passed as parameter `f`, and returns a function that does the wrapping. The wrapping function then prints the arguments and kwarguments, calls `f` with them, prints the result of the call and finally returns the result of the call. All without knowing anythig about the parameters of `f` itself. From a parameter/return perspective, it behaves quite like `f` does -- only it prints out the parameters and results in between. How do we use it? Let's try:

    >>> new_f = log_fun(fun)
    >>> new_f(0, 0)
    called with (0, 0) and {}
    0 0 () {}
    resulted in None

You could be even more daring and _replace_ `fun` with that new logged version of fun:

    >>> fun = log_fun(fun)
    >>> fun(0, 0)
    called with (0, 0) and {}
    0 0 () {}
    resulted in None

Pretty neat, eh? You simply wrapped your function in some logging, without caring what the actual parameters are. That `log_fun` function is pretty useful when you want to debug your function calls without changing the functions themselves.

Since wrapping, enhancing or _decorating_ functions is such a useful concept, there's a special syntax for it in python, with an `@`. These next two examples are exactly the same:

    def something(x):
        print("X!", x)
    something = log_fun(something)
    
and this one:

    @log_fun
    def something(x):
        print("X!", x)

And now you know what a _Decorator_ is in python: It's a function `d`that takes a function `f` and returns a function `f'`, and in-between does something with the original function `f` -- effectively enhancing the things `f` does. Don't be alarmed by the syntax, the two blocks above are exactly identical, semantically, so if you ever see one of the two, you can replace it with the other without fear.

There's more to say about decorators, but there's another document for that.


## Overloading

If you ever programmed in a compiled language like C, C++ or Java, you might have heard the term "overloading a function". It's a cool concept, and it basically means that two functions or methods can have the same name but a different parameter list. Like this (in Java):

    class OverloadingDemo
    {
        void simpleFunc()
        {
            System.out.println('simpleFunc v1 called')
        }

        int simpleFunc(int param)
        {
            System.out.println('simpleFunc v2 called')
            return param * 2;
        }

        public static void main(String[] args)
        {
            simpleFunc();
            simpleFunc(2);
        }
    }

If you compiled that program and ran it, the output would be:

    simpleFunc v1 called
    simpleFunc v2 called

The reason this works is because when you compile this program, the compiler can match the different calls to the different function definitions. So effectively, there are two functions in this Java class, one without parameters and one with parameters.

Python works differently. When you define a function, as you remember, you simply give a value to a variable. So if you do this in Python:

    def fun():
        print("fun v1 called")
        
    def fun(a):
        print("fun v2 called")
        
Now there is _still_ only one version of `fun`, and it's the last one that you defined. The second definition of `fun` didn't overload the function, it replaced it.

If you want your function to work the same way as the ones in the example above, you'll have to do it yourself:

    def fun(a=None):
        if a is None:
            print("fun v1 called")
        else:
            print("fun v2 called")
            
So, the gist is that Python does not have built-in overloading. Instead, you can assign a `None` value for the parameter you want to overload and check for its existence yourself.



## Conclusion

Well, there's a surprising amount of stuff in Python functions. The most important things you have to remember are:

  * If you want a variable number of positional arguments, use `args`. If you want to variable number of named arguments, use `kwargs`.
  * Function definitions have a lot of syntax, but they're nothing "magic". They just simply create a function object and assign that value to a name, the function name.
  * You can not overload a function in the Java-sense, but you can overload them in other ways, with named arguments, args, kwargs and your own separation logic.
  * **Do not use a mutable value as a default parameter value.**
  
And finally, don't worry too much about it! =)
