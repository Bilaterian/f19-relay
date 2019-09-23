#!/usr/bin/env python3

asdf = "0R10L12R10R10R10R3L1A"

# todo: file input
# output in correct format

import sys

def main(args):
    input = args[0]
    
    instructions = asdf
    print(instructions)

    lista = []

    #facing = ['R', 'D', 'L', 'U']

    direction = ''
    acc = ''
    for x in instructions:
        if x == 'R' or x == 'L':
            lista.append(acc)
            lista.append(x)
            acc = ""
        elif x == "A":
            continue
        else:
            acc += x

    lista.append(acc)

    up = 0
    right = 0

    facing = 3

    for x in lista:
        if x == 'R':
            facing = (facing + 1) % 4
        elif x == 'L':
            facing = (facing - 1) % 4
        else:
            if facing == 0:
                right += int(x)
            elif facing == 1:
                up -= int(x)
            elif facing == 2:
                right -= int(x)
            elif facing == 3:
                up += int(x)

    print(up, right)

    # need to finish writing all combinations of right left
    # we have the amount we need to move up and right
    if up == 0 and right == 0:
        print("0A")
    if up < 0 and right < 0:
        print("0L" + str(right*-1) + "L" + str(up*-1))
    if up > 0 and right > 0:
        print(str(up) + "R" + str(right))
    if up < 0 and right > 0:
        print("0R" + str(right))

if __name__ == "__main__":
    main(sys.argv)
