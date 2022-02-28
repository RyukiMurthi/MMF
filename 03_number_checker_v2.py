# functions goes here

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

valid_age = 0
while valid_age == 0:
    age = int_check ("Age: ")

    if age < 12:
        print ("Sorry, youy are too young for this movie")
        continue
    elif age > 130:
        print ("That must be a mistake, you are too old")
        continue
    else:
        break