import os
import sys
sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    splits = [[True if c == "^" else False for c in line.strip()] for line in lines]
    beams = [True if c == "S" else False for c in lines[0].strip()]

    split_count = 0
    for line in splits[1:]:
        new_beams = [False] * len(beams)
        for i in range(len(beams)):
            if line[i] and beams[i]:
                split_count += 1
                if i-1 >= 0:
                    new_beams[i-1] = True
                if i+1 < len(new_beams):
                    new_beams[i+1] = True
            elif beams[i]:
                new_beams[i] = True
        beams = new_beams

    return split_count

EXPECTED_TEST_RESULT = 21 
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
