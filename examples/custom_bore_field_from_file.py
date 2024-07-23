# -*- coding: utf-8 -*-
""" Example of definition of a bore field using custom borehole positions.

"""

from pathlib import Path

import pygfunction as gt


def main(make_plots=True):
    # -------------------------------------------------------------------------
    # Parameters
    # -------------------------------------------------------------------------

    # Filepath to bore field text file
    filename = Path(__file__).parent / "data" / "custom_field_32_boreholes.txt"

    # -------------------------------------------------------------------------
    # Borehole field
    # -------------------------------------------------------------------------

    # Build list of boreholes
    field = gt.boreholes.field_from_file(filename)

    if make_plots:
        # -------------------------------------------------------------------------
        # Draw bore field
        # -------------------------------------------------------------------------

        gt.boreholes.visualize_field(field)


# Main function
if __name__ == '__main__':
    main()
