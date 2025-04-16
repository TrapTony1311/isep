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
        self.addition_floats()
        self.subtraction()
        self.subtraction_negative_result()
        self.multiplication()
        self.multiplication_floats()
        self.multiple_operations()
        self.operation_precedence()
        self.parenthesus()
        self.nested_parenthesis()
        self.negatives()
        self.negatives_parentheses()
        self.complex_expression()
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
        self.is_equal(self.calculator.calculate("42"), 42, "Test for a solo integer")

    def single_float(self):
        self.is_close_enough(self.calculator.calculate("3.14"), 3.14, "Test for a single float")

    def addition(self):
        self.is_equal(self.calculator.calculate(" 2 + 3"), 5, "Test for a single addition")

    def addition_floats(self):
        self.is_close_enough(self.calculator.calculate("2.5 + 3.1"), 5.6, "Test for a single addition with floats")

    def subtraction(self):
        self.is_equal(self.calculator.calculate("7 - 4"), 3, "Test for a simple substraction")

    def subtraction_negative_result(self):
        self.is_equal(self.calculator.calculate("2 - 5"), -3, "Test for a substraction that has a negative result")

    def multiplication(self):
        self.is_equal(self.calculator.calculate("3 * 4"), 12, "Testing with just a simple multiplication")

    def multiplication_floats(self):
        self.is_close_enough(self.calculator.calculate("2.5 * 4"), 10.0, "Test for a multiplication with a float in it")

    def multiple_operations(self):
        self.is_equal(self.calculator.calculate("2 + 3 * 4"), 14, "Test for an addition before a multiplication for operation precedence")

    def operation_precedence(self):
        self.is_equal(self.calculator.calculate("2 + 3 * 4 - 5"), 9, "More tests for operation precedence with different operations")

    def parenthesis(self):
        self.is_equal(self.calculator.calculate("(2 + 3) * 4 "), 20, "Testing for parenthesis and precedence using a multiplication")

    def nested_paretnhesis(self):
        self.is_equal(self.calculator.calculate("2 * (3 + (4 - 1)) "), 12, "Testnig parenthesis in parenthesis")

    def negatives(self):
        self.is_equal(self.calculator.calculate("-3 + 7"), 4, "Test for a negative number in an addition")

    def negatives_parentheses(self):
        self.is_equal(self.calculator.calculate("2 * (-3 + 5)"), 4, "Test for a negative number inside a paretnhesis")

    def complex_expression(self):
        self.is_close_enough(self.calculator.calculate("3.5 + 2 * (4 - 1.5)"), 8.5, "Testing multiple cases in one expression")

# Run the tests

if __name__ == "__main__" :
    CalculatorTest().run()
