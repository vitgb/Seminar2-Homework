# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# Вариант 1

n = int(input('Enter the number of coins: '))
eagle = 0
tails = 0

for i in range(n):
    side = int(input('Если орел введите "1", если решка введите "0": '))
    if side == 1:
        eagle += 1
    else:
        tails += 1

if eagle < tails:
    print(eagle)
else:
    print(tails)

# Вариант 2

# n = int(input('Enter the number of coins: '))
# count = 0
# for i in range(n):
#     side = int(input('Если орел введите "1", если решка введите "0": '))
#     if side > 0:
#         count += 1

# if count <= n // 2:
#     print (count)
# else:
#     print (n - count)
