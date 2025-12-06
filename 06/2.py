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
    
    lines = [line.strip("\n") for line in lines]
    
    total = 0
    result = 0
    for col in range(len(lines[0])):
        
        # if last line has operator, that means a new problem
        if lines[-1][col] == "+":
            result = 0
            operator = "+"
        elif lines[-1][col] == "*":
            result = 1
            operator = "*"

        number = 0
        for line in lines[:-1]:
            if line[col] == " ":
                continue
            number = number * 10 + int(line[col])

        if number: 
            if operator == "+":
                result += number
            else:
                result *= number
        else: # if number is 0, column was full of spaces -> finish the problem
            total += result

    total += result # last problem has no empty spaces after it
    return total


EXPECTED_TEST_RESULT = 3263827  
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
