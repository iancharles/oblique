#!/usr/bin/env python

import random

file = 'strategies.txt'

strategies = []

with open(file, 'r+') as f:
    for line in f:
        if line != '' :
            strategies.append(line.strip())


def picker():
    return random.choice(strategies)

print(picker())
