def get_number_of_apples():
    Apples_Func = int(input("Number of Apples you want to buy: "))
    return Apples_Func

def get_number_of_oranges():
    Oranges_Func = int(input("Number of Oranges you want to buy: "))
    return Oranges_Func

def compute_amount(Apples, Oranges, price_of_apple, price_of_orange):
    apple_amount = Apples * price_of_apple
    orange_amount = Oranges * price_of_orange
    total_amount = apple_amount + orange_amount
    return total_amount

def display_amount(total_amount):
    print(f"The total amount is {total_amount}")





    
# Create a program that will ask how many apples and oranges you want to buy.
print ("How many apples and oranges you want to buy? ")
Apples = get_number_of_apples()
Oranges = get_number_of_oranges()
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
price_of_apple = 20
price_of_orange = 25
#Display the output in the following format.
# The total amount is ______.
total_amount = compute_amount(Apples, Oranges, price_of_apple, price_of_orange)
display_amount(total_amount)