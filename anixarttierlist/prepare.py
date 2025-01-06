import os


def prepare():
    if not os.path.exists('./temp'):
        os.mkdir('./temp')
