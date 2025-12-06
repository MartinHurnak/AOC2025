import os
import sys
sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.start < other.start


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

       
    split = lines.index("\n")
    lines = [line.strip() for line in lines]
    ranges_str, ingredients_str = lines[0:split], lines[split+1:] 
    ranges = []
    for rs in ranges_str:
        start, end = rs.split("-")
        ranges.append(Range(int(start), int(end)))
    ranges.sort()

    fresh_ids = 0
    for i in ingredients_str:
        for r in ranges:
            if r.start <= int(i) <= r.end:
                fresh_ids +=1
                break

    return fresh_ids


EXPECTED_TEST_RESULT = 3  # TODO change based on test
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
