def school(tutors, klasses):
    i = 0
    while i < len(tutors) and i < len(klasses):
        yield tutors[i], klasses[i]
        i += 1
    while i < len(tutors):
        yield tutors[i], None
        i += 1

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

for i in school(tutors, klasses):
    print(i)

print('-'*30)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']

for i in school(tutors, klasses):
    print(i)
