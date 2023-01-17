# Define product discounts
pricing_rules = {
    # A 2-for-1 special on VOUCHER items.
    "VOUCHER": lambda product: (((product.SIZE / 2) - product.SIZE % 2) * product.PRICE) + (product.SIZE % 2 * product.PRICE),
    # If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.
    "TSHIRT": lambda product: (product.SIZE * (product.PRICE - 1)) if product.SIZE >= 3 else (product.SIZE * product.PRICE)
}