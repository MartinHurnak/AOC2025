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


    print(G)
    fft_nodes = nx.ancestors(G, "fft") | nx.descendants(G, "fft") | {"fft"}
    dac_nodes = nx.ancestors(G, "dac") | nx.descendants(G, "dac") | {"dac"}
    print("dac" in nx.ancestors(G, "fft"), "dac" in nx.descendants(G, "fft"))

    svr_fft_G = G.subgraph(nx.ancestors(G, "fft") | {"fft"})
    fft_dac_G = G.subgraph((nx.descendants(G, "fft") & nx.ancestors(G, "dac"))|{"fft", "dac"})
    dac_out_G = G.subgraph(nx.descendants(G, "dac") | {"dac"})
    print(svr_fft_G)
    print(fft_dac_G)
    print(dac_out_G)

    svr_fft = list(nx.all_simple_paths(G, source="svr", target="fft"))
    print("svr_fft", svr_fft[0])
    fft_dac = list(nx.all_simple_paths(G, source="fft", target="dac"))
    print("fft_dac", fft_dac[0])
    dac_out = list(nx.all_simple_paths(G, source="dac", target="out"))
    print("dac_out", dac_out[0])
    return len(svr_fft) * len(fft_dac) * len(dac_out)


EXPECTED_TEST_RESULT = 2 # TODO change based on test
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
