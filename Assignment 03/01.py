value_01 = int(input("Enter the first value: "))
value_02 = int(input("Enter the second value: "))
value_03 = int(input("Enter the third value: "))

def middle_value(value_01, value_02, value_03):
    return sorted([value_01, value_02, value_03])[1]

print("The middle value is ")
print(middle_value(value_01, value_02, value_03))

