import os, random, json, testcases, time
from check import matrixSum
from operator import itemgetter
start = time.time()
files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
passs = 0
no_pass = 0
peeps = []
efficient = []
forbidden = ["testcases.py", "check.py", os.path.basename(__file__), "__pycache__"]
for i in forbidden:
    if i in files:
        files.remove(i)
amount = len(files)

checks = testcases.gen()
outs = []
print("storing correct test case results")
for check in checks:
    outs.append(matrixSum(check))

#keys = tests.keys()

wrong = []
print("testing solutions")
for index, f in enumerate(files):
    if f.endswith(".py"):
        starteff = time.time()
        unit = __import__(f"{f.split('.')[0]}")
        passed = True
        count = 0
        for i, x in enumerate(checks):
            print(f"solution: {index+1}/{amount} testcase: {i+1}/{len(checks)}    ", end="\r")
            if count < 1:
                try:
                    if unit.matrixSum(x) != outs[i]:
                        passed = False
                        wrong.append(f"{f.split('.')[0]},{x} {outs[i]} {unit.matrixSum(x)}")
                        count += 1
                except BaseException as e:
                    passed = False
                    wrong.append(f"{f.split('.')[0]},{x} {outs[i]} {e}")
                    count += 1
            else:
                count = 0
                break
        endeff = time.time()
        efficient.append([f, endeff-starteff])
        if passed:
            peeps.append(f.split('.')[0])
            passs += 1
        else:
            no_pass += 1
end = time.time()
print("\n\n\n")
for i in wrong:
    print(i)
print("\n\n\nresults:\n")
for i in peeps:
    print(i)
print(f"\npassed {passs}\nnot passed {no_pass}")

print("\n\nStats:")
print(f"\nComputation time: {end-start} seconds")
print("\nEfficiency: ")
for i in sorted(efficient, key=itemgetter(1)):
    found = False
    for w in wrong:
        if i[0].split(".")[0] in w:
            found = True
    if not found:
        print(f"{i[1]:.4f} {i[0]}")