"""
Получите от пользователя 2 значения и ответьте, будет ли сумма этих двух значений
равна, больше или меньше чем 5.
"""
print ("введите первое число:")
first_value = int(input())
print ("введите второе число:")
second_value = int(input())
if first_value + second_value > 5:
    print ("сумма больше 5")
else: 
    print("cумма меньше 5")