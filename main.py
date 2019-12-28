#!/usr/bin/env python3

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

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle_input_file")
    ns = parser.parse_args()

    with open(ns.puzzle_input_file) as f:
        opline = f.readline()
        opcodes = [int(op) for op in opline.split(",")]

    outcodes = check(opcodes)
    new_codes = ",".join([str(c) for c in outcodes])
    print(f"New codes: {new_codes}")

if __name__=="__main__":
    main()
