# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = 6
dictionary = dict(enumerate([3 * i + 1 for i in range(1, n + 1)], 1)) # реализиция через enumerate
print(f"{n = }: {dictionary}")