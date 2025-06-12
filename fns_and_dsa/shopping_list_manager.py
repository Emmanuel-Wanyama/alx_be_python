def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager application.
    Manages the shopping list based on user choices.
    """
    shopping_list = [] # Initialize an empty list for the shopping list

    while True:
        display_menu() # Display the menu
        choice = input("Enter your choice: ").strip() # Get user choice and remove leading/trailing whitespace

        if choice == '1':
            # Add an item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the item name is not empty
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove an item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit the application
            print("Goodbye!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
