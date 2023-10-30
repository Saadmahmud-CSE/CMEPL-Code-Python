from math import sin, pi
y = input('Function f(x) : ')

def f(x):
    f = eval(y)
    return f

a = int(input('Enter lower limit : '))
b = int(input('Enter upper limit : '))
n = int(input('Enter number of interval : '))
dx = (b - a) / n
integration = f(a) + f(b)

for i in range(1, n):
    integration += 2 * f(a + i * dx)

integration = (dx / 2) * integration
print('Integral = %f' % integration)