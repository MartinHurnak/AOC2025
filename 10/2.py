import os
import sys
import scipy
import numpy as np

sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

class Machine:
    def __init__(self, line):
        line = line.strip().split(" ")
        self.buttons = [tuple(int(i) for i in button.strip("()").split(",")) for button in line[1:-1]]
        self.joltage = [int(i) for i in line[-1].strip("{}").split(",")]

    def solve(self):
        a = np.zeros((len(self.buttons), len(self.joltage)))
        for i, button in enumerate(self.buttons):
            for l in button:
                a[i][l] = 1

        return scipy.optimize.linprog([1]*len(self.buttons), A_eq = a.T, b_eq = np.array(self.joltage), integrality=1).fun
        

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    machines = [Machine(line) for line in lines]

    button_presses = 0
    for machine in machines:
        button_presses += machine.solve()
    return button_presses


EXPECTED_TEST_RESULT = 33
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
