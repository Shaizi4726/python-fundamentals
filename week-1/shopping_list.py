def main():
    shopping_list = []

    while True:
        print("\nShopping List Menu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View shopping list")
        print("4. Search for an item")
        print("5. Exit")

        action = input("Choose an action (1-5): ")

        match action:
            case '1':
                item = input("Enter the name of the item to be added: ")
                shopping_list.append(item)
                print(f"'{item}' added to your shopping list.")

            case '2':
                item = input("Enter the name of the item to be removed: ")

                try:
                    shopping_list.remove(item)
                    print(f"'{item}' removed from your shopping list.")
                except ValueError:
                    print("The item is not in the shopping list.")

            case '3':
                if not shopping_list:
                    print("Your shopping list is empty.")
                else:
                    for index, item in enumerate(shopping_list):
                        print(f"{index + 1}. {item}")

            case '4':
                item = input("Enter the name of the item to search for: ")

                if item in shopping_list:
                    position = shopping_list.index(item) + 1
                    print(f"Found! {item} is item #{position} in your list.")
                else:
                    print(f"'{item}' is not in your shopping list.")

            case '5':
                print("Exiting the shopping list application. Goodbye!")
                break

            case _:
                print("Invalid choice. Please select a valid option (1-5).")


if __name__ == "__main__":
    main()
