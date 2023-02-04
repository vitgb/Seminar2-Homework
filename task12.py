# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input('Enter the sum of numbers X and Y: '))
P = int(input('Enter the product of numbers X and Y: '))
x = 0
y = 0
i = 0
res = 0

while i <= 1000: # (S-2) * y != P:
    res = i*(S-i)
    if res == P:
        y = i
    i += 1
print('x =', y)
print('y =', S-y)


       

