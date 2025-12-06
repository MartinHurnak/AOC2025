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
    
    def overlaps(self, other):
        return (self.start <= other.start <= self.end) or (self.start <= other.end <= self.end)
    
    def extend(self, other):
        self.start = min(other.start, self.start)
        self.end = max(other.end, self.end)
    
    def __repr__(self):
        return f"{self.start} - {self.end}"

    def __lt__(self, other):
        return self.start < other.start


def main(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    split = lines.index("\n")
    lines = [line.strip() for line in lines]
    ranges_str, ingredients_str = lines[0:split], lines[split:] 
    ranges = []
    for rs in ranges_str:
        start, end = rs.split("-")
        ranges.append(Range(int(start), int(end)))

    ranges.sort()

    new_ranges = []
    for r in ranges:
        r_overlap = False
        for rg in new_ranges:
            if rg.overlaps(r):
                rg.extend(r)
                r_overlap = True
                break
        if not r_overlap:
            new_ranges.append(r)

    fresh_ids = 0
    for r in new_ranges:
        fresh_ids += r.end - r.start + 1
    return fresh_ids


EXPECTED_TEST_RESULT = 14  # TODO change based on test
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
