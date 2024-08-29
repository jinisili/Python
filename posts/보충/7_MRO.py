#%%

class A:
    def __init__(self):
        print('A Constructor')

class X:
    def __init__(self):
        print('X Constructor')
   

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')
    
class C(X):
    def __init__(self):
        super().__init__()
        print('C Constructor')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')

print(D.mro())
d = D()

#%%

class A:
    def __init__(self):
        self.common = 'A'
        print('A Constructor')

class X:
    def __init__(self):
        self.common = 'X'
        print('X Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')
    
class C(X):
    def __init__(self):
        super().__init__()
        print('C Constructor')

class D(B, C):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        print('D Constructor')

print(D.mro())
d = D()
print(d.common)
