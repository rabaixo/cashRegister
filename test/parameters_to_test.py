parameters_to_test_list=[
    (["VOUCHER"], 5),
    (["VOUCHER", "VOUCHER"], 5.00),
    (["TSHIRT", "TSHIRT"], 40.00),
    (["PANTS"], 7.50),
    (["PANTS", "PANTS"], 15.00),
    (["TSHIRT", "TSHIRT", "TSHIRT"], 57.00),
    (["VOUCHER", "TSHIRT", "PANTS"], 32.5),
    (["VOUCHER", "TSHIRT", "VOUCHER"], 25.00),
    (["TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], 81.00),
    (["VOUCHER", "TSHIRT", "VOUCHER", "VOUCHER", "PANTS", "TSHIRT", "TSHIRT"], 74.5)
]

parameters_to_test_error_list = [
    ("LILLE"),
    ("SMALL")
]