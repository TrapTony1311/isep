#################################################
# Calculator code for clean code class
# Class : Software Engineering II.2405
# Author : Anthony Nora
# Date : 16/04/2025
#################################################

class Calculator:

    def calculate(self, expression):

        # Clean the input first to understand the string as mathematical operation
        tokens = self._tokenize(expression)

        # Handling the operation precedence by using a classic algorithm used called the Shunting Yard algorithm
        postfix = self._convert_to_postfix(tokens)

        # Apply the operations and return the result
        return self._evaluate_postfix(postfix)


    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue

            if char.isdigit() or char == ".":
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == "."):
                    j += 1
                number = expression[i:j]
                tokens.append(float(number) if "." in number else int(number))
                i = j

            elif char == "-" and (i == 0 or self._is_operator_or_parenthesis(tokens)):
                tokens.append("neg")
                i += 1

            elif char in "+-*/()":
                tokens.append(char)
                i += 1
            else:
                raise ValueError(f"Invalid character: {char}")
        return tokens

    def _is_operator_or_parenthesis(self, tokens):
        return not tokens or isinstance(tokens[-1], str) and tokens[-1] in "+-*/("

    def _convert_to_postfix(self, tokens):
        output = []
        associativity = {"neg": "right", "*": "left", "/": "left", "+": "left", "-": "left"}
        stack = []        
        precedence = {"neg": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        

        for token in tokens:
            if isinstance(token, (int, float)):
                output.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()  # Remove '('
            else:
                while stack and stack[-1] != "(" and self._should_pop_operator(stack, token, precedence, associativity):
                    output.append(stack.pop())
                stack.append(token)
        
        while stack:
            output.append(stack.pop())
        
        return output

    def _should_pop_operator(self, stack, current_op, precedence, associativity):
        stack_op = stack[-1]
        return (precedence[stack_op] > precedence[current_op]) or \
               (precedence[stack_op] == precedence[current_op] and associativity[current_op] == "left")

    def _evaluate_postfix(self, postfix):
        stack = []
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token == "neg":
                stack.append(-stack.pop())
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(self._apply_operation(left, right, token))
        return stack[0]

    def _apply_operation(self, left, right, operator):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b
        }
        return operations[operator](left, right)
