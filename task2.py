# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

new_list = [2, 3, 4, 5, 6]

print(f'Дан список: {new_list}')

for i in range(len(new_list)):
    if i >= len(new_list) / 2:
        break
    multi = new_list[i] * new_list[len(new_list) - 1 - i]
    print(f'Произведение {i + 1} и {len(new_list) - i} элементов = {multi}')