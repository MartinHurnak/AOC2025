import os
import sys
import networkx as nx

sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test2.txt")
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

    # fft and dac need to be in specific order, otherwise graph would not be DAG
    # based on ancestors/descendants it needs to be fft->dac
    # split the graph into 3 parts (svr->fft, fft->dac, dac->out)
    # then reconstructing it will keep only svr->out paths going through fft and dac
    svr_fft_G = G.subgraph((nx.ancestors(G, "fft")) | {"fft"} )
    fft_dac_G = G.subgraph((nx.descendants(G, "fft") & nx.ancestors(G, "dac"))|{"fft", "dac"})
    dac_out_G = G.subgraph((nx.descendants(G, "dac"))| {"dac"})
    G = G.edge_subgraph(svr_fft_G.edges | fft_dac_G.edges | dac_out_G.edges)

    # nx.all_simple_paths seems too tedious to iterate through all combinations
    # we are only interested in number
    # each node has that many paths going into it from svr that is the sum of it's predecessors's paths
    paths = {"svr": 1}
    for node in nx.topological_sort(G):
        if node == "svr": 
            continue
        # thanks to topological sort, we can rely on predecessors being resolved
        paths[node] = sum(paths[predecessor] for predecessor in G.predecessors(node))
    return paths["out"]


EXPECTED_TEST_RESULT = 2 
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
