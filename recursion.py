def n():    
    n=int(input("enter the n--"))
    return n

def n_natural(n):
    if n<1:
        return       
    n_natural(n-1)
    print(n)
        

n_natural(10)
