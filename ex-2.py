numbers = list(range(1, 1000, 2))
numbers_cub = []
sum_numbers = 0
new_numbers = []
new_sum_num = 0

for i in numbers:
    numbers_cub.append(i**3)
print(numbers_cub)

for i in range(len(numbers_cub)):
    sum_numbers_cub = 0
    cub = numbers_cub[i]
    while cub != 0:
        sum_numbers_cub = sum_numbers_cub + cub % 10
        cub = cub // 10
    if sum_numbers_cub % 7 == 0:
        sum_numbers = sum_numbers + numbers_cub[i]
print(sum_numbers)

for i in numbers_cub:
    new_numbers.append(i+17)
print(new_numbers)

for i in range(len(new_numbers)):
    new_sum = 0
    new_cub = new_numbers[i]
    while new_cub != 0:
        new_sum = new_sum + new_cub % 10
        new_cub = new_cub // 10
    if new_sum % 7 == 0:
        new_sum_num = new_sum_num + new_numbers[i]
print(new_sum_num)