# a=10  #global scope
# def demo():
#     b=20
#     print("In local space",a)

# print(a)
# demo()
# print(b) it will throw error

def outer():
    def inner():
        c=30
        print(c)
    inner()

outer()


def outer():
    b=20
    def inner():
        nonlocal b 
        c=30
        b-=15
        print(b)

    inner()
outer()

