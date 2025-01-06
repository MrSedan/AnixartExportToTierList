import csv
from enum import Enum
from typing import List

from anixarttierlist import group_by_common_part


class TableColumns(Enum):
    ID = 0
    RUS_NAME = 1
    JAP_NAME = 2
    ALT_NAME = 3


def main():
    anime_list: List[str] = []
    with open('./aboba.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            name: str = row[TableColumns.JAP_NAME.value]


if __name__ == '__main__':
    main()
