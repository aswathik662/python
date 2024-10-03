# Predefined admin credentials
admin_credentials = {
    "admin": "password123",  # Example username and password
}

# Room inventory
rooms = {}
reservations = []

def admin_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if admin_credentials.get(username) == password:
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def add_room():
    room_number = input("Enter room number: ")
    room_type = input("Enter room type (single/double/suite): ")
    price_per_night = float(input("Enter price per night: "))
    availability = input("Is the room available? (yes/no): ").lower() == 'yes'
    
    rooms[room_number] = {
        "type": room_type,
        "price": price_per_night,
        "available": availability,
    }
    print("Room added successfully!")

def update_room_details():
    room_number = input("Enter room number to update: ")
    if room_number in rooms:
        price = float(input("Enter new price per night: "))
        availability = input("Is the room available? (yes/no): ").lower() == 'yes'
        rooms[room_number]["price"] = price
        rooms[room_number]["available"] = availability
        print("Room details updated successfully!")
    else:
        print("Room not found.")

def remove_room():
    room_number = input("Enter room number to remove: ")
    if room_number in rooms:
        del rooms[room_number]
        print("Room removed successfully!")
    else:
        print("Room not found.")

def view_all_reservations():
    if reservations:
        for reservation in reservations:
            print(reservation)
    else:
        print("No reservations found.")

def generate_reports():
    total_rooms = len(rooms)
    available_rooms = sum(1 for room in rooms.values() if room["available"])
    occupancy_rate = (total_rooms - available_rooms) / total_rooms * 100 if total_rooms else 0
    revenue = sum(room["price"] for room in rooms.values() if not room["available"])
    
    print(f"Total rooms: {total_rooms}")
    print(f"Available rooms: {available_rooms}")
    print(f"Occupancy rate: {occupancy_rate:.2f}%")
    print(f"Revenue generated: ${revenue:.2f}")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Room")
        print("2. Update Room Details")
        print("3. Remove Room")
        print("4. View All Reservations")
        print("5. Generate Reports")
        print("6. Exit")
        
        choice = input("Select an option: ")
        if choice == '1':
            add_room()
        elif choice == '2':
            update_room_details()
        elif choice == '3':
            remove_room()
        elif choice == '4':
            view_all_reservations()
        elif choice == '5':
            generate_reports()
        elif choice == '6':
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Hotel Management System")
    if admin_login():
        admin_menu()

if __name__ == "__main__":
    main()
