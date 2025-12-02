
# Step 1: Create an empty list to store user data (ID and password pairs)
user_data = []

# Step 2: Use a loop to generate 10 user IDs
for i in range(1, 11):  # Loop runs from 1 to 10
    # Format the user ID as USER001, USER002, ... USER010
    user_id = f"USER{i:03d}"  # :03d ensures numbers are zero-padded to 3 digits

    # Step 3: Create the password using the first 3 letters of user ID + "@123"
    password = user_id[:3] + "@123"

    # Step 4: Store the ID and password as a tuple inside the list
    user_data.append((user_id, password))

# Step 5: Print the data in a table-like format
print("User ID   | Password")
for uid, pwd in user_data:
    print(f"{uid:<8} | {pwd}")