price = [57.8, 46.51, 97, 5.34, 5, 32.9, 3, 12, 100.4, 0.9]

def new_price(num_obj):
    str_obj = f"{num_obj:.{2}f}"
    str_obj = f"{str_obj[:-3]} руб {str_obj[-2:]} коп"
    return str_obj


print(', '. join(list(map(new_price, price))))
