"""Test Module"""
# Python packages
import pytest

# package
from cashRegister import checkout, pricing_rules
from test import parameters_to_test as pt
from cashRegister import checkout, pricing_rules


@pytest.mark.parametrize(
    "items, total_expected_cost",
    pt.parameters_list_to_test
)
def test_price_rules(items, total_expected_cost):
    """Test the behavior of price rules

    Args:
        items (list): list of the products codes
        total_expected_cost (double): total expected cost
    """
    checkout_obj = checkout.Checkout(pricing_rules.pricing_rules)
    for item in items:
        package_results = checkout_obj.scan(item)
    assert items == package_results["items"] and package_results["total"] == total_expected_cost


@pytest.mark.parametrize(
    "item",
    pt.parameters_list_to_test_error
)
def test_error(item):
    """ An error should be returned when trying to scan an element
        with non-existent code in the database

    Args:
        item (str): code of product to scan
    """
    checkout_obj = checkout.Checkout(pricing_rules.pricing_rules)
    package_results = checkout_obj.scan(item)
    assert "error" in package_results


@pytest.mark.parametrize(
    "items, item_to_remove, item_list_updated, total_expected_cost",
    pt.parameters_list_to_test_remove
)
def test_remove_element(items, item_to_remove, item_list_updated, total_expected_cost):
    """ The list and the value of the total cost must be updated
        when a product is deleted from the list of items
    Args:
        items (list): list of the products codes
        item_to_remove (str): item to remove
        item_list_updated (list): updated list of the products codes
        total_expected_cost (double): total expected cost
    """
    checkout_obj = checkout.Checkout(pricing_rules.pricing_rules)
    for item in items:
        checkout_obj.scan(item)
    package_results = checkout_obj.remove(item_to_remove)
    assert item_list_updated == package_results["items"] and package_results["total"] == total_expected_cost



@pytest.mark.parametrize(
    "item_to_scan, item_to_remove",
    pt.parameters_list_to_test_warning
)
def test_warning(item_to_scan, item_to_remove):
    """ A warning should be returned when trying
        to delete an unregistered element (for Django web app)

    Args:
        item_to_scan (list): list of the products codes to scan
        item_to_remove (str): item to remove
    """
    checkout_obj = checkout.Checkout(pricing_rules.pricing_rules)
    for item in item_to_scan:
        checkout_obj.scan(item)
    package_results = checkout_obj.remove(item_to_remove)
    assert "warning" in package_results

