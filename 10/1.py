import os
import sys
from collections import deque

sys.path.insert(0, os.getcwd())
from test_run import test_and_run

dirname = os.path.dirname(__file__)
testfile = os.path.join(dirname, "test.txt")
inputfile = os.path.join(dirname, "input.txt")

class QueueItem:
    def __init__(self, lights, buttons):
        self.lights = lights
        self.buttons = buttons

class Machine:
    def __init__(self, line):
        line = line.strip().split(" ")
        self.lights = [True if c =="#" else False for c in line[0].strip("[]")]
        self.buttons = [tuple(int(i) for i in button.strip("()").split(",")) for button in line[1:-1]]

    def __repr__(self):
        return str(self.lights) + str(self.buttons)

    def bfs(self):
        queue = deque()
        queue.append(QueueItem([False] * len(self.lights), []))

        print(self.lights)
        while queue:
            item = queue.popleft()
            # print(item.lights, item.buttons)
            if item.lights == self.lights:
                print(item.buttons)
                return len(item.buttons)
            for button in self.buttons:
                new_lights = item.lights.copy()
                for l in button:
                    new_lights[l] = not new_lights[l]
                    queue.append(QueueItem(new_lights, item.buttons + [button]))



def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    machines = [Machine(line) for line in lines]

    button_presses = 0
    for machine in machines:
        button_presses += machine.bfs()
    return button_presses


EXPECTED_TEST_RESULT = 7
test_and_run(main, testfile, EXPECTED_TEST_RESULT, inputfile)
