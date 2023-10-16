numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_miss = 4

numbers_sum = sum(numbers[:index_miss]) + sum(numbers[index_miss + 1:])
numbers_quantity = len(numbers)
average_numbers = numbers_sum / numbers_quantity
numbers[index_miss] = average_numbers
print("Измененный список:", numbers)

