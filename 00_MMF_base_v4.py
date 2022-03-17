# import statements
import re
import pandas

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



# checks for an integer more than 0
def int_check (question) :

    error = "please enter a whole number between that is more than 0"
   
    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int (input(question))

            if response <= 0:
                print (error)
            else:
                return response

        except ValueError:
            print (error)


# checks number of tickets and warns user
# if maximum is being approached

def check_tickets (tickets_sold, ticket_limit):
    #tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print ("You have {} seats left".format (ticket_limit - tickets_sold))

    # warns user that there is one seat left
    else:
        print ("*** There is ONE seat left ***")

    return ""


# gets ticket price based on age
def get_ticket_price():

    # get age between 12 and 130
    age = int_check("Age: ")

    # check that age is valid
    if age < 12:
        print ("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print ( "That is very old, it must be a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

# ******  Main Routine  ********

# initialise details loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initialise lists (to make data frame in due course)
all_names = []
all_tickets = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# ask user if they have used the program before & show instructions

# loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # checks number of ticket limit has not been exceeded
    check_tickets (ticket_count, MAX_TICKETS)

    # *** get details for each ticket ***

    # get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # get ticket price based on age
    ticket_price = get_ticket_price()
    # if age is invalid, repeat loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to list
    all_names.append (name)
    all_tickets.append (ticket_price)

  

# print details
movie_frame = pandas.DataFrame (movie_data_dict)
print (movie_frame)

# calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print ("Ticket profit: ${ : .2f}".format(ticket_profit))

# tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print ("You have sold all the available tickets")
elif ticket_count > 1:
    print ("You have sold {} tickets. There were {} tickets available")
    print ("You have sold {} tickets. There were 4 tickets available")