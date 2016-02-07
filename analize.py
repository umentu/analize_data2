# -*- coding; utf-8 -*-

import os

import matplotlib.pyplot as plt
import scipy as sp

DIRNAME = os.path.dirname(os.path.abspath(__file__))


class Analize(object):
    """
    usage:
        xlabel: グラフのx軸のラベル
        ylabel: グラフのy軸のラベル
    """


    def __init__(self,
                 xlabel="time",
                 ylabel="data"):

        self.xlabel = xlabel
        self.ylabel = ylabel

    def get_data_from_csv(self, 
                          file_path,
                          delimiter="\t"):
        """
        CSVファイルからデータを抽出する。
        usage:
            file_path: ファイルのパス
            delimiter: csvファイルの区切り文字（デフォルト: tab）
        """

        d = sp.genfromtxt(file_path, delimiter=delimiter)
        x = d[:, 0]
        y = d[:, 1]

        return (x, y)

    def show_graph(self,
                   x,
                   y,
                   f=None,
                   ):
        """
        data_source(delimiterで区切った2列のデータ)を
        プロットしてグラフとして表示する。

        usage: 
            x: fと比較するデータの1カラム目
            y: fと比較するデータの2カラム目
            f: 描画する関数
        """
        plt.scatter(x, y)

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.autoscale(tight=True)

        if f is not None:

            fx = sp.linspace(0, x[-1], 1000)
            plt.plot(fx, f(fx), "r", linewidth=6)

        plt.show()


if __name__ == '__main__':

    analize = Analize()
    (x, y) = analize.get_data_from_csv(DIRNAME + "/number_data.txt")
    analize.show_graph(x, y)
