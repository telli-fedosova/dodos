from typing import List
from dodos.types import Dodo


def get_table(dodos: List[Dodo]) -> str:
    sum_max_length = max(len(d.summary) for d in dodos)

    lines = [f"| Summary {' ' * (sum_max_length - len('Summary'))}| Date       |"]
    for d in dodos:
        padding_length = sum_max_length - len(d.summary)
        lines.append(f"| {d.summary} {' ' * padding_length}| {d.date} |")

    return "\n".join(lines) + "\n"
