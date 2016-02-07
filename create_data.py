# -*- coding: utf-8 -*-

import random
import os
import numpy as np


class CreateData(object):

    """
    create data to analyze.
    """

    def create_number_data(self,
                           file_path,
                           count,
                           min_int=0,
                           max_int=10000):

        with open(file_path, "w") as f:
            for n in range(count):
                f.write(str(n) + "\t" +
                        str(random.randint(min_int, max_int) + (n * 6)) + "\n")

    def create_line_data(self,
                         file_path,
                         count):

        with open(file_path, "w") as f:
            for n in range(count):
                f.write(str(n)
                        + "\t"
                        + str(n * n + random.randint(0, 100000))
                        + "\n")


if __name__ == '__main__':

    create_data = CreateData()
    create_data.create_number_data(
        os.path.dirname(os.path.abspath(__file__))
        + "/number_data.txt",
        count=1000,
        min_int=1000,
        max_int=3000
    )
