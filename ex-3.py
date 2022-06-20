import re

def type_logger(func):
    def logger(*args):
        name_func = (re.findall(r'\s(.+)\s[a]', str(func)))[0]
        otvet = ""
        for i in args:
            if str(i).isdigit():
                rez = func(i)
                otvet = otvet + f'{name_func}({i}: {type(i)}--- результат {rez})\n'
            else:
                otvet = otvet + f'{name_func}({i}: {type(i)})\n'
        return otvet
    return logger
@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(222,"gfhfghfgh",55.5)
print(a)
