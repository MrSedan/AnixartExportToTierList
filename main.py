import csv
import sys
from enum import Enum
from typing import List

from anixarttierlist import group_by_common_part


class TableColumns(Enum):
    ID = 0
    RUS_NAME = 1
    JAP_NAME = 2
    ALT_NAME = 3


def main(file: str):
    anime_list_before_group: List[str] = []
    with open(file, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(spamreader):
            if i == 0:
                continue
            if row[TableColumns.JAP_NAME.value] != '':
                anime_list_before_group.append(
                    row[TableColumns.JAP_NAME.value])
    # anime_list: List[str] = group_by_common_part(anime_list_before_group) # TODO: find the best algorithm for that
    print(anime_list_before_group)


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        print('Error! Run program with file name: \'python main.py file.csv\'')
        sys.exit(1)
    sys.exit(main(argv[1]))
