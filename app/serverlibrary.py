
def mergesort(array, byfunc=None):
  if byfunc == None:
    mergesort_recursive(array, 0, len(array) - 1, None)
  else:
    mergesort_recursive(array, 0, len(array) - 1, byfunc)

def mergesort_recursive(array, p, r, byfunc):
  print(f"MergeSort Start {p} End {r}")
  start, end = p, r
  n = end - start + 1
  if n > 1:
    middle = int((start + end )/ 2)
    mergesort_recursive(array, start, middle, byfunc)
    mergesort_recursive(array, middle + 1, end, byfunc)
    merge(array, start, middle, end, byfunc)

def merge(array, p, q, r, byfunc):
  start, middle, end = p, q, r
  Aleft_none = array[start:middle +1]

  Aright_none = array[middle +1:end +1]
  if byfunc != None:
    Aleft = [byfunc(n) for n in Aleft_none]
    Aright = [byfunc(n) for n in Aright_none]
  else:
    Aleft = Aleft_none
    Aright= Aright_none

  nleft = len(Aleft)
  nright = len(Aright)

  print(Aleft, Aright)

  left, right, dest = 0, 0, start
  print(left, right, dest)

  while left < nleft and right < nright:
    if Aleft[left] <= Aright[right]:
      array[dest] = Aleft_none[left]
      left += 1
    else:
      array[dest] = Aright_none[right]
      right += 1

    dest += 1

  print(array)

  while left < nleft:
    array[dest] = Aleft_none[left]
    left += 1
    dest += 1

  while right < nright:
    array[dest] = Aright_none[right]
    right += 1
    dest += 1

  print("Final outcome", array)


class Stack:
  def __init__(self):
    self.__items = []  # name mangling

  def push(self, item):
    self.__items.append(item)

  def pop(self):
    if len(self.__items) >= 1:
      return self.__items.pop()

  def peek(self):
    if len(self.__items) >= 1:
      return self.__items[-1]  # return element in last index
    # does not remove the last element from list of items

  @property
  def is_empty(self):
    return len(self.__items) == 0

  @property
  def size(self):
    return len(self.__items)


class EvaluateExpression:

  def __init__(self, string=""):
    self.expression = string

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    valid_char = '0123456789+-*/() '
    for char in new_expr:
      if char not in valid_char:
        self._expression = ""
        return

    self._expression = new_expr

  def insert_space(self):
    new_expr = ""
    for char in self.expression:
      if char in "+-*/()":
        new_expr += " " + char + " "
      else:
        new_expr += char
    return new_expr

  def process_operator(self, operand_stack, operator_stack):
    if operand_stack.size < 2:
      pass
    else:
      operator = operator_stack.pop()
      op2 = int(operand_stack.pop())
      op1 = int(operand_stack.pop())

      if operator == "+":
        operand_stack.push(op1 + op2)
      elif operator == "-":
        operand_stack.push(op1 - op2)
      elif operator == "*":
        operand_stack.push(op1 * op2)
      elif operator == "/":
        operand_stack.push(op1 // op2)

      return operand_stack.peek()

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    #         print(tokens)

    for char in tokens:
      if char.isnumeric():
        operand_stack.push(char)

      elif char == "+" or char == "-":
        #                 print("+-")
        while (not operator_stack.is_empty) and (operator_stack.peek() not in "()"):
          #                     print(operator_stack.peek())
          self.process_operator(operand_stack, operator_stack)

        operator_stack.push(char)

      elif char in "*/":
        #                 print("*/")
        extracted_operators = []
        while (not operator_stack.is_empty) and (operator_stack.peek() != "("):
          #                     print(operator_stack.size)
          op = operator_stack.peek()
          if op not in "*/":
            extracted_operators.append(operator_stack.pop())
          else:
            self.process_operator(operand_stack, operator_stack)
        #                         print(operand_stack.peek())

        while len(extracted_operators) > 0:
          operator_stack.push(extracted_operators.pop())

        operator_stack.push(char)

      elif char == "(":
        operator_stack.push(char)

      elif char == ")":
        #                 print(")")
        while operator_stack.peek() != "(" and not operator_stack.is_empty:
          self.process_operator(operand_stack, operator_stack)
          #                     print(operand_stack.peek())
          #                     print(operator_stack.peek())

          # REMOVE THAT "(" AT THE START TO PUT OPERATIONS BETWEEN THE PRODUCTS OF TWO PARENTHESIS
          operator_stack.pop()

    #                     print(operator_stack.peek())

    while operand_stack.size != 1:
      self.process_operator(operand_stack, operator_stack)

    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





