import os
import sys

from shapely import Polygon

sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")


def rectangle(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    corners = [tuple(int(a) for a in line.strip().split(",")) for line in lines]
    green_area = Polygon(corners)
    max_size = 0
    for i, c1 in enumerate(corners):
        for c2 in corners[i + 1 :]:
            rect = Polygon(
                [(c1[0], c1[1]), (c1[0], c2[1]), (c2[0], c2[1]), (c2[0], c1[1])]
            )
            if rect.within(green_area):
                max_size = max(max_size, rectangle(c1, c2))

    return max_size


EXPECTED_TEST_RESULT = 24
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
