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