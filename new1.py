import sympy

x, y = sympy.symbols('x, y')
f = 3 * x / 125


print(sympy.integrate(f, (x, y, 5), (y, 0, 5)))#二重积分定积分