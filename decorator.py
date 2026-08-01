# def instagram(func):
#     def wrapper(*args,**kwargs):
#         print("Go to www.instagram.com")
#         print("Log in")
#         func(*args, **kwargs)
#         print("Log Out")

#     return wrapper

# @instagram
# def akash_insta():
#     print("Chatting with gf")

# akash_insta()


# def validate_positive(func):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if i<0:
#                 print("Please enter positive number")
#                 return
#         func(*args, **kwargs)
#     return wrapper


# @validate_positive
# def add(a,b,c):
#     print(a+b+c)

# add(10,20,-30)            


def login():
    status=eval(input("Do you want to login?(True/False): "))
    return status

is_logged_in=login()

print(is_logged_in)

def check_log(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            func(*args, **kwargs)
        else:
            print("Please login first")
    return wrapper

@check_log
def addToCart(item):
    print("Added to the Cart: ", item)

print(addToCart("Mobile"))

