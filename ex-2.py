lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for value in lst:
    i = lst.index(value)
    if lst[i].isdigit():
        lst[i] = lst[i].zfill(2)
    if lst[i].startswith('+' or '-') and ((lst[i])[1:].isdigit()):
        lst[i] = lst[i].zfill(3)

print(' '.join(lst))