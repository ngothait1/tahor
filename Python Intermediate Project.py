def menu():
    print("1.Save a new entry") 
    print("2.Search by ID")
    print("3.Print ages average")
    print("4.Print all names")
    print("5.Print all IDs")
    print("6.Print all entrys")
    print("7.Print entry by index")
    print("8.Exit")
    return input("Please enter you choice: ")
    
def toCon():
    input("Press Enter to continue ")

def notNumError(user_input, key):
    print("Error: " + key + " must be a number. " + str(user_input) + " is not a number")

def saveNewEntry(): # 1
    id = input("ID: ")
    if id in id_dicsh:
        print("Error: ID already exists: " + str(id_dicsh[id]))
        return False
    
    if not id.isdigit():
        notNumError(id, "ID")
        return False
    
    name = input("Name: ")
    age = input("Age: ")

    while not age.isdigit():
        print("Error: Age must be a number. " + str(age) + " is not a number")
        re_age = input("do you want to start over? y/n: ")
        if re_age == "n":
            age = input("Age: ")
        else:
            return False
        
    id_list.append([id, name, age])
    id_dicsh[id] = {"Name": name, "Age": int(age)}
    print("ID [" + str(id) + "] saved successfuly")
    return True

def searchById(new_dicsh, id_to_search): #3
    if not id_to_search.isdigit():
        notNumError(id_to_search, "ID")
        return 
        
    if id_to_search not in new_dicsh:
        print("ID " + id_to_search + " is not saved")
        return 
    else:
        print("ID: " + str(id_to_search))
        print("Name: " + str(new_dicsh[id_to_search]["Name"]))
        print("Age: " + str(new_dicsh[id_to_search]["Age"]))

def printAgesAvg(sum, round):
    if round == 0:
        ages_avg = 0
    else:
        ages_avg = sum / round
    print(ages_avg)

def printAllNames(new_list):
    for idx, name in enumerate(new_list):
        print(str(idx) + ". " + name[1])

def printAllIds(new_list):
    for idx, id in enumerate(new_list):
        print(str(idx) + ". " + id[0])

def printAllEntrys(new_list):
    for idx, entry in enumerate(new_list):
        print(str(idx) + ". " + str(entry[0]))
        print("   Name: " + str(entry[1]))
        print("   Age: " + str(entry[2]))

def printEntryByIndex(new_list):
    idx = input("Please enter the index of the entry you want to print: ")
    if not idx.isdigit():
        notNumError(idx, "Index")
        return
    idx = int(idx)
    if idx >= len(new_list):
        print("Error: Index out of range. the maximum index allowed is " + str(len(new_list) - 1))
        return
    print("ID: " + str(new_list[idx][0]))
    print("Name: " + str(new_list[idx][1]))
    print("Age: " + str(new_list[idx][2]))


id_list = []
id_dicsh ={}
count = 0
ages_sum = 0
ongoing = True

while ongoing:
    choice = menu()
    if choice == "1":
        if saveNewEntry():
            ages_sum += int(id_list[count][2])
            count += 1
            toCon()
        else:
            toCon()

    elif choice == "2":
        search_id = input("Please enter the ID you want to look for: ")
        searchById(id_dicsh, search_id)
        toCon()
  
    elif choice == "3":
        printAgesAvg(ages_sum, count)
        toCon()

    elif choice == "4":
        printAllNames(id_list)
        toCon()
    
    elif choice == "5":
        printAllIds(id_list)
        toCon()

    elif choice == "6":
        printAllEntrys(id_list)
        toCon()

    elif choice == "7":
        printEntryByIndex(id_list)
        toCon()

    elif choice == "8":
        sure = True
        while sure:
            answer = input("Are you sure? (y/n)")
            if answer == "n":
                sure = False 
            if answer == "y":
                ongoing = False
                sure = False
        
    else:
        print("Error: Option [" + str(choice) + "] does not exist. Please try again")
    
    

