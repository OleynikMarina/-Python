numbers = {'zero':'ноль', 'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}

def num_translate(ing):
    if ing in numbers:
        print(numbers[ing])
    else: return None

num_translate('two')
