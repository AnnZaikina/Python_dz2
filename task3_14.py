# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 5 > 24; 30> 24816

n = int (input("Введите число: "))
a = int (1)
res = str ()

for i in range (n):
    if i == 2**a:
        b = str (i)
        res += b
        a += 1

print (res)

