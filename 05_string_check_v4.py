

# function goes here
def string_check (choice, options):

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


# valid snacks holds list of all snacks
# each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# and possible abreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "o", "juice", "e"]
]

_yes_no = [
    ["yes", "y"],
    ["no", 'n']
]

# holds snack order for a single user
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input ("Do you want to order snacks? ").lower()
    check_snack = string_check (want_snack, _yes_no)

# if they say yes, ask what snacks they want (and add to our snack list)
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
         # ask user for desired snack and put it in lower case
        desired_snack = input ("Snack: ").lower()

        if desired_snack == "xxx":
            break

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        print ("Snack choice: ", snack_choice)

        # add snack to list...

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append (snack_choice)

# show snack orders
print ()
if len (snack_order) == 0:
    print ("snacks ordered: None")

else:
    print ("Snacks ordered: ")

    for item in snack_order:
        print (item)

# loop six times to make testing quicker
for item in range (0, 6):



    # check if snack is valid
    snack_choice = string_check (desired_snack, valid_snacks)
    print ("Snack choice: ", snack_choice)
