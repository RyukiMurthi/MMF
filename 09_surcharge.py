import re
import pandas

# function goes here
# warning: the response is returned ion title case
def string_check (choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snaclk is in one of the lists, return the full statement
        if choice in var_list:

            # get full name of snack and put it
            #in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        
        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# Main routine

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# loop until exit code
name = ""
while name != "xxx":
    name = input ("Name: ")
    if name == "xxx":
        break

    # ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input ("Please choose a payment method (CASH or CREDIT): ").lower()
        how_pay = string_check (how_pay, pay_method)


    # ask for subtotal (for testing purposes)
    subtotal = float (input("Sub total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print ("Name: {} | Subtotal: ${: .2f} | Surcharge: ${: .2f} | Total Payable: ${: .2f}".format (name, subtotal, surcharge, total))