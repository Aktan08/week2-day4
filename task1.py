"""
Напишите функцию который будет определять введенный год, високосный или
нет.
"""
print("введите год:")

input_ = int(input())

if input_ % 4 != 0:
    print("не вискосный год")

elif input_ % 100 == 0:
    if input_ % 400 == 0:
        print("Високосный год")
    else:
        print("не вискосный год")
else:
    print("Високосный год")