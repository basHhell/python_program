# WHILE LOOP

# x=1
#
# while x <= 10:
#     print(x)
#     x += 1

#       D-2/006

# password=(input("Write your password..\n"))
#
# while password !="123at":
#     password=(input("Write your password..\n"))
# print("Welcome..")

#       D-2/004                                 # TODO LIST

#.append() is a method , difference between function and method is that method is linked to a data type.


todos = []

while True:
    user_action=input("Would you like to Add , Show, Edit the list or Exit \n")
    user_action=user_action.strip()     # .strip will remove extra space from input.. ex= "add "="add"

    match user_action:
        case 'add':
            input_1=input("Type to add in your list \n").capitalize()
            todos.append(input_1)

        case 'show':
            for x in todos:     # this loop will convert
                print(x)
            #Day-4 /002
        case 'edit':            # here we have edited our input by first getting the index value of the string becoz it is in a list and then stick that place value to the edited value.
            number = int(input("Enter no of ToDo you want to edit \n"))
            number = number - 1
            edited=input("Write your new ToDo..")
            todos[number]=edited


        case 'exit':
            print("Okay...bye")


            break








































