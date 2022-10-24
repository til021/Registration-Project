import json
with open("data_file(2).json", "r") as data_file:
    data = json.load(data_file)
    
def received_id():
    """
    Receives an input consisting of numbers and blank spaces.
    Each input represents an user id.
    Ex: (1 23 456) => id:1, id:23, id:456
    """    
  
    while True:
        id_list = set(input("Enter user ids: ").split())
        valid_ids = [id for id in id_list if id in data.keys()]
        
        if valid_ids == []:
            print("Input not valid.")
            
        else:
            return valid_ids
        
def receive_user(id = 0, name = 0):
    """
    Receives user data.
    """
    
    if name == 0:
        name = input("Insert user name: ")
    telephone = input("Insert user telephone: ")
    adress = input("Insert user adress: ")
    status = True
    
    if telephone == "":
        try:
            telephone = data[id]["Telephone"]
        except:
            telephone = "not given"
        
    if adress == "":
        try:
            adress = data[id]["Adress"]
        except:
            adress = "not given"

    return status, name, telephone, adress
  
def user_verification(name, telephone, adress):
    """
    Verifies if user data exists in database.
    """
    
    for id in data:
        if (data[id]["Name"] == name) and (data[id]["Telephone"] == telephone) and (data[id]["Adress"] == adress):
            data[id]["Status"] = True
            return True
    else:
        return False
    
def insert_user():
    """
    Apply the 'receive_user' and 'user_verification' functions to insert user data in the dataframe.
    """
    
    inserted_ids = []
    num_users = int(input("\n How many users do you wish to upload? "))
    
    for user in range(num_users):
        print(f"\nFor the {user+1} user:")
        status, name, telephone, adress = receive_user()
        
        if user_verification(name, telephone, adress) == False:  
            data[str(int(max(data)) + 1)] = {"Status": status, "Name": name, "Telephone": telephone, "Adress": adress}
            inserted_ids.append(max(data))
            
    return inserted_ids  
  
def remove_user(valid_ids):
    """
    Set user status to False.
    """
    
    for id in valid_ids:
        data[id]["Status"] = False
        
    return valid_ids
  
def update_user(valid_ids):
    """
    Updates the information of a user.
    """
    
    for id in valid_ids:
        print(f"\n Updating user id {id}")
        print(f"Name: {data[id]['Name']}")
        
        status, name, telephone, adress = receive_user(id = id, name = data[id]["Name"])
        data[id]["Telephone"] = telephone
        data[id]["Adress"] = adress
    
    return valid_ids   
  
def user_info(valid_ids = data.keys()):
    """
    Print the changes made in the dataframe.
    """
    
    print("----------------------------------")
    for id in valid_ids:
        print(f"""
        Id: {id}
        Name: {data[id]['Name']}
        Telephone: {data[id]['Telephone']}
        Adress: {data[id]['Adress']}
        Status: {data[id]['Status']}
        """)
    print("----------------------------------")
    
def active_users():
    """
    Select users where Status == True.
    """
    
    def status_verification(keys):
        return data[keys]["Status"] == True
    
    ids = list(filter(status_verification, data.keys()))
    return ids
  
def save_n_leave():
    """
    Save changes to a file.
    """
    
    commit = input("Commit changes? (y/n): ").lower()
    if commit == "y":
        with open("data_file(2).json", "w") as write_file:
            json.dump(data, write_file)
        print("All changes were saved!")
    else:
        print("No changes were commited!")
        
        
working = True
while working == True:
    print("""
Welcome to Tiago's Data Management Engine!
        
 1 - Insert user
 2 - Remove user
 3 - Update user
 4 - User info
 5 - All active users
 6 - All registered users 
 7 - Leave
    """)
    
    option = input("Choose a task: ")
    
    if option == "1":
        user_info(insert_user())
        
    elif option == "2":
        user_info(remove_user(received_id()))
        
    elif option == "3":
        user_info(update_user(received_id()))
        
    elif option == "4":
        user_info(received_id())
        
    elif option == "5":
        user_info(active_users())
        
    elif option == "6":
        user_info()
    
    elif option == "7":
        save_n_leave()
        working = False
    
    variable_that_exists_solemly_to_ease_the_results_readability = input("")
