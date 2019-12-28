#!/usr/bin/env python3
import copy
import sys

OP_ADD = 1
OP_MUL = 2
OP_STOP = 99

def operate(opcodes, index):
    op = opcodes[index]
    arg1 = opcodes[opcodes[index+1]]
    arg2 = opcodes[opcodes[index+2]]
    save_pos = opcodes[index+3]
    if op == OP_ADD:
        opcodes[save_pos] = arg1 + arg2
    elif op == OP_MUL:
        opcodes[save_pos] = arg1 * arg2
    else:
        raise ValueError(f"Invalid opcode ({op}) found at index {index}")
    return opcodes

def check(opcodes):
    index = 0
    while opcodes[index] != OP_STOP:
        opcodes = operate(opcodes, index)
        index += 4
    return opcodes

class FoundSolutionException(Exception):
    pass

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle_input_file")
    ns = parser.parse_args()

    with open(ns.puzzle_input_file) as f:
        opline = f.readline()
        opcodes = [int(op) for op in opline.split(",")]

    try:
        for verb in range(100):
            for noun in range(100):
                opcodes[1] = noun
                opcodes[2] = verb
                outcodes = check(copy.copy(opcodes))
                output = outcodes[0]
                if output == 19690720:
                    raise FoundSolutionException()
    except FoundSolutionException:
        print(f"Found a solution for verb={verb} and noun={noun}")
    else:
        print("Program failed to find a solution")
        sys.exit(-1)
    print(f"Output: 100 * noun + verb = {100 * noun + verb}")

if __name__=="__main__":
    main()
