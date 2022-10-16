# Реализуйте алгоритм перемешивания списка.
import random

arr = input("Введите элементы списка(элементы списка вводить через запятую): ")
split_arr = [int(i) for i in arr.split(',')]
print('Изачальный список: ')

print(split_arr)

print('Перемешанный список: ')

print(sorted(split_arr, key=lambda x: random.random())) # реализация через lambda