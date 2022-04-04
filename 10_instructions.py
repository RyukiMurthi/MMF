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

def instructions (options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input ("Would you like to read the instructions?").lower()
        show_help = string_check (show_help, options)

    if show_help == "Yes":
        print ()
        print ("*** Mega Movie Fundraiser Instructions ***")
        print ()
        print ("Instructions go here.    They are brief but helpful")

    return ""

# main routine goes here
# list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]


# aks if instructions are needed
instructions (yes_no)
print ()
print ("Program launches...")