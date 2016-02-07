# -*- coding: utf-8 -*-

import os
import scipy as sp

from analize import Analize

DIRNAME = os.path.dirname(os.path.abspath(__file__))


class Model(object):

    def error(self, f, x, y):
        """
        求める関数の誤差を求める

        usage:
            f: 誤差を求める関数
            x: fと比較するデータの1カラム目
            y: fと比較するデータの2カラム目
        """
        return sp.sum(f(x) - y ** 2)

    def get_1d_approx_func(self, x, y, dim=1):
        """
        データ(x, y)の近似関数を算出する。
            x: fと比較するデータの1カラム目
            y: fと比較するデータの2カラム目
        """

        fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, dim, full=True)

        return sp.poly1d(fp1)


if __name__ == '__main__':

    analize = Analize()
    (x, y) = analize.get_data_from_csv(DIRNAME + "/cpu.csv")

    model = Model()
    f = model.get_1d_approx_func(x, y)

    analize.show_graph(x, y, f)
