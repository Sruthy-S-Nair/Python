original_tuple = (78, 45, 32, 19, 82, 77, 40, 39)
print("Original tuple:", original_tuple)

tuple_list = list(original_tuple)
tuple_list[2] = 100

modified_tuple = tuple(tuple_list)
print("Modified tuple:", modified_tuple)
