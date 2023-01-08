# Eular scheme for equation `s˙ = −10s(t)`

def euler_explicit(s, dt, N):
    for _ in range(N):
        s = s*(1-10*dt)
    return s

def eular_implicit(s, dt, N):
    for _ in range(N):
        s = s/(1+10*dt)
    return s

N=4
dt = 0.05
print(f"{dt=} {euler_explicit(1, dt, N)=} {eular_implicit(1, dt, N)=}")

dt = 0.1
print(f"{dt=} {euler_explicit(1, dt, N)=} {eular_implicit(1, dt, N)=}")

dt = 0.2
print(f"{dt=} {euler_explicit(1, dt, N)=} {eular_implicit(1, dt, N)=}")

dt = 0.25
print(f"{dt=} {euler_explicit(1, dt, N)=} {eular_implicit(1, dt, N)=}")

print("---")
for dt in [0.01, 0.05, 0.1, 0.15, 0.2, 0.25]:
    print(f"{dt=} {euler_explicit(1, dt, 100)=}")
