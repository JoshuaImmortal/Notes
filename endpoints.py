from flask import Flask
app = Flask(__name__)

List_of_entries = []
for x in range(5):
    use = input("Username: ")
    pas = input("Password: ")
    email = input("Email: ")
    Tele = input("Telephone: ")
    user = {f"username": use,
             "Password": pas,
             "Email": email,
             "Telephone": Tele}
    List_of_entries.append(user)
    
@app.route('/Profile', methods=['GET'])
def Profile():
    return List_of_entries

@app.route('/Profile/posting', methods=['POST'])
def post():
    usee = input("Username: ")
    pars = input("Password: ")
    emal = input("Email: ")
    Tel = input("Telephone: ")
    Fresh_input = {f"Username": usee,
                    "Password": pars,
                    "Email": emal,
                    "Telephone": Tel}
    List_of_entries.append(Fresh_input)
    return List_of_entries
    
@app.route('/Profile/updating', methods =['PUT'])
def put():
    dynamic_index = int(input("index(0-4): "))
    List_of_entries[dynamic_index]["Username"] = input("New username: ")
    List_of_entries[dynamic_index]["Password"] = input("New Password: ")
    List_of_entries[dynamic_index]["Email"] = input("New Email: ")
    List_of_entries[dynamic_index]["Telephone"]= input("New Telephone: ")
    return List_of_entries

@app.route('/Profile/deleting', methods =['DELETE'])
def delete():
    dynamic_index = int(input("index(0-4): "))
    List_of_entries.pop(dynamic_index)
    return List_of_entries

if(__name__=='__main__'):
    app.run()