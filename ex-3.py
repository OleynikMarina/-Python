with open('users.csv', 'r') as u:
    users = u.read().splitlines()
with open('hobby.csv', 'r') as h:
    hobby = h.read().splitlines()

if len(hobby) < len(users):
    while len(hobby) != len(users):
        hobby.append(None)
elif len(users) < len(hobby):
    exit(1)

result = dict(zip(users, hobby))

with open('ex-3-6.txt', 'w') as f:
    for key, val in result.items():
        f.write('{}: {}\n'.format(key, val))
