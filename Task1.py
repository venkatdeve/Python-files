# Function to add a new user to the dictionary
def add_user(users, user_id, user_name):
    users[user_id] = user_name
    print(users)

# Function to update an existing user's name
def update_user(users, user_id, user_name):
    # Updating user id with name if exists
    if user_id in users:
        users[user_id] = user_name
    else:
        print("User not found in database")
    print(users)

# Function to delete a user by ID
def delete_user(users, user_id):
    # Check if the user_id exists before deleting
    if user_id in users:
        del users[user_id]
    else:
        print("The user ID doesn't exist in database")
    print(users)

# Function to list all users in the dictionary
def list_users(users):
    # Listing all Users
    if users:
        for name in users.values():
            print(name)
    else:
        print("No users in database")

# ---------------- DEMO ----------------
users = {}  # Initialize dictionary

add_user(users, 1, "satish")   # Add first user
add_user(users, 2, "vishnu")   # Add second user
add_user(users, 2, "naveen")   # Attempt duplicate ID (will warn)
list_users(users)              # List all users
delete_user(users, 1)          # Delete user with ID 1