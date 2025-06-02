from typing import List


def resolve_input(input_line: str) -> List[int]:
    char_to_remove = list("[]")
    line_no_bracket = "".join((c if c not in char_to_remove else "" for c in input_line))
    chunks = [c for c in line_no_bracket.split(",") if c]
    # print(f"{chunks=}")
    return [int(str.strip(chunk)) for chunk in chunks]


def solve(input_line: str) -> str:
    number_list = resolve_input(input_line)

    if len(number_list) < 2:
        return "input contains less than 2 numbers"
    else:
        sorted_list = sorted(number_list)
        second_largest = sorted_list[-2]
        second_smallest = sorted_list[1]
        sum_ans = second_largest + second_smallest
        return f"{sum_ans} ({second_smallest} + {second_largest})"


def main():
    input_line = input()
    ans = solve(input_line)
    print(ans)


if __name__ == '__main__':
    main()
