import os
import unittest

from examples.bore_field_thermal_resistance import main as bftr_main
from examples.comparison_gfunction_solvers import main as cgs_main
from examples.comparison_load_aggregation import main as cla_main
from examples.custom_bore_field import main as cbf_main
from examples.custom_bore_field_from_file import main as cbff_main
from examples.custom_borehole import main as cb_main
from examples.equal_inlet_temperature import main as eit_main
from examples.fluid_temperature import main as ft_main
from examples.fluid_temperature_multiple_boreholes import main as ftmb_main
from examples.inclined_boreholes import main as ib_main
from examples.load_aggregation import main as la_main
from examples.mixed_inlet_conditions import main as mic_main
from examples.multiple_independent_Utubes import main as miu_main
from examples.multipole_temperature import main as mt_main
from examples.regular_bore_field import main as rbf_main
from examples.unequal_segments import main as us_main
from examples.uniform_heat_extraction_rate import main as uher_main
from examples.uniform_temperature import main as ut_main


class TestExamples(unittest.TestCase):

    def test_bore_field_thermal_resistance_example(self):
        bftr_main(make_plots=False)

    def test_comparison_gfunction_solvers_example(self):
        cgs_main(make_plots=False)

    @unittest.skipIf("CI" not in os.environ, "long running test - only runs on CI")
    def test_comparison_load_aggregation_example(self):
        cla_main(make_plots=False)

    def test_custom_bore_field_example(self):
        cbf_main(make_plots=False)

    def test_custom_bore_field_from_file_example(self):
        cbff_main(make_plots=False)

    def test_custom_borehole_example(self):
        cb_main(make_plots=False)

    def test_equal_inlet_temperature_example(self):
        eit_main(make_plots=False)

    def test_fluid_temperature_example(self):
        ft_main(make_plots=False)

    def test_fluid_temperature_multiple_boreholes_example(self):
        ftmb_main(make_plots=False)

    def test_inclined_boreholes_example(self):
        ib_main(make_plots=False)

    def test_load_aggregation_example(self):
        la_main(make_plots=False)

    def test_mixed_inlet_conditions_example(self):
        mic_main(make_plots=False)

    def test_multiple_independent_Utubes_example(self):
        miu_main(make_plots=False)

    def test_multipole_temperature_example(self):
        mt_main(make_plots=False)

    def test_regular_bore_field_example(self):
        rbf_main(make_plots=False)

    def test_unequal_segments_example(self):
        us_main(make_plots=False)

    def test_uniform_heat_extraction_rate_example(self):
        uher_main(make_plots=False)

    def test_uniform_temperature_example(self):
        ut_main(make_plots=False)
