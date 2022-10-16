# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];

massive = [2,3,4,5,6]

def multi (mass):
    new_massive = []
    for (i,j) in zip(mass [0: int(len(mass)/2+1): 1], # реализация zip
                     mass [-1: int(len(mass)/2-1): -1]):
        new_massive.append(i*j)
    return new_massive

print(f"произведения пар чисел списка равна: {multi(massive)}")