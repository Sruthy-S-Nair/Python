L = input("What is the minimum dimension? (length) ") 
N = input("How many photos are there?")
W = input("What is the width? ")
H = input("What is the height? ")

def check_photo(L, W, H):
    if W < L or H < L:
        return "UPLOAD ANOTHER"
    elif W == H:
        return "ACCEPTED"
    else:
        return "CROP IT"

print(check_photo(L, W, H))