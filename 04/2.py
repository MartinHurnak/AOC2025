import os
import sys
sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

def in_map(map, y, x):
    return 0 <= y < len(map) and 0 <= x < len(map[y])

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    
    rolls = 0

    removed = set()
    at_least_one_removed = True
    while at_least_one_removed:
        at_least_one_removed = False
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c =="@" and (y,x) not in removed:
                    neighbour_rolls = 0
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            if dx == 0 and dy == 0:
                                continue
                            if in_map(lines, y+dy, x+dx) and lines[y+dy][x+dx] == "@" and ((y+dy, x+dx) not in removed):
                                neighbour_rolls += 1
                    if neighbour_rolls < 4:
                        rolls += 1
                        removed.add((y,x))
                        print(y,x)
                        at_least_one_removed = True

    return rolls


EXPECTED_TEST_RESULT = 43  
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
