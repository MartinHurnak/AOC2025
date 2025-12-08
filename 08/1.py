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
    return sqrt(sum(((x - y) ** 2) for x, y in zip(box1, box2)))


def main(filename, num_pairs):
    with open(filename) as f:
        lines = f.readlines()

    boxes = [tuple(int(coord) for coord in box.split(",")) for box in lines]

    distances = []
    for i, box in enumerate(boxes):
        for other_box in boxes[i + 1 :]:
            if box != other_box:
                distances.append((distance(box, other_box), box, other_box))
    distances.sort()

    circuits = nx.Graph()
    for _, box1, box2 in distances[:num_pairs]:
        circuits.add_edge(box1, box2)

    # PART 1
    components = [len(circuit) for circuit in list(nx.connected_components(circuits))]
    components.sort(reverse=True)

    return components[0] * components[1] * components[2]


EXPECTED_TEST_RESULT = 40
test_and_run(
    main,
    testfile,
    EXPECTED_TEST_RESULT,
    inputfile,
    test_parameters=(10,),
    main_paramenters=(1000,),
)
