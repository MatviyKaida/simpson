import numpy as np

# Глобальні змінні
a = -10
b = 10
h = 0
eps = 1e-8

# Функція f(x)
def f(x):
    return np.sin(x) + np.cos(2 * x)

# Первісна F(x) для функції f(x)
def F(x):
    return -np.cos(x) + np.sin(2 * x) / 2

# Метод Сімпсона для числового інтегрування
def Integral(N):
    global a, b, h
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    
    # Застосування формули Сімпсона
    Int_N = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    Int_N = Int_N * (h / 3)
    return Int_N

# Початкові дані
I0 = F(b) - F(a)
N = 0
with open("inNopt.txt", "w") as file:
    # Виконуємо інтеграцію до досягнення точності
    while N <= 10000:
        N += 2
        epsI = abs(Integral(N) - I0)
        file.write(f"{N} {epsI}\n")
        if epsI <= eps:
            break

    # Оптимальне значення N
    Nopt = N
    epsopt = abs(Integral(Nopt) - I0)
    print(f"Nopt = {Nopt} \t epsopt = {epsopt}\n{Integral(N)}\n{I0}")