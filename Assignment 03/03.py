import math

side_a= int(input("Enter the length of side a: "))
side_b= int(input("Enter the length of side b: "))

side_c = math.sqrt(side_a ** 2 + side_b ** 2)
print(side_c)