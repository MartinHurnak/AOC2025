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
    for i, box in enumerate(boxes):
        for other_box in boxes[i + 1:]:
            circuits.add_edge(box, other_box, weight=distance(box, other_box))

    # we are looking for longest edge in minimum spanning tree
    edges = nx.minimum_spanning_edges(circuits)
    # edges look like ((216, 146, 977), (117, 168, 530), {'weight': 458.360120429341})
    longest_edge = max(edges, key= lambda e: e[-1]["weight"])
    return longest_edge[0][0] * longest_edge[1][0]

EXPECTED_TEST_RESULT = 25272
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
