# -*- coding: utf-8 -*-

import os
import scipy as sp

from analize import Analize

DIRNAME = os.path.dirname(os.path.abspath(__file__)) + "/data"


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

    def get_approx_func(self, x, y, dim=1):
        """
        データ(x, y)の近似関数を算出する。
            x: fと比較するデータの1カラム目
            y: fと比較するデータの2カラム目
        """

        fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, dim, full=True)

        return sp.poly1d(fp1)


if __name__ == '__main__':

    """
    color memo:
    b: blue
    g: green
    r: red
    c: cyan
    m: magenta
    y: yellow
    k: black
    w: white
    """

    analize = Analize()
    (x, y) = analize.get_data_from_csv(DIRNAME + "/web_traffic.tsv", delimiter="\t")

    model = Model()
    f = model.get_approx_func(x, y, dim=1)
    g = model.get_approx_func(x, y, dim=2)
    h = model.get_approx_func(x, y, dim=10)

    funcs = [
        {'func': f, 'color': "r", 'legend': "f dim: 1"},
        {'func': g, 'color': "g", 'legend': "g dim: 2"},
        {'func': h, 'color': "y", 'legend': "h dim: 10"},

    ]

    analize.show_graph(x, y, funcs)
