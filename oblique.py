#!/usr/bin/env python

import random

file = 'strategies.txt'

strategies = []

with open(file, 'r+') as f:
    for line in f:
        if line != '' :
            strategies.append(line.strip())


print(random.choice(strategies))

