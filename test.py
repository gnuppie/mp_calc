# class Stack:
#     def __init__(self):
#         self.__items = []  # name mangling
#
#     def push(self, item):
#         self.__items.append(item)
#
#     def pop(self):
#         if len(self.__items) >= 1:
#             return self.__items.pop()
#
#     def peek(self):
#         if len(self.__items) >= 1:
#             return self.__items[-1]  # return element in last index
#         # does not remove the last element from list of items
#
#     @property
#     def is_empty(self):
#         return len(self.__items) == 0
#
#     @property
#     def size(self):
#         return len(self.__items)
#
#
# class EvaluateExpression:
#
#     def __init__(self, string=""):
#         self.expression = string
#
#     @property
#     def expression(self):
#         return self._expression
#
#     @expression.setter
#     def expression(self, new_expr):
#         valid_char = '0123456789+-*/() '
#         for char in new_expr:
#             if char not in valid_char:
#                 self._expression = ""
#                 return
#
#         self._expression = new_expr
#
#     def insert_space(self):
#         new_expr = ""
#         for char in self.expression:
#             if char in "+-*/()":
#                 new_expr += " " + char + " "
#             else:
#                 new_expr += char
#         return new_expr
#
#     def process_operator(self, operand_stack, operator_stack):
#         if operand_stack.size < 2:
#             pass
#         else:
#             operator = operator_stack.pop()
#             op2 = int(operand_stack.pop())
#             op1 = int(operand_stack.pop())
#
#             if operator == "+":
#                 operand_stack.push(op1 + op2)
#             elif operator == "-":
#                 operand_stack.push(op1 - op2)
#             elif operator == "*":
#                 operand_stack.push(op1 * op2)
#             elif operator == "/":
#                 operand_stack.push(op1 // op2)
#
#             return operand_stack.peek()
#
#     def evaluate(self):
#         operand_stack = Stack()
#         operator_stack = Stack()
#         expression = self.insert_space()
#         tokens = expression.split()
#         print(tokens)
#
#         for char in tokens:
#             if char.isnumeric():
#                 operand_stack.push(char)
#
#             elif char == "+" or char == "-":
#
#                 while (not operator_stack.is_empty) and (operator_stack.peek() not in "()"):
#                     self.process_operator(operand_stack, operator_stack)
#                 operator_stack.push(char)
#
#             elif char == "*" or char == "/":
#                 extracted_operators = []
#                 while not operator_stack.is_empty:
#                     op = operator_stack.peek()
#                     if op != "*" or op != "/":
#                         extracted_operators.append(operator_stack.pop())
#                     else:
#                         self.process_operator(operand_stack, operator_stack)
#                 while len(extracted_operators) > 0:
#                     operator_stack.push(extracted_operators.pop())
#
#                 operator_stack.push(char)
#
#             elif char == "(":
#                 operator_stack.push(char)
#
#             elif char == ")":
#                 while operator_stack.peek() != "(" and not operator_stack.is_empty:
#                     self.process_operator(operand_stack, operator_stack)
#                 # remove the ()
#                 operator_stack.pop()
#
#
#         while operand_stack.size != 1:
#             self.process_operator(operand_stack, operator_stack)
#
#
#         return operand_stack.pop()
#
#
# expr1 = EvaluateExpression("(1 + 2) * 4 - 3")
# print(expr1.evaluate())