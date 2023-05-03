contacts = []
quit = ''

def start():
    global quit
    action = input("Enter 'add' to add contacts\nEnter 'delete' to delete contacts\nEnter 'list' to list contacts\nEnter 'edit' to edit contacts\nPlease enter the action you want to perform: ").lower()
    if(action == "delete"):
        delete()
    elif(action == "add"):
        add()
    elif(action == "list"):
        listAll()
    elif(action == "edit"):
        update()



def add():
    enter_more = "y"
    while(enter_more == "y"):
        contact = {}
        name = input("Please enter a name: ")
        number = input("Please enter a contact: ")
        contact[name] = number
        contacts.append(contact)
        enter_more = input("Do you want to enter more, type 'y' for YES or 'n' fro NO: ").lower()
    start()

def delete():
    name = input("Please enter the name of contact to delete: ")
    for i in contacts:
        if(list(i.keys())[0] == name):
            contacts.remove(i)
            break
    start()

def update():
    name = input("Please enter the name of contact to edit: ")
    number = input("Please enter the new contact: ")
    for index, i in enumerate(contacts):
        if(list(i.keys())[0] == name):
            contacts[index][name] = number
            break
    start()

def listAll():
    print("All your contacts: ", contacts)
    start()

start()
quit = input("Do you want to quit the program? Type 'y' for YES or 'n' fro NO: ").lower()

if(quit == "y"):
    print("This is your list of contacts: ", contacts)
else:
    start()