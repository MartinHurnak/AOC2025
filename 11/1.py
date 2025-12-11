import os
import sys
import networkx as nx

sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    G = nx.DiGraph()

    for line in lines:
        line = line.strip()
        node, outputs = line.split(":")
        outputs = outputs.strip().split(" ")
        for output in outputs:
            G.add_edge(node, output)


    return len(list(nx.all_simple_paths(G, source="you", target="out")))


EXPECTED_TEST_RESULT = 5 # TODO change based on test
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
