from typing import List

AND = "AND"
OR = "OR"
OPERATIONS = [AND, OR]


def operate(op: str, a: int, b: int) -> int:
    if op == AND:
        return a and b
    elif op == OR:
        return a or b
    else:
        raise ValueError(f"Operation {op} is not supported.")


def char_to_01(c: str) -> int:
    """
        A = 1
        B = 0
        C = 1
        ..
    """
    return (ord(c[0]) - ord('A') + 1) % 2


def tokenize(input_line: str) -> List[str]:
    upper_line = input_line.upper()
    char_to_add_space = list("()")
    line_more_space = "".join((c if c not in char_to_add_space else f" {c} " for c in upper_line))
    words = line_more_space.split()

    return [str.strip(word) for word in words]


def aggregate_operand_with_last_2(stack, operand):
    last_op = stack.pop()
    last_val = stack.pop()
    result = operate(last_op, last_val, operand)
    stack.append(result)


def solve(input_line: str) -> int:
    tokens = tokenize(input_line)

    stack = []

    for token in tokens:
        # print("----")
        # print(f"cur token: {token}")
        # print(f"start stack: {stack}")
        if token == "(" or token in OPERATIONS:
            stack.append(token)
        elif token == ")":
            last_val = stack.pop()
            stack.pop()  # pop (
            if not stack or stack[-1] == "(":
                stack.append(last_val)
            else:
                # in case there is a summation value before (
                aggregate_operand_with_last_2(stack, last_val)
        elif len(token) == 1:  # operand
            cur_operand = char_to_01(token)
            if not stack:
                stack.append(cur_operand)
            elif stack[-1] in OPERATIONS:
                aggregate_operand_with_last_2(stack, cur_operand)
            elif stack[-1] == "(":
                stack.append(cur_operand)
            else:
                raise ValueError(f"Unexpected token {token}, current stack is {stack}, input = {input_line}")

        # print(f"end stack: {stack}")
        # print("----")
    if len(stack) != 1:
        raise ValueError(f"Wrong, end result stack len should be 1")

    return stack[0]


def main():
    input_line = input()
    ans = solve(input_line)
    print(ans)


if __name__ == '__main__':
    main()
