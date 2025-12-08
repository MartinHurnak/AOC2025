import os
import sys
from math import sqrt

import networkx as nx

sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

def distance(box1, box2):
    return sqrt(sum(((x - y) ** 2) for x,y in zip(box1, box2)))


def main(filename, ):
    with open(filename) as f:
        lines = f.readlines()

    boxes = [tuple(int(coord) for coord in box.split(",")) for box in lines]
    circuits = nx.Graph()
    for box in boxes:
        circuits.add_node(box)

    distances = []

    for i, box in enumerate(boxes):
        for other_box in boxes[i + 1:]:
            if box != other_box:
                distances.append((distance(box, other_box), box, other_box))
    distances.sort()

    for _, box1, box2 in distances:
        circuits.add_edge(box1, box2)
        if nx.is_connected(circuits):
            return box1[0] * box2[0]



EXPECTED_TEST_RESULT = 25272
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
