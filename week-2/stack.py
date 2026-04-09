class Stack:
    def __init__(self):
        # Setting a default empty stack
        self.stack = []

    def push(self, item):
        # Adding item to top
        self.stack.append(item)
        print(f"The item {item} is added at the top successfully.")

    def pop(self):
        if not self.stack:
            raise IndexError("The stack is empty. Can't pop :(")
        else:
            # Removing and returning top item
            return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("The stack is empty. Can't peek :(")
        else:
            # Returning top item
            return self.stack[-1]

    def is_empty(self):
        # Returning the empty status of stack
        return not self.stack

    def size(self):
        # Returning the size of stack
        return len(self.stack)

    def display(self):
        # Printing all items of stack
        for item in reversed(self.stack):
            print(item)


def main():
    stack = Stack()

    print("Checking if the stack is empty: ")
    if stack.is_empty():
        print("Yes, the stack is empty.")
    else:
        print("No, the stack is not empty")

    print("\nTrying to peek item when stack is empty: ")
    try:
        peeked_item = stack.peek()
        print(f"Confirming the peeked item is {peeked_item}.")
    except IndexError as e:
        print(e)

    print("\nTrying to pop item when stack is empty: ")
    try:
        popped_item = stack.pop()
        print(f"Confirming the popped item is {popped_item}.")
    except IndexError as e:
        print(e)

    print("\nAdding items to the top of stack: ")
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("\nConfirming the stack content: ")
    stack.display()

    print("\nPopping item from a non-empty stack: ")
    try:
        popped_item = stack.pop()
        print(f"Confirming the popped item is {popped_item}.")
    except IndexError as e:
        print(e)

    print("\nConfirming stack content after an item is popped: ")
    stack.display()

    print("\nPeeking item from a non-empty stack: ")
    try:
        peeked_item = stack.peek()
        print(f"Confirming the peeked item is {peeked_item}.")
    except IndexError as e:
        print(e)

    print("\nConfirming stack content after an item is peeked: ")
    stack.display()

    print("\nChecking if the stack is empty: ")
    if stack.is_empty():
        print("Yes, the stack is empty.")
    else:
        print("No, the stack is not empty")

    print("\nGetting the size of stack: ")
    print(f"The size of the stack is {stack.size()}.")


if __name__ == "__main__":
    main()
