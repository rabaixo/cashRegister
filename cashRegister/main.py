# python packages
import argparse
import logging as log
import sys
import pickle
import pkg_resources
import os

# package modules



# parse_args ------------------------------------------------------------------
def parse_args():
    """Argument parser function (see argparse_):

    .. _argparse: http://newcoder.io/api/part-4/
    """

    # general parser and info
    parser = argparse.ArgumentParser(
        prog="scan_clothes",
        description="Scan multiple pieces of clothing",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--products_list",
        nargs="+",
        default=None,
        help="The list of  the clothes to scan.",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="package version.",
        required=False,
    )

    args = parser.parse_args()

    return args


# --------------------------------------------------------------------------- #


# main ------------------------------------------------------------------------
def main():
    """Read data using argparse_ package and execute the
    :func:`scengenref.scengenref.scengenref`.

    .. _argparse: http://newcoder.io/api/part-4/
    """
    # =========================================================================
    # Load input
    # -------------------------------------------------------------------------
    args = parse_args()
    products_file = args.products_list
    version = args.version


    if version:
        try:
            package_info = pkg_resources.get_distribution("cashRegister")
        except pkg_resources.DistributionNotFound:
            sys.exit(1)
        print(package_info.version)
        sys.exit(0)

    if args.products_file is None:
        sys.exit("No items to scan.")





if __name__ == "__main__":
    main()