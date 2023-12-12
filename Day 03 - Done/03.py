given_age = int(input("Enter your age: "))

given_gender = input("Enter your gender (male/female): ")

ticket_price = 0

if given_age < 5 or given_age > 60:
    ticket_price = 0
elif 5 <= given_age <= 12:
    ticket_price = 10
elif given_age > 12:
    ticket_price = 50
if given_gender.lower() == 'female':
    ticket_price /= 2

print("Your ticket price is: Rs.", ticket_price)
