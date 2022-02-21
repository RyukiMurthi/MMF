# checks that ticket name is not blank
def not_blank (question):
    valid = False

    while not valid:
        response = input(question)

        #if name is not blank, program continues
        if response != "":
            return response

        #if name is blank, show error (& repeat loop)  
        else:
                print("sorry - this can't be blank")


# ******  Main Routine  ********

#get name (can't be blank)
name = not_blank("Name: ")








# loop to get details

# start of loop

# initialise loop so that it runs at least once
from typing import Mapping


name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    
    # tells user how many setas are left
    if count < 4:
        print ("You have {} seats left".format (MAX_TICKETS - count))

    # warns user that only one seat is left
    else:
        print("*** There is 1 seat left! ***")

    # get details...

    #get name (can't be blank)
    name = not_blank("Name: ")
    count += 1
    print ()

if count == MAX_TICKETS:
    print ("You have sold all the available tickets!")
else:
    print ("You have sold {} tickets.   \n"
        "There are {} places still availabe".format (count, MAX_TICKETS - count))