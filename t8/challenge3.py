from collections import deque
from typing import List, Tuple

DEQUEUE_TIMES = 2


def sanitize(item_raw_text: str) -> str:
    return item_raw_text.strip().lstrip("[").rstrip("]").strip().strip("\'")


def translate_input(input_line: str) -> Tuple[List[str], str]:
    no_bracket = input_line.strip().lstrip("[").rstrip("]")
    split_result = no_bracket.split(",")
    last_item = sanitize(split_result[-1])
    print(f"{no_bracket=}")
    print(f"{split_result=}")
    items_in_queue = [sanitize(item) for item in split_result[:-1]]

    return items_in_queue, last_item


def dequeue_and_insert(a_queue, new_item):
    # dequeue N times
    for _ in range(DEQUEUE_TIMES):
        if a_queue:
            a_queue.popleft()

    a_queue.append(new_item)


def construct_ans(a_queue):
    middle_text = ", ".join(a_queue)
    return f"[\"{middle_text}\"]"


def solve(input_line: str) -> str:
    items_in_queue, new_item = translate_input(input_line)

    a_queue = deque(items_in_queue)
    dequeue_and_insert(a_queue, new_item)

    return construct_ans(a_queue)


def main():
    input_line = input()
    ans = solve(input_line)
    print(ans)


# [['Apple', 'Banana', 'Cherry'], 'Tomato']
if __name__ == '__main__':
    main()
