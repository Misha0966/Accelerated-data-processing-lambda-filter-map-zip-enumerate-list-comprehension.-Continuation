# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] 
import math
n = int(input('Введите число: '))
list = [math.factorial(i) for i in range(1,n+1)] # реализация  list comprehension
print(list)