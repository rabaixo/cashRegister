# Define product discounts
pricing_rules = {
    # A 2-for-1 special on VOUCHER items.
    "VOUCHER": lambda product: (((product.size / 2) - product.size % 2) * product.price) + (product.size % 2 * product.price),
    # If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.
    "TSHIRT": lambda product: (product.size * (product.price - 1)) if product.size >= 3 else (product.size * product.price)
}