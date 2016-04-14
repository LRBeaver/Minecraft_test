__author__ = 'lyndsay.beaver'
import random

temp = []
middle = []
layout = []

width = 5
height = 5
starting = random.randint(1, 6)
temp.append(starting)

print(temp)
for i in range(1, width):
    previous = starting + random.randint(1, 6)
    if altered == 1 and altered <= 4:
        temp.append(altered)
        layout.append('Sand')
    elif altered == 5 and altered <= 7:
        temp.append(altered)
        layout.append('Water')
    elif altered == 8 and altered <= 10:
        temp.append(altered)
        layout.append('Grass')
    else:
        temp.append(altered)
        layout.append('Stone')

print(temp)
#print(layout)
