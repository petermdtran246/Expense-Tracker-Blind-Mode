"""
Expense Tracker - A simple console-based application to track group expenses
and secretly determine who spent the most (blind mode).
Perfect for splitting bills or fun spending competitions.
"""

import art

# Display the custom ASCII art logo at startup
print(art.logo)

def find_highest_spending(spending_dictionary):
    """
    Find the person with the highest spending from the dictionary.
    
    Args:
        spending_dictionary (dict): Dictionary with names as keys and spending amounts as values.
    
    Returns:
        str: Formatted string announcing the winner and their spending amount.
        
    Note: In case of a tie, returns the first person encountered (preserves insertion order).
    """
    winner = ""
    highest_spending = 0
    for spender in spending_dictionary:
        spending_amount = spending_dictionary[spender]
        if spending_amount > highest_spending:
            highest_spending = spending_amount
            winner = spender
    return f"The winner is {winner} with the spending of $ {highest_spending}."

# Main program
spending = {}                # Stores name: amount pairs
continue_spending = True     # Loop control flag
while continue_spending:
    name = input('Who spent the money?: ')
    amount = int(input('How much did they spent: $'))
    spending[name] = amount # Add a key-value pair to the dictionary
    should_continue = input("Is there another expense? Type ‘yes’ or ‘no’\n").lower()
    if should_continue == "no":
        continue_spending = False # Important point: Stop the loop
        print(find_highest_spending(spending))
    elif should_continue == "yes":
        # Clear screen for next person (blind mode - others can't see previous entries)
        print("\n" * 20)
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
            
            