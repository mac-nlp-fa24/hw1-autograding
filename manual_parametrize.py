# github classroom autorunner does not support parametrized tests?
# https://github.com/classroom-resources/autograding-python-grader/issues/3

import subprocess
import os

self_dir = "./hw1-autograding/"

test_folder = self_dir + "cases/"
header = """import subprocess
undef = ["ppl: nan\\n", "ppl: inf\\n"]
"""

test_template = """def test_match{1}(): 
    with open(\"{0}\".format("in")) as in_f, open(\"{0}\".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)
"""

if __name__ == "__main__":
    examples = []
    for fn in os.listdir(test_folder):
        if fn.endswith("-out.txt"):
            continue
        testnum = fn.split("-")[0]
        testlabel = test_folder + testnum + "-{}.txt"
        examples.append((testlabel, testnum))
    
    out = []
    for testfile, num in examples:
        out.append(test_template.format(testfile, num))

    with open(self_dir + "auto_auto_test.py", "w") as out_f:
        out_f.write(header)
        out_f.write("\n".join(out))






