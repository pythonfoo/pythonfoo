

class A():
    def __init__(self, a):
        self.a = a
        print("AAAAAAAA: {}".format(a))
        
class B(A):
    def __init__(self, a, b=0):
        super(B, self).__init__(a)
        self.b = b
        print("BBBBBB: {}".format(b))
        
    def __init__(self, a, b, c):
        print("ABC")
    
    
A(10)
B(20, 0, 0)
