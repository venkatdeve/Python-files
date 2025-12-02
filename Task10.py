# function to compare two values
def compare(a, b):
    return a == b   # returns True or false

# test functions
def test_case_1():
    return compare(2 + 2, 4)

def test_case_2():
    return compare("hello".upper(), "HELLO")

def test_case_3():
    return compare(len([1, 2, 3]), 4)  # should fail

def test_case_4():
    return compare(10 / 2, 5)

def test_case_5():
    return compare("Python"[0], "P")

# store test cases in a list
tests = [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5]

# runner loop
passed = 0
failed = 0
#for loop for passed and failed

for i, test in enumerate(tests, start=1):
    result = test()
    if result:
        print(f"Test {i}: PASS")
        passed += 1
    else:
        print(f"Test {i}: FAIL")
        failed += 1

# final total
print(f"Total: {len(tests)}, Passed: {passed}, Failed: {failed}")