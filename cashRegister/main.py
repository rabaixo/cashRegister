# python packages
import argparse
import sys
import pkg_resources

# package modules
from . import pricing_rules as pr
from . import checkout as co


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
    products_list = args.products_list
    version = args.version


    if version:
        try:
            package_info = pkg_resources.get_distribution("cashRegister")
        except pkg_resources.DistributionNotFound:
            sys.exit(1)
        print(package_info.version)
        sys.exit(0)

    if args.products_list is None:
        sys.exit("No items to scan.")


    checkout_obj = co.Checkout(pr.pricing_rules)
    for product in products_list:
        items = checkout_obj.scan(product)
        if "error" in items:
            print(f'Error: {items["error"]}')
        elif "error" in items:
            print('Warning: {items["warning"]}')
        else:
            print("Items: "+", ".join(items["items"])+ f" - Total:{items['total']}")


if __name__ == "__main__":
    main()