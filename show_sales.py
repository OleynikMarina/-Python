from sys import argv

with open('bakery.csv', 'r') as f:
    if len(argv) == 1:
        print(f.read())
    for i, line in enumerate(f, 1):
        if i >= int(argv[1]):
            print(line.strip())
