import subprocess
undef = ["ppl: nan\n", "ppl: inf\n"]
def test_matchtest10(): 
    with open("./hw1-autograding/cases/test10-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test10-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest26(): 
    with open("./hw1-autograding/cases/test26-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test26-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest38(): 
    with open("./hw1-autograding/cases/test38-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test38-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest34(): 
    with open("./hw1-autograding/cases/test34-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test34-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest7(): 
    with open("./hw1-autograding/cases/test7-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test7-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest5(): 
    with open("./hw1-autograding/cases/test5-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test5-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest9(): 
    with open("./hw1-autograding/cases/test9-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test9-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest12(): 
    with open("./hw1-autograding/cases/test12-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test12-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest28(): 
    with open("./hw1-autograding/cases/test28-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test28-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest36(): 
    with open("./hw1-autograding/cases/test36-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test36-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest24(): 
    with open("./hw1-autograding/cases/test24-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test24-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest1(): 
    with open("./hw1-autograding/cases/test1-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test1-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest20(): 
    with open("./hw1-autograding/cases/test20-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test20-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest32(): 
    with open("./hw1-autograding/cases/test32-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test32-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest16(): 
    with open("./hw1-autograding/cases/test16-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test16-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest30(): 
    with open("./hw1-autograding/cases/test30-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test30-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest22(): 
    with open("./hw1-autograding/cases/test22-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test22-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest14(): 
    with open("./hw1-autograding/cases/test14-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test14-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest18(): 
    with open("./hw1-autograding/cases/test18-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test18-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest3(): 
    with open("./hw1-autograding/cases/test3-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test3-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest6(): 
    with open("./hw1-autograding/cases/test6-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test6-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest39(): 
    with open("./hw1-autograding/cases/test39-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test39-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest27(): 
    with open("./hw1-autograding/cases/test27-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test27-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest35(): 
    with open("./hw1-autograding/cases/test35-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test35-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest11(): 
    with open("./hw1-autograding/cases/test11-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test11-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest37(): 
    with open("./hw1-autograding/cases/test37-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test37-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest29(): 
    with open("./hw1-autograding/cases/test29-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test29-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest25(): 
    with open("./hw1-autograding/cases/test25-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test25-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest13(): 
    with open("./hw1-autograding/cases/test13-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test13-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest4(): 
    with open("./hw1-autograding/cases/test4-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test4-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest8(): 
    with open("./hw1-autograding/cases/test8-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test8-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest17(): 
    with open("./hw1-autograding/cases/test17-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test17-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest21(): 
    with open("./hw1-autograding/cases/test21-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test21-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest33(): 
    with open("./hw1-autograding/cases/test33-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test33-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest0(): 
    with open("./hw1-autograding/cases/test0-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test0-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest2(): 
    with open("./hw1-autograding/cases/test2-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test2-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest15(): 
    with open("./hw1-autograding/cases/test15-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test15-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest19(): 
    with open("./hw1-autograding/cases/test19-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test19-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest31(): 
    with open("./hw1-autograding/cases/test31-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test31-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)

def test_matchtest23(): 
    with open("./hw1-autograding/cases/test23-{}.txt".format("in")) as in_f, open("./hw1-autograding/cases/test23-{}.txt".format("out")) as out_f:
        out = subprocess.run(in_f.read().split(), capture_output=True)
        correct = out_f.read()
        if correct in undef:
            assert(out.stdout.decode() in undef)
        else:
            assert(out.stdout.decode() == correct)
