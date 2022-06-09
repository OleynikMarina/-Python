def generator_number(stop):
    for num in range(1, stop + 1, 2):
        yield num

add_to_15 = generator_number(15)
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
print(next(add_to_15))
