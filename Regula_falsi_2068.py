y = input('Non-linear function f(x): ')
def f(x):
    f = eval(y)
    return f

a1 = int(input('Start Range,a: '))
a = float(a1)
fa = f(a)
b1 = int(input('End Range,b: '))
b = float(b1)
fb = f(b)
e = float(input('Tolerance Error,e: '))
while fa * fb > 0:
    a = a + 1
    b = b + 1
    fa = f(a)
    fb = f(b)

if fa * fb > 0:
    print('change a and b')
else:
    c = ((b * fa) - (a * fb)) / (fa - fb)
    fc = f(c)
    print('\n\n    a \t\t\t b \t\t\t   c \t\t\t   f(c)\n')

    while abs(fc) > e:
        print(f'{a:2.6f}', '\t\t', f'{b:2.6f}', '\t\t', f'{c:2.6f}', '\t\t', f'{fc:2.6f}', '\n')
        if fc * fa < 0:
            b = c
        else:
            a = c

        c=((b*fa)-(a*fb))/(fa-fb)
        fc = f(c)

    print('\nRoot is:', c, ' \n')
