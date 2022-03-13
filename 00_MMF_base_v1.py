# import statements


# functions goes here

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


# checks for an integer between two values
def int_check (question, low_num, high_num) :

    error = "please enter a whole number between {} and {}".format (low_num, high_num)
   
    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int (input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)
                return "invalid age"
                 
        # if an integer is not entered, display an error
        except ValueError:
            print (error)


# ******  Main Routine  ********

# initialise details loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    
    # get details...

    # get name (can't be blank)
    name = not_blank("Name: ")
    
    # end the loop if the exit code is entered
    if name == "xxx":
        break
   
    # get age between 12 and 130
    age = int_check("Age: ", 12, 130)

    if age == "invalid age":
        continue

    count += 1  

    # tells user how many seats are left
    if count < 4:
        print ("You have {} seats left".format (MAX_TICKETS - count))

    # warns user that only one seat is left
    else:
        print("*** There is 1 seat left! ***")

if count == MAX_TICKETS:
    print ("You have sold all the available tickets!")
else:
    print ("You have sold {} tickets.   \n"
        "There are {} places still availabe".format (count, MAX_TICKETS - count))