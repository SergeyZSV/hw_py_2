# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

new_list = [1.1, 1.2, 3.1, 5, 10.01]




def find_fraction():
    for i in range(0, len(new_list)):
        new_list[i] =  new_list[i] - round(new_list[i])

def max_min_fraction():
    max = new_list[0]
    min = new_list[0]
    for i in range(1, len(new_list) - 1):
        if new_list[i] > max:
            max = new_list[i]
        if new_list[i] < min:
            min = new_list[i]
    print(f'Разница между максимальным и минимальным элементом равна {max -  min}')

print(f'Дан список: {new_list}')
find_fraction()
max_min_fraction()



