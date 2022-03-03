
# valid snacks holds list of all snacks
# each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# and possible abreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]


# initialise variables
snack_ok = ""
snack = ""

# loop three times to make testing quicker
for item in range (0, 3):

    # ask user for desired snakc and put it in lower case
    desired_snack = input ("Snack: ").lower()
    
    for var_list in valid_snacks:

        # if the snack is in one of the lists, return the full
        if desired_snack in var_list:

            # get full name of snack and put it
            # in title case so it looks nice when outputted
            snack = var_list [0].title()
            snack_ok = "yes"
            break

        #if chosen snack is not valid, set snack_ok to no
        else:
            snack_ok = "no"
            
            # if the snack is not OK - ask question again.
    if snack_ok == "yes":
        print ("Snack choice", snack)
    else:
        print ("invalid choice")
