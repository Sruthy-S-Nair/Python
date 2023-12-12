dictionary = {'John': [25,32,43], 'Peter': [87,55,96], 'Ram': [58,55,43], 'Meena': [63,79,85]}

given_name = input("Enter a name: ")

if given_name in dictionary:
       dictionary[given_name] = [88,77,99]
       print(dictionary)
       
else:
    print('Name not found')
