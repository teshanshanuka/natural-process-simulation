# This is wrong apparently. No idea why

def leap_frog(x, v, dt, acc_func):
    x2 = x + dt*v
    v2 = v + dt*acc_func(x2)
    return  x2, v2

def acc(r, m):
    G = 6.67408e-11
    return G*m/(r*r)

# x0_1 = 0
# x0_2 = 1e6
# v1_0 = 0
# v2_0 = 0
m1 = 1e20
m2 = 1e12

x1 = 6.67408e-5
x2 = 993325.92
v1 = 6.67408e-8
v2 = -6.67408
dt = 1000

for i in range(10):
    x1new, v1new = leap_frog(x1, v1, dt, lambda m: acc(x2-x1, m2))
    x2new, v2new = leap_frog(x2, v2, dt, lambda m: acc(x2-x1, m1))
    print(f"step {i+1} 1:{(x1new, v1new)} 2:{(x2new, v2new)}")

    x1, v1, x2, v2 = x1new, v1new, x2new, v2new