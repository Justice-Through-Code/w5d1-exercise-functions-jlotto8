# tip_calculator.py

# TODO: Create a function named calculate_tip
try:  #DO NOT MODIFY


    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
    def tip_calculator():
        cost = float(input("Enter the cost of the food: $"))
        num_people = int(input("Enter the number of people splitting the bill: "))
        tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
        sales_tax = 0.10  # 10% sales tax
        total_tip = (cost * tip_percentage) / 100
        total_cost = cost + total_tip + (cost * sales_tax)

    # NOTE: Calculate the tip and tax separately. 
        per_person_cost = total_cost / num_people
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
    
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
        print(f"Total bill: ${total_cost:.2f}")
        print(f"Each person should pay: ${per_person_cost:.2f}")

    # NOTE: The amounts are displayed with 2 decimals only

except ValueError: # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid 
        print("Invalid input. Please enter valid numbers.")
    
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY