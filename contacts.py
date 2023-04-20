contacts = []
quite = ''

def start():
    global quite
    action = input("Please enter the action you want to perform: ").lower()
    if(action == "delete"):
        delete()
    elif(action == "add"):
        add()
    elif(action == "list"):
        listAll()
    else:
        quite = input("Do you want to quite the program? Type 'y' for YES or 'n' fro NO: ").lower()



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

def listAll():
    print(contacts)
    start()

if(quite == "y"):
    print("This is your list of contacts: ", contacts)
else:
    start()