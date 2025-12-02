contacts = {}  # for saving contacts

# to add a contact
def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print(name , "added.")

# search for contact
def search_contact(name):
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print(f"{name} not found.")

# delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted.")
    else:
        print(name , "not found.")

# show all contacts
def show_all():
    for name, info in contacts.items():
        print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")

# demo run
add_contact("Satish", "12345", "satish@mail.com")
add_contact("Mahi", "67890", "mahi@mail.com")

search_contact("Mahi")
search_contact("Chari")

show_all()

delete_contact("Mahi")
show_all()