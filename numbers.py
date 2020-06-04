import random
import pyperclip

numbers = ''

for i in range(150):
    numbers += ' ' + str(random.randint(0, 40)) + random.choice(['j', 'k'])
    
pyperclip.copy(numbers)

