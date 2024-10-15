import subprocess
import os
from pathlib import Path

self_dir = "./hw1-autograding/"

test_folder = self_dir + "cases/"
undef = ["ppl: nan\n", "ppl: inf\n"]

def test_match(testnum): 
    with open(testnum.format("in")) as in_f, open(testnum.format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def pytest_generate_tests(metafunc):
        examples = []
        for fn in os.listdir(test_folder):
            if fn.endswith("-out.txt"):
                continue
            testlabel = test_folder + fn.split("-")[0] + "-{}.txt"
            examples.append(testlabel)

        metafunc.parametrize("testnum", examples)





