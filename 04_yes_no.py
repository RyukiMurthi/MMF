
def _yes_no (question):
    
    error = "Please answer yes / no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input (question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == 'no' or response == "n":
            return "no"
        else:
            print (error)

# Main routine goes here

for item in range (0, 6):
    want_snacks = _yes_no ("do you want snack?")
    print ("Answer OK, You said:", want_snacks)
    print ()