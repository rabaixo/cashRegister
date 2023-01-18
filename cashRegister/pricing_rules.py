# Define product discounts
pricing_rules = {
    # A 2-for-1 special on VOUCHER items.
    "VOUCHER": lambda product: (int(product.ITEMS / 2) * product.PRICE) + (product.ITEMS % 2 * product.PRICE),
    # If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.
    "TSHIRT": lambda product: (product.ITEMS * (product.PRICE - 1)) if product.ITEMS >= 3 else (product.ITEMS * product.PRICE)
}