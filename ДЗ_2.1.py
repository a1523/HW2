# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

numb = int(input('Введите число: '))
f=1
for i in range(1, numb+1):
    f = i*f
    i+=1
    print(f, end=" ")
    