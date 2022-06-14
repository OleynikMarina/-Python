import sys

with open('bakery.csv', 'a') as f:
    f.write('{}\n'.format(sys.argv[1]))
