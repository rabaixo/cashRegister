parameters_list_to_test = [
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

parameters_list_to_test_error = [
    ("LILLE"),
    ("SMALL")
]

parameters_list_to_test_remove = [
    (["VOUCHER", "TSHIRT", "VOUCHER", "VOUCHER", "PANTS", "TSHIRT", "TSHIRT"] , "VOUCHER", ["TSHIRT", "VOUCHER", "VOUCHER", "PANTS", "TSHIRT", "TSHIRT"], 69.5),
    (["TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], "TSHIRT", ["TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], 62),
    (["TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"] , "TSHIRT", ["TSHIRT", "VOUCHER", "TSHIRT"], 45.00),
]


parameters_list_to_test_warning = [
    (["TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], "PANTS"),
    (["TSHIRT", "PANTS", "TSHIRT"], "VOUCHER"),
]