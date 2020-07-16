# 22.Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
# другу. Считается, что любые два элемента, равные друг другу образуют
# одну пару, которую необходимо посчитать.(input: 1, 2, 3, 2, 3 output: 2)

list_ =["aktan", 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 1]

counter = 0
for num in list_:

    list_.count(num)
    if list_.count(num) == 2 :
        counter +=1
    elif list_.count(num) == 4 and list_.count(num) % 2 == 0 :
        while list_.count(num) == 2:
            list_.count(num)/2
            counter +=2
            print(counter)
            if list_.count(num)/2 == 3:
                list_.count(num)+1
                continue

new_counter = int(counter)
print(new_counter)
print(list_[0])
# for nums in list_ :
#     counted = list_.count[nums]
#     print(counted)




# counter = 0
# for nums in range(len(list_)):
#     for num in range(nums, len(list_)):
#         if list_[nums] == list_[num]:
#             counter += 1
# print(counter)
