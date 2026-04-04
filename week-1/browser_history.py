def visit_new_page():
    new_page = input("Enter the URL to visit new page: ")
    print(f"You are viewing the page {new_page}")
    return new_page


def main():
    back_stack = []
    forward_stack = []
    browser_history = []
    current_page = None

    while True:
        print("Browser Menu (Select the relevant menu item):")
        print("1. Visit new page")
        print("2. Visit previous page")
        print("3. Visit next page")
        print("4. View current page")
        print("5. View full history")
        print("6. Exit the browser")

        action = input("Which action (1-6) you want to perform? ")

        match action:
            case '1':
                if current_page is not None:
                    back_stack.append(current_page)
                new_page = visit_new_page()
                forward_stack = []
                browser_history.append(new_page)
                current_page = len(browser_history) - 1

            case '2':
                if not back_stack:
                    print("No previous page.")
                else:
                    forward_stack.append(current_page)
                    current_page = back_stack.pop()
                    print(
                        f"You are viewing the page {browser_history[current_page]}.")

            case '3':
                if not forward_stack:
                    print("No next page.")
                else:
                    back_stack.append(current_page)
                    current_page = forward_stack.pop()
                    print(
                        f"You are viewing the page {browser_history[current_page]}.")

            case '4':
                if current_page is None:
                    print("No current page.")
                else:
                    print(
                        f"You are viewing the page {browser_history[current_page]}")

            case '5':
                for index, page in enumerate(browser_history):
                    if index == current_page:
                        print(f"{index + 1:>4}. {page} (current page)")
                    else:
                        print(f"{index + 1:>4}. {page}")

            case '6':
                print("Exiting the browser.")
                break

            case _:
                print("Invalid choice. Please enter a valid option (1-6).")


if __name__ == "__main__":
    main()
