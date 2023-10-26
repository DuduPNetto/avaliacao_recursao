from math import pow

# a
def S(n):
    if n == 1: return 10
    return S(n - 1) + 10
print(S(5))

# b
def A(n):
    if n == 1: return 2
    return pow(A(n - 1), -1)
print(A(5))

# c
def B(n):
    if n == 1: return 1
    return B(n - 1) + pow(n, 2)
print(B(5))

# d
def P(n):
    if n == 1: return 1
    return pow(n, 2) * P(n - 1) + n - 1
print(P(5))

# e
def D(n):
    if n == 1: return 3
    elif n == 2: return 5
    return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)
print(D(5))

# f
def W(n):
    if n == 1: return 2
    elif n == 2: return 5
    return W(n - 1) * W(n - 2)
print(W(5))

# g
def T(n):
    if (n == 1 or n == 2 or n == 3): return n
    return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)
print(T(5))