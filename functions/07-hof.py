def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print('ejemplo con funciones normales ->', result)

# Ejemplo con funciones lambda
increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x)

# 2 + (2 + 1)
result = high_ord_func_v2(2, increment_v2)
print('ejemplo con funciones lambda -> ', result)

result = high_ord_func_v2(2, lambda x: x + 5)
print(result)
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)
result = high_ord_func_v2(2, lambda x: x - 5)
print(result)