class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        data_node = Node(data)

        if self.head is None:
            self.head = data_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = data_node

        print(f"Data {data} appended to the linked list.")

    def prepend(self, data):
        data_node = Node(data)

        if self.head is None:
            self.head = data_node
        else:
            data_node.next = self.head
            self.head = data_node

        print(f"Data {data} prepended to the linked list successfully.")

    def delete(self, data):
        if self.head is None:
            raise ValueError("List is empty.")

        if data == self.head.data:
            self.head = self.head.next
            print(f"Data {data} deleted successfully.")
            return

        current = self.head

        while current.next is not None:
            if data == current.next.data:
                current.next = current.next.next
                print(f"Data {data} is deleted successfully.")
                return
            current = current.next

        raise ValueError(f"Data {data} not found.")

    def search(self, data):
        current = self.head

        while current is not None:
            if data == current.data:
                return True
            current = current.next

        return False

    def size(self):
        if self.head is None:
            return 0

        size = 1
        current = self.head

        while current.next is not None:
            size += 1
            current = current.next

        return size

    def display(self):
        if self.head is None:
            print("Nothing to display. :(")

        else:
            current = self.head

            while current.next is not None:
                print(current.data, end=" ")
                print("->", end=" ")
                current = current.next

            print(current.data, end=" ")
            print(f"-> {current.next}")

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev_node = None
        current = self.head
        next_node = current.next

        while True:
            current.next = prev_node
            prev_node = current
            current = next_node
            if current is None:
                self.head = prev_node
                return
            next_node = current.next

    def get(self, index):
        if index >= self.size():
            raise IndexError(f"Index {index} out of bound.")

        if index == 0:
            return self.head.data

        current = self.head
        for i in range(index):
            current = current.next

        return current.data


def main():
    linked_list = LinkedList()

    linked_list.append(40)
    linked_list.append(50)
    linked_list.append(60)
    linked_list.append(70)
    linked_list.prepend(30)
    linked_list.prepend(20)
    linked_list.prepend(10)
    linked_list.prepend(0)

    linked_list.display()
    print(f"Size of the list is {linked_list.size()}.")

    try:
        linked_list.delete(70)
        linked_list.delete(30)
        linked_list.delete(0)
        linked_list.delete(100)
    except ValueError as e:
        print(e)

    linked_list.display()

    if linked_list.search(50):
        print("Yes, value 50 is present in the list.")
    else:
        print("Nope, it's not there. :(")

    print(f"Size of the list is {linked_list.size()}.")

    linked_list.reverse()

    linked_list.display()

    try:
        data = linked_list.get(3)
        print(f"Data at index positon 3 is {data}.")
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()
