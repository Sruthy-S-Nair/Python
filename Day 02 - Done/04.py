given_list = [19,32,10,55,31,32,94,29,10,65,77,40,40]
print("Original list:", given_list)


given_list.remove(32)
print("(a) After deleting the first occurrence of 32:", given_list)


given_list = [i for i in given_list if i != 40]
print("(b) After deleting all occurrences of 40:", given_list)


del given_list[5]
print("(c) After deleting the value at index 5:", given_list)


given_list.insert(9,300)
print("(d) After modifying the value at index 9 as 300:", given_list)


given_list[2]+= 200
print("(e) After adding 200 at index 2:", given_list)


print("(f) Final list:", given_list)
print("(f.1) Length of the final list:", len(given_list))
print("(f.2) Maximum value in the final list:", max(given_list))
print("(f.3) Sum of all elements in the final list:", sum(given_list))