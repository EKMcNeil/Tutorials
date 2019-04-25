#!/usr/bin/python3

import sys

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

count = 0
for row in game:
    print(row)
    count += 1

print("   0, 1, 2")

for count, row in enumerate(game):
    print(count, row)
    sys.exit(1)
