import os

from examples.bore_field_thermal_resistance import main as bftr_main
from examples.comparison_gfunction_solvers import main as cgs_main
from examples.comparison_load_aggregation import main as cla_main

import unittest

class TestExamples(unittest.TestCase):

    def test_bftr_main(self):
        bftr_main(make_plots=False)

    def test_cgs_main(self):
        cgs_main(make_plots=False)

    @unittest.skipIf("CI" not in os.environ, "Long running test that only runs on CI. Skipping.")
    def test_cla_Main(self):
        cla_main(make_plots=False)
