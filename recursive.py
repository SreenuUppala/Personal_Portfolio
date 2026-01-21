#Recursion
"""
def num(n):
    if n==0:
        return
    else:
        num(n - 1)
    print(n)
num(8)
"""
"""
def num(n):
    if n==0:
        return 1
    return n*num(n-1)
print(num(8))
"""
"""
def num(n):
    if n<0:
        return
    print(n)
    num(n-1)
num(8)
"""
#Fibonocci
"""
def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for  i  in range(10):
    print(fib(i))
"""
#reverse Stack
def reverse(n):
    if not n:
        return 0
    top=n.pop()
    print(top)

    bottom=n.append(top)
    print(bottom)
    return reverse(bottom)

s=[1,2,3,4,5]
print(reverse(s))


