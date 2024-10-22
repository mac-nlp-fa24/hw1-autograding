import subprocess
import os
from pathlib import Path

self_dir = "./hw1-autograding/"

run_cmd = "python main.py --train {} --valid {} --smooth {} -n {}"
discount = " --discount {}" 
lambdas = " --coeff {}"
debug = "--debug --byword".split()

output_dir = self_dir + "cases/"
test_folder = self_dir + "data/"

def save(path, output, cmd, i):
    Path(path).mkdir(parents=True, exist_ok=True) 
    with open(path + "test{}-in.txt".format(i), "w") as out_f:
        out_f.write(cmd)
    with open(path + "test{}-out.txt".format(i), "w") as out_f:
        out_f.write(output.stdout.decode())
    with open(path + "test{}-log.txt".format(i), "w") as out_f:
        out_f.write(output.stderr.decode())


coeffss = {3: [[0.5, 0.25, 0.25], 
              [0.34, 0.33, 0.33],
              [0.75, 0.25, 0.0]],
          4: [[0.6, 0.2, 0.1, 0.1],
              [0.5, 0.25, 0.125, 0.125],
              [0.8, 0.1, 0.1, 0.0]]
          }

discounts = [0.3, 0.7, 0.9]

i = 0
for fn in os.listdir(test_folder):
    path = test_folder + fn
    for n in [1, 2, 3, 4]:
        # MLE
        mle_cmd = run_cmd.format(path + "/train.txt", path + "/test.txt", "mle", n) 
        out = subprocess.run(mle_cmd.split() + debug, capture_output=True)
        save(output_dir, out, mle_cmd, i)
        i += 1

        # laplace
        l_cmd = run_cmd.format(path + "/train.txt", path + "/test.txt", "laplace", n) 
        out = subprocess.run(l_cmd.split() + debug, capture_output=True)
        save(output_dir, out, l_cmd, i)
        i += 1

    for n in [3, 4]:
        # interpolation
        for coeffs in coeffss[n]:
            interp_cmd = run_cmd.format(path + "/train.txt", path + "/test.txt", "interp", n) + lambdas.format(",".join((str(x) for x in coeffs))) 
            out = subprocess.run(interp_cmd.split() + debug, capture_output=True)
            save(output_dir, out, interp_cmd, i)
            i += 1

    for n in [3, 4]:
        # backoff
        for d in discounts:
            bo_cmd = run_cmd.format(path + "/train.txt", path + "/test.txt", "backoff", n) + discount.format(d)
            out = subprocess.run(bo_cmd.split() + debug, capture_output=True)
            save(output_dir, out, bo_cmd, i)
            i += 1



