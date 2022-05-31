def thesaurus(*args):
    letter_name = {}
    for name in args:
        name = name.capitalize()
        val = letter_name.setdefault(name[0], [name])
        if name not in val:
            letter_name[name[0]].append(name)
    return print(letter_name)

thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Игорь", "Кристина")
