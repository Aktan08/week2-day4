"""
14.Дан список, упорядоченный по неубыванию элементов в нем. Определите,
сколько в нем различных элементов.(input: 1, 2, 2, 3, 3, 3 output: 3)
"""
list_ = [1, 3,3,3,4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6]
raznye = 1
for num in range(len(list_)-1):
    if list_[num] != list_[num + 1]:
        raznye += 1
razlichnye_elementy = raznye
print(razlichnye_elementy)

