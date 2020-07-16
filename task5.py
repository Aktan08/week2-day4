"""Три ввода и сверьте их, все ли равны или что-либо из них?"""

print ("введите первое значение:")
first_value = input()
print ("введите второе значение:")
second_value = input()
print ("введите третье значение:")
third_value = input()
if first_value is second_value is third_value :
    print ("все трое совподают")
elif first_value is second_value or first_value is third_value: 
    print("двое совпадают")
elif second_value is first_value or second_value is third_value: 
    print("двое совпадают")
elif third_value is first_value or third_value is second_value: 
    print("двое совпадают")
else :
    print("ничего не совподает")