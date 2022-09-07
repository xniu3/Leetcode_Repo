import sympy

# x, y = sympy.symbols('x, y')
# f = 3 * y**2 / 125

# print(sympy.integrate(f, x, y))#不定积分
# print(sympy.integrate(f, (x, y, 5), (y, 0, 5)))#二重积分定积分

x, y = sympy.symbols('x, y')
f = 3 * x**2 * y / 4
print(sympy.integrate(f, (x, 2 * y, 2), (y, 0, 1)))#二重积分定积分
