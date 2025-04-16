#################################################
# Calculator tests for clean code class
# Class : Software Engineering II.2405
# Author : Anthony Nora
# Date : 16/04/2025
#################################################

from calculator import Calculator

class CalculatorTest:
    
    def __init__(self):
        self.calculator = Calculator()
        self.passed = 0
        self.failed = 0

    def run(self):
        self.single_integer()
        self.single_float()
        self.addition()
        self.multiple_additions()
        self.subtraction()
        self.multiplication()
        self.multiple_operations()
        self.parenthesis()
        self.negatives()
        self.multiple_operations()
        print(f"\ntests passed: {self.passed}")
        print(f"tests failed: {self.failed}")

    def is_equal(self, actual, expected, name):
        if actual == expected:
            print(f"PASS : {name}")
            self.passed += 1
        else:
            print(f"FAILED : {name} (expected {expected}, instead got {actual})")
            self.failed += 1

    def is_close_enough(self, actual, expected, name, threshold = 1e-7):
        if abs( actual - expected ) < threshold :
            print(f"PASS : {name}")
            self.passed += 1
        else:
            print(f"FAILED : {name} (expected {expected}, instead got {actual})")
            self.failed += 1

    def single_integer(self):
        self.is_equal(self.calculator.calculate("6"), 6, "Test for a solo integer")
        self.is_equal(self.calculator.calculate("0"), 0, "Test for a solo integer")
        self.is_equal(self.calculator.calculate("548511"), 548511, "Test for a solo integer")

    def single_float(self):
        self.is_close_enough(self.calculator.calculate("8.9"), 8.9, "Test for a single float")
        self.is_close_enough(self.calculator.calculate("1.0"), 1, "Test for a single float")
        self.is_close_enough(self.calculator.calculate("3.14"), 3.14, "Test for a single float")

    def addition(self):
        self.is_equal(self.calculator.calculate("1 + 1"), 2, "Test for a single addition")
        self.is_equal(self.calculator.calculate("12 + 12"), 24, "Test for a single addition")
        self.is_equal(self.calculator.calculate("13+12"), 25, "Test for a single addition")
        self.is_equal(self.calculator.calculate("2+ 3"), 5, "Test for a single addition")
        self.is_equal(self.calculator.calculate("8 +3"), 11, "Test for a single addition")

    def multiple_additions(self):
        self.is_equal(self.calculator.calculate("1 + 1 + 1"), 3, "Test for a multiple additions")
        self.is_equal(self.calculator.calculate("12 + 12 + 1"), 25, "Test for a multiple additions")
        self.is_equal(self.calculator.calculate("13+12+11"), 36, "Test for a multiple additions")
        self.is_equal(self.calculator.calculate("2+ 3+ 5"), 10, "Test for a multiple additions")
        self.is_equal(self.calculator.calculate("8 +3+3"), 14, "Test for a multiple additions")

    def subtraction(self):
        self.is_equal(self.calculator.calculate("1 - 1"), 0, "Test for a simple substraction")
        self.is_equal(self.calculator.calculate("8-5"), 3, "Test for a simple substraction")
        self.is_equal(self.calculator.calculate("13-14"), -1, "Test for a simple substraction")
        self.is_equal(self.calculator.calculate("20-10-5"), 5, "Test for a simple substraction")
        self.is_equal(self.calculator.calculate("5 - 0 - 4 - 0 - 3"), -2, "Test for a simple substraction")

    def multiplication(self):
        self.is_equal(self.calculator.calculate("0 * 0"), 0, "Testing with just a simple multiplication")
        self.is_equal(self.calculator.calculate("0 * 1"), 0, "Testing with just a simple multiplication")
        self.is_equal(self.calculator.calculate("1 * 0"), 0, "Testing with just a simple multiplication")
        self.is_equal(self.calculator.calculate("2 * 2"), 4, "Testing with just a simple multiplication")
        self.is_equal(self.calculator.calculate("1*2*3*4"), 24, "Testing with just a simple multiplication")
        self.is_equal(self.calculator.calculate("9 * 0.5"), 4.5, "Testing with just a simple multiplication")

    def parenthesis(self):
        self.is_equal(self.calculator.calculate("0 * (0 + 1)"), 0, "Testing for parenthesis")
        self.is_equal(self.calculator.calculate("(1 + 2) * 2 + 1 "), 7, "Testing for parenthesis")
        self.is_equal(self.calculator.calculate("(1 + 2) * (2 + 1) "), 9, "Testing for parenthesis")
        self.is_equal(self.calculator.calculate("(5 - 5) * 0 - 4 "), -4, "Testing for parenthesis")
        self.is_equal(self.calculator.calculate("(10 - 2) * 10"), 80, "Testing for parenthesis")

    def negatives(self):
        self.is_equal(self.calculator.calculate("-15"), -15, "Test for a single negative number")
        self.is_equal(self.calculator.calculate("-1"), -1, "Test for a single negative number")


    def multiple_operations(self):
        self.is_close_enough(self.calculator.calculate("0 * 0 + 1"), 1, "Testing multiple cases in one expression")
        self.is_close_enough(self.calculator.calculate("1 + 2 * 2 + 1"), 6, "Testing multiple cases in one expression")
        self.is_close_enough(self.calculator.calculate("5 - 5 * 0 - 4"), 1, "Testing multiple cases in one expression")
        self.is_close_enough(self.calculator.calculate("10 - 2 * 10"), -10, "Testing multiple cases in one expression")

# Run the tests

if __name__ == "__main__" :
    CalculatorTest().run()
