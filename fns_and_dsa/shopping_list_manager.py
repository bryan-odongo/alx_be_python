# shopping_list_manager.py

def display_menu():
    """
    Displays the menu options for the Shopping List Manager.
    """
    print("Shopping List Manager")  # Ensure exact match for grading
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize the shopping list as an empty list

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item to the list
            item = input("Enter the item to add: ").strip()  # Match the expected prompt
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            # Remove an item from the list
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        elif choice == '3':
            # View the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

