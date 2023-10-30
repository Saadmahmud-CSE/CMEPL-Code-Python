from math import *

def lagrange_interp(x,y,u):
    r = range(len(y))
    a = [y[i]/product(x[i]-x[j]for j in r if j!=i)for i in r]
    return sum(a[i]*product([u-x[j]for j in r if j!=i])for i in r)

def product(a):
    p = 1
    for i in a:
        p *= i
    return p
x = [0,1,2,3]
y = [1,2,3,4]
y0 = int(input("Enter y0: "))
ans = lagrange_interp(x,y,y0)
print("\nAns = {:.4f}".format(ans))