import os
import sys
import re
sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")



def main(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    lines = [re.sub(r'\s+', ' ', line) for line in lines]
    lines = [line.strip().split(" ") for line in lines]
    
    
    total = 0
    for col in range(len(lines[0])):
        operator = lines[-1][col]
        result = 1 if operator == "*" else 0
        for line in lines[:-1]:
            if operator == "+":
                result += int(line[col])
            elif operator == "*":
                result *= int(line[col])
        total += result

    return total


EXPECTED_TEST_RESULT = 4277556  
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
