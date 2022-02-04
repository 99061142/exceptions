# Xander Briem
# opdracht: Pizza calculator


# Array with the pizza information

pizza = {
    "size": ["small", "medium", "large"],

    "price": [4, 6, 11],

    "total_price": [0, 0, 0],

    "amount": [0, 0, 0]
}

# /Array with the pizza information


# Function to show the receipt to the user

def receipt():
    receipt_price = 0 # Total price the user must pay

    # Get all the total prices of the pizza's
    for num, value in enumerate(pizza['total_price']):
        
        # If the total price is not 0, the receipt gets updated
        if value:
            receipt_price += value # Add the total price for the pizza to the total receipt price
            size = pizza['size'][num] # Size name
            total_price = str( pizza['total_price'][num] )  # Total price for the pizza
            amount = str( pizza['amount'][num] ) # Amount of the pizza
            price = str( pizza['price'][num] ) # Price for 1 of the pizza

            # Make a receipt with the information of the pizza
            print(
                "\n" + "---------------------------------------------------------------"
                "\n" + size + " pizza = " + price + " * " + amount + " = " + total_price + " euro")

    receipt_price = str(receipt_price) # Make the total receipt price a string

    # Add the total price for the receipt on the receipt
    print(
        "\n" + "--------------------------------------------------------------- \n" 
        "Totaal: " + receipt_price,
        "\n" + "--------------------------------------------------------------- \n" 
    )    

# /Function to show the receipt to the user


# Function to check if the receipt must be shown to the user

def check_receipt():
    # Only show the receipt if 1 of the amounts for the pizza's is not 0
    for amount in pizza['amount']:
        if amount != 0:
            receipt() 

# /Function to check if the receipt must be shown to the user



# Function to add a pizza in the array

def add_pizza(size, amount):
    index = pizza['size'].index(size) # Get the number which position the size is
    pizza_price = pizza['price'][index] # Get the price of the pizza
    

    total_price = pizza_price * amount # Calculate the total price the user must pay
    pizza['total_price'][index] += total_price # Add the total price in the array
    
    pizza['amount'][index] += amount # Add the amount of pizza's (with the size the user chose) in the array

# /Function to add a pizza in the array


#Variables
not_stopped = True #Variable to ask the questions to add a pizza


# Loop to ask what the user wants

while not_stopped:
    # Variables
    size_empty = True # Variabales for the size loop
    amount_empty = True # Variabales for the amount loop
    pizza_choices = " / ".join(pizza['size']) # Variable to show all the sizes the user can choose


    # Ask which size the user wants
    while size_empty and not_stopped:
    
        print("\n" + "Welke grootte pizza wilt u hebben?, u heeft keuze tussen '" + pizza_choices + "' \n") # Question

        size = input("Grootte: ") # Input for the user
        
        # If the user says "stop" in the input, the receipt gets shown
        if size == "stop":
            not_stopped = False # The questions does not get shown anymore
            check_receipt() # Check if the receipt must be shown

        # Check if the user did choose an size that is in the shop, and if not, the user gets shown an error message
        else:
            if size in pizza['size']:
                size_empty = False # Stops the loop, and go to the amount question

            print("\n" + "Kies een geldige grootte \n") # Error message


    # Ask the amount for the size the user wants
    while amount_empty and not_stopped:

        print("\n" + "Hoeveel stuks wilt u hebben? \n") # Question

        amount = input("Aantal(len): ") # Input for the user

        # If the user says "stop" in the input, the receipt gets shown
        if amount == "stop":
            not_stopped = False # The questions does not get shown anymore
            check_receipt() # Check if the receipt must be shown


        # Check if the user did choose an size that is in the shop, and if not, the user gets shown an error message
        else:
            try:
                
                amount = int(amount) # Try to make the amount the user has chosen an number 
                
                # Checks if the number the user has chosen is higher than 0
                if amount > 0:
                    amount_empty = False # Stops the loop, and go to the size question
                
                else:
                    print("\n" + "Kies een geheel getal (1, 2, 3, etc...). \n") # Error message
            
            except:
                print("\n" + "Kies een geheel getal (1, 2, 3, etc...). \n") # Error message

    # Add the pizza when the size and the amount are correctly answered
    if not_stopped:
        add_pizza(size, amount)

# /Loop to ask what the user wants