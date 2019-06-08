#!/usr/bin/env python

file = 'strategies.txt'

strategies = []

with open(file, 'r+') as f:
    for line in f:
        if line != '' :
            strategies.append(line.strip())

print(strategies)