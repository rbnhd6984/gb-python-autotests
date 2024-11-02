a = 3
b = 5


# def f(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     elif b % 2 == 0:
#         return f(a * a, b // 2)
#     else:
#         return a * f(a * a, (b - 1) // 2)
def f(a, b):
    if b == 0:
        return 1
    return f(a, b - 1) * a


print(f(a, b))
# temp = a
# while b != 1:
#     a *= temp
#     b -= 1
