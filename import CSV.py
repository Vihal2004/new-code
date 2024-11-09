import csv
from datetime import datetime

class item:
    def __init__(self, name, quantity, location, last_maintenance_date, serial_number, type):
        self.name = name            
        self.quantity = quantity    
        self.location = location   
        self.last_maintenance_date = last_maintenance_date     
        self.serial_number = serial_number                    
        self.type = type                                    

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"item '{item.name}' added successfully.")

    def update_item(self, serial_number, updated_item):
        for index, item in enumerate(self.inventory):
            if item.serial_number == serial_number:
                self.inventory[index] = updated_item
                print(f"item '{serial_number}' updated successfully.")
                return True
        print(f"item with serial number '{serial_number}' not found.")
        return False

    def remove_item(self, serial_number):
        initial_length = len(self.inventory)
        self.inventory = [item for item in self.inventory if item.serial_number != serial_number]
        if len(self.inventory) < initial_length:
            print(f"item '{serial_number}' removed successfully.")
        else:
            print(f"item with serial number '{serial_number}' not found, try again.")

    def generate_report(self):
        with open('inventory_report.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Quantity', 'Location', 'Last Maintenance Date', 'Serial Number', 'type'])
            for item in self.inventory:
                writer.writerow([item.name, item.quantity, item.location, item.last_maintenance_date,
                                 item.serial_number, item.type])
            print("Report generated successfully: inventory_report.csv")

def input_item_details():
    name = input("Enter item Name: ")
    quantity = int(input("Enter Quantity: "))
    location = input("Enter Location: ")
    last_maintenance_date = input("Enter Last Maintenance Date (YYYY-MM-DD): ")
    serial_number = input("Enter Serial Number: ")
    type = input("Enter type: ")
    
    try:
        datetime.strptime(last_maintenance_date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format. Please use YYYY-MM-DD.")
        return None

    return item(name, quantity, location, last_maintenance_date, serial_number, type)

def main():
    manager = InventoryManager()
    
    while True:
        print("\nInventory Management System")
        print("1. Add item")
        print("2. Update item")
        print("3. Remove item")
        print("4. Generate Report")
        print("5. Exit")
        
        choice = input("Select  an option: ")
        
        if choice == '1':
            item = input_item_details()
            if item:
                manager.add_item(item)
                
        elif choice == '2':
            serial_number = input("Enter Serial Number of the item to update: ")
            updated_item = input_item_details()
            if updated_item:
                manager.update_item(serial_number, updated_item)
                
        elif choice == '3':
            serial_number = input("Enter Serial Number: ")
            manager.remove_item(serial_number)
            
        elif choice == '4':
            manager.generate_report()
            
        elif choice == '5':
            print("Thank you.")
            print("Exiting the program.")
            break
            
        else:
            print(" Sorry, Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
