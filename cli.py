import sqlite3
import os

# Create an SQLite database file in the current directory
DB_FILE = "cli_app.db"
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def create_user(name):
    conn = sqlite3.connect(DB_FILE)
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print(f"User '{name}' created successfully!")

def read_users():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    if users:
        print("Existing users:")
        for user in users:
            print(user)
    else:
        print("No users found.")

def update_user(user_id, new_name):
    conn = sqlite3.connect(DB_FILE)
    conn.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
    conn.commit()
    rows_affected = conn.total_changes
    conn.close()
    if rows_affected > 0:
        print(f"User {user_id} updated successfully!")
    else:
        print(f"User with ID {user_id} not found.")

def delete_user(user_id):
    conn = sqlite3.connect(DB_FILE)
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    rows_affected = conn.total_changes
    conn.close()
    if rows_affected > 0:
        print(f"User {user_id} deleted successfully!")
    else:
        print(f"User with ID {user_id} not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter user name: ")
            create_user(name)
        elif choice == '2':
            read_users()
        elif choice == '3':
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            update_user(user_id, new_name)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
