"""
23.Дан список. Выведите те его элементы, которые встречаются в списке
только один раз. Элементы нужно выводить в том порядке, в котором они
встречаются в списке.(input: 1, 2, 2, 3, 3, 3 output: 1)

"""
list_ = [1, 2, 2, 3, 3, 3]
counter = 0
for nums in range(len(list_)):
    for num in range(nums + 1, len(list_)):
        if list_[nums] == list_[num]:
            counter += 1
print(counter)

