duration = int(input('Введите количество секунд: '))

days = duration // 86400
hours = (duration % 86400) // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60

if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3600:
    print(minutes, 'мин', seconds, 'сек')
elif duration >= 3600 and duration < 86400:
    print(hours, 'час',  minutes, 'мин', seconds, 'сек')
else:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')