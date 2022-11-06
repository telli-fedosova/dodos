import datetime

from dodos import output
from dodos.types import Dodo


def test_output():
    dodos = [
        Dodo("Write output.to_string implementation", datetime.date(2022, 6, 6)),
        Dodo("Create more dodos", datetime.date(2022, 6, 7)),
    ]

    expected = (
        "|                Summary                |    Date    |\n"
        "| Write output.to_string implementation | 2022-06-06 |\n"
        "| Create more dodos                     | 2022-06-07 |  \n"
    )

    actual = output.get_table(dodos)

    assert expected == actual
