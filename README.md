# HW1 Autograder

`generate_tests.py` constructs the test cases in `./cases` with the format test{n}-{in/out/log}.txt

`manual_parametrize.py` constructs a non-parametrized testfile for pytest under the filename `auto_auto_test.py`

`auto_test_.py` is a parametrized version of the tests, but breaks under github classroom's autograder  

## Checking Test Cases:

Each test case is structured so that you should be able to run your code with the line in `test{n}-in.txt` and get output to stdout (i.e., with a print statement) that looks like `test{n}-out.txt`. the code does handle ambiguity about returning *inf* vs *nan*, but if you handled infinitely ppls differently, let me know and I can correct it.

If you got a test wrong, I recommend going through `test{n}-log.txt`, which provides relevant counts and (base-2) log-probabilities used to compute the final ppl. Add print statements or use a debugger to check whether you get different numbers! The early tests use the relatively short example in `data/mini/train.txt` and evaluate on the same text (copied to `data/mini/test.txt`). you should be able to compute these probabilities by hand, and verify correctness! If my examples happen to be incorrect (which they may be!), let me know and I can correct the text case for the class. You will be justly rewarded beyond (hopefully) now getting that example correct. 


