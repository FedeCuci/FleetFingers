# https://stackoverflow.com/questions/26367812/appending-to-list-in-python-dictionary

import random
import string


practice = input('Combinations: ')

combinations = practice.split(' ') 

# if '' in combinations:
    # combinations.remove('')

final_combinations = {}

with open ('words.txt', 'r') as words:
    words = words.readlines()
    for i in combinations: # Loop over the combinations entered by the user
        i.rstrip()
        for j in words: # Loop over all the words
            j = j.title()
            if i in j: 
                special_character = random.choice(string.punctuation + string.digits) # Create a varible for a special character
                final_combinations.setdefault(i, []).append(j.title().rstrip() + special_character) # Add the word with the current combination to the array of words containing this combination

filename = '-'.join(combinations)

with open('files/{}.txt'.format(filename), 'w') as file:
    for i in final_combinations.values():
        i = i.shuffle()
        del i[99:-1]
        file.write(' '.join(i) + '\n')
