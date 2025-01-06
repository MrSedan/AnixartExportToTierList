import csv
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
from typing import List

import numpy as np
from tqdm import tqdm

from anixarttierlist import (add_url_to_file, download_image, get_image_url,
                             prepare)


class TableColumns(Enum):
    ID = 0
    RUS_NAME = 1
    JAP_NAME = 2
    ALT_NAME = 3


def get_urls(names: List[List[str]]) -> List[str]:
    for group in tqdm(names):
        for name in tqdm(group):
            url = get_image_url(name)
            if url != '':
                add_url_to_file(url)
                download_image(url, name)
            time.sleep(0.68)  # Time to not get banned on shikimori API


def download_imgs(urls: List[str]):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, urls)


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
    np_anime_list = np.array(anime_list_before_group)
    res = np.array_split(np_anime_list, np.ceil(len(np_anime_list) / 5))
    get_urls(res)


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        print('Error! Run program with file name: \'python main.py file.csv\'')
        sys.exit(1)
    prepare()
    sys.exit(main(argv[1]))
