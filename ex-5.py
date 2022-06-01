from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    random_jokes = []
    for i in range(n):
        word_nouns = choice(nouns)
        word_adverbs = choice(adverbs)
        word_adjectives = choice(adjectives)
        joke = f'{word_nouns} {word_adverbs} {word_adjectives}'
        random_jokes.append(joke)
    return random_jokes

print(get_jokes(5))
