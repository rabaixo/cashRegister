"""Test Module"""
# Python packages
import pytest

# package
from cashRegister import checkout, pricing_rules
from test import parameters_to_test as pt
from cashRegister import checkout, pricing_rules


@pytest.mark.parametrize(
    "items, total_expected_cost",
    pt.parameters_to_test_list
)
def test_price_rules(items, total_expected_cost):
    """Test the behavior of price rules

    Args:
        items (list): list of products code
        total_expected (double): total cost
    """
    checkout_obj = checkout.Checkout(pricing_rules.pricing_rules)
    for item in items:
        package_results = checkout_obj.scan(item)
    assert items == package_results["items"] and package_results["total"] == total_expected_cost


@pytest.mark.parametrize(
    "item",
    pt.parameters_to_test_error_list
)
def test_warning(item):
    """Test the behavior of price rules

    Args:
        items (list): list of products code
        total_expected (double): total cost
    """
    checkout_obj = checkout.Checkout(pricing_rules.pricing_rules)
    package_results = checkout_obj.scan(item)
    assert "error" in package_results


