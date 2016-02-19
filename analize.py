# -*- coding; utf-8 -*-

import os

import matplotlib.pyplot as plt
import scipy as sp

DIRNAME = os.path.dirname(os.path.abspath(__file__)) + "/data"


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
                          delimiter=","):
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
                   funcs=[],
                   ):
        """
        data_source(delimiterで区切った2列のデータ)を
        プロットしてグラフとして表示する。

        usage: 
            x: fと比較するデータの1カラム目
            y: fと比較するデータの2カラム目
            funcs: 描画する関数と関数の情報をdictのタプルで指定する
                example:
                    funcs = (
                        {
                            'func': f,
                            'color': "r",
                            'legend': "f: {0} d".format(1)
                        },
                        {
                            'func': g,
                            'color': "g",
                            'legend': "g: {0} d".format(2)
                        },
                    )

        """
        plt.scatter(x, y)

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.autoscale(tight=True)

        if funcs is not None:

            legends = []

            for func in funcs:
                f = func['func']
                c = func['color']
                l = func['legend']

                fx = sp.linspace(0, x[-1], 1000)
                plt.plot(fx, f(fx), c, linewidth=6)
                legends.append(l)

            plt.legend([leg for leg in legends], loc="upper left")

        plt.show()


if __name__ == '__main__':

    analize = Analize()
    (x, y) = analize.get_data_from_csv(DIRNAME + "/web_traffic.tsv", delimiter="\t")
    analize.show_graph(x, y)
