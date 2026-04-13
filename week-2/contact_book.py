import json
import os

json_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(json_dir, 'assets', 'contacts.json')


def contacts_menu():
    print("\nContacts Menu:\n")
    print("1. Add a contact")
    print("2. Delete a contact by name")
    print("3. Search contact(s) by name")
    print("4. Update a contact's phone or email")
    print("5. List all contacts")
    print("6. Exit\n")


def load_json():
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    print("No contacts file to load.")
    return {}


def dump_json(data):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=8, sort_keys=True)
    except Exception:
        print("Unable to write to json file.")


def main():
    data = load_json()

    while True:
        contacts_menu()

        user_choice = input("Select operation from the menu (1-6): ")

        match user_choice:
            case '1':
                name = input("Enter contact name: ")
                if name in data:
                    print(f"Contact '{name}' already exists.")
                    continue
                phone = input("Enter contact phone number: ")
                email = input("Enter contact email address: ")

                if not phone or not email:
                    print("Phone and email cannot be empty.")
                    continue

                data[name] = {'phone': phone, 'email': email}
                dump_json(data)
                print(f"Contact '{name}' added.")

            case '2':
                name = input("Enter contact name to delete: ")
                if name in data:
                    del data[name]
                    dump_json(data)
                    print(f"Contact '{name}' deleted.")
                else:
                    print(f"Contact '{name}' not found.")

            case '3':
                search_term = input("Enter the name to search in contacts: ")
                matches = {key: value for key,
                           value in data.items() if search_term.lower() in key.lower()}

                if not matches:
                    print(f"No contacts found matching '{search_term}'.")
                else:
                    print(f"{'Name':<15} -> {'Phone':<13} Email")
                    for name, value in sorted(matches.items()):
                        print(
                            f"{name:<15} {value['phone']:<13} {value['email']}")

            case '4':
                name = input("Enter contact name to update: ")

                if name not in data:
                    print(f"Contact '{name}' not found to update.")
                    continue

                while True:
                    print("Fields Menu:")
                    print("1. Phone")
                    print("2. Email")
                    print("3. Exit")
                    update_field = input("Select the field to update (1-3): ")

                    match update_field:
                        case '1':
                            phone = input("Enter the updated phone number: ")

                            if not phone:
                                print("Phone cannot be empty.")
                                continue

                            data[name]['phone'] = phone
                            print(
                                f"Phone number for contact '{name}' updated.")
                            dump_json(data)
                            break

                        case '2':
                            email = input("Enter the updated email: ")

                            if not email:
                                print("Email cannot be empty.")
                                continue

                            data[name]['email'] = email
                            dump_json(data)
                            print(f"Email for contact '{name}' updated.")
                            break

                        case '3':
                            break
                        case _:
                            print("Please select valid menu item (1-3).")

            case '5':
                if not data:
                    print("No contacts saved yet.")
                else:
                    print(f"{'Name':<15} -> {'Phone':<13} Email")
                    for name, value in sorted(data.items()):
                        print(
                            f"{name:<15} {value['phone']:<13} {value['email']}")

            case '6':
                break

            case _:
                print("Please select valid menu item (1-6).")


if __name__ == "__main__":
    main()
