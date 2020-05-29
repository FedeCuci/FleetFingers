import random

combinations = input('combinations ')

if ',' in combinations:
    combinations = combinations.split(',')

with open('words.txt', 'r') as words:
    words = words.readlines()

    for i in words:
        for i in 
