"""
@brief      test log(time=28s)
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
    import pymyinstall as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_
    import pymyinstall as skip__

from pyquickhelper.loghelper import fLOG
from src.pyensae.datasource.data_velib import DataVelibCollect


class TestDataVelibSimulation (unittest.TestCase):

    def test_data_velib_simulation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")
        fold = os.path.abspath(os.path.split(__file__)[0])
        data = os.path.join(fold, "data")

        for speed in (10, 15):
            for bike in (1, 2, 3, 5, 10):
                df = DataVelibCollect.to_df(data)
                dfp, dfs = DataVelibCollect.simulate(
                    df, bike, speed, fLOG=fLOG)

                dfp.to_csv(
                    "out_simul_bike_nb{0}_sp{1}_path.txt".format(
                        bike,
                        speed),
                    sep="\t",
                    index=False)
                dfs.to_csv(
                    "out_simul_bike_nb{0}_sp{1}_data.txt".format(
                        bike,
                        speed),
                    sep="\t",
                    index=False)
                if __name__ != "__main__":
                    return


if __name__ == "__main__":
    unittest.main()
