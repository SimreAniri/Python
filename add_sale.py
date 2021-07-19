import sys


with open('bakery.csv ', 'a') as f:
    f.write(f'{sys.argv[1]:<20}\n')
