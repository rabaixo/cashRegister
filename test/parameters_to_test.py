# The list of parameters to test the behavior of the correct functioning of the price rules.
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

# The parameter list to test the error that the package should return
parameters_list_to_test_error = [
    ("LILLE"),
    ("SMALL")
]

#the list of parameters to test the correct updating of the total cost once an element has been deleted from the list of products
parameters_list_to_test_remove = [
    (["VOUCHER", "TSHIRT", "VOUCHER", "VOUCHER", "PANTS", "TSHIRT", "TSHIRT"] , "VOUCHER", ["TSHIRT", "VOUCHER", "VOUCHER", "PANTS", "TSHIRT", "TSHIRT"], 69.5),
    (["TSHIRT", "TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], "TSHIRT", ["TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], 62),
    (["TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"] , "TSHIRT", ["TSHIRT", "VOUCHER", "TSHIRT"], 45.00),
]

# The parameter list to test the warning that the package should return
parameters_list_to_test_warning = [
    (["TSHIRT", "TSHIRT", "VOUCHER", "TSHIRT"], "PANTS"),
    (["TSHIRT", "PANTS", "TSHIRT"], "VOUCHER"),
]