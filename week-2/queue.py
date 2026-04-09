from collections import deque


class Queue:
    def __init__(self):
        # Setting a default empty queue
        self.queue = deque()

    def enqueue(self, item):
        # Adding item to back of queue
        self.queue.append(item)
        print(f"The item {item} is added to the back of queue successfully.")

    def dequeue(self):
        if not self.queue:
            raise IndexError("The queue is empty. Can't dequeue :(")
        else:
            # Removing and returning the item from front
            return self.queue.popleft()

    def peek(self):
        if not self.queue:
            raise IndexError("The queue is empty. Can't peek :(")
        else:
            # Returning front item
            return self.queue[0]

    def is_empty(self):
        # Returning the empty status of queue
        return not self.queue

    def size(self):
        # Returning the size of queue
        return len(self.queue)

    def display(self):
        # Printing all items of queue
        for item in self.queue:
            print(item)


class CircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.queue = [None] * k
        self.front = self.back = -1

    def enqueue(self, item):
        if (self.back + 1) % self.capacity == self.front:
            raise OverflowError(
                "The circular queue is full. Better luck next time :(")
        else:
            if self.is_empty():
                self.front = 0
                self.back = 0
            else:
                self.back = (self.back + 1) % self.capacity
            self.queue[self.back] = item
            print(f"Item {item} added successfully to circular queue.")

    def dequeue(self):
        if self.is_empty():
            raise IndexError(
                "The circular queue is empty. No item to remove :(")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            if (self.front == self.back):
                self.front = self.back = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return item

    def peek(self):
        if self.is_empty():
            raise IndexError("The circular queue is empty. No item to peek :(")
        else:
            return self.queue[self.front]

    def is_empty(self):
        return self.front == self.back == -1

    def size(self):
        if self.is_empty():
            return 0
        return (self.back - self.front + self.capacity) % self.capacity + 1

    def display(self):
        if self.is_empty():
            print("Empty circular queue. Nothing to display. :(")
        else:
            front = self.front
            while True:
                print(self.queue[front])
                if front == self.back:
                    break
                front = (front + 1) % self.capacity


def main():
    print(f"{'='*80}")
    print("Queue")
    print(f"{'='*80}\n\n")

    queue = Queue()
    print("Checking if the queue is empty: ")
    if queue.is_empty():
        print("Yes, the queue is empty.")
    else:
        print("No, the queue is not empty")

    print("\nTrying to peek item when queue is empty: ")
    try:
        peeked_item = queue.peek()
        print(f"Confirming the peeked item is {peeked_item}.")
    except IndexError as e:
        print(e)

    print("\nTrying to dequeue item when queue is empty: ")
    try:
        dequeued_item = queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
    except IndexError as e:
        print(e)

    print("\nAdding items to the back of queue: ")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("\nConfirming the queue content: ")
    queue.display()

    print("\nDequeuing item from a non-empty queue: ")
    try:
        dequeued_item = queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
    except IndexError as e:
        print(e)

    print("\nConfirming queue content after an item is dequeued: ")
    queue.display()

    print("\nPeeking item from a non-empty queue: ")
    try:
        peeked_item = queue.peek()
        print(f"Confirming the peeked item is {peeked_item}.")
    except IndexError as e:
        print(e)

    print("\nConfirming queue content after an item is peeked: ")
    queue.display()

    print("\nChecking if the queue is empty: ")
    if queue.is_empty():
        print("Yes, the queue is empty.")
    else:
        print("No, the queue is not empty")

    print("\nGetting the size of queue: ")
    print(f"The size of the queue is {queue.size()}.")

    print(f"\n\n{'='*80}")
    print("Circular Queue")
    print(f"{'='*80}\n\n")

    circular_queue = CircularQueue(5)
    print("Checking if the circular queue is empty: ")
    if circular_queue.is_empty():
        print("Yes, the circular queue is empty.")
    else:
        print("No, the circular queue is not empty")

    print("\nTrying to peek item when circular queue is empty: ")
    try:
        peeked_item = circular_queue.peek()
        print(f"Confirming the peeked item is {peeked_item}.")
    except IndexError as e:
        print(e)

    print("\nTrying to dequeue item when circular queue is empty: ")
    try:
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
    except IndexError as e:
        print(e)

    print("\nAdding items to the circular queue: ")
    try:
        circular_queue.enqueue(1)
        circular_queue.enqueue(2)
        circular_queue.enqueue(3)
        circular_queue.enqueue(4)
        circular_queue.enqueue(5)
        circular_queue.enqueue(6)
    except OverflowError as e:
        print(e)

    dequeued_item = circular_queue.dequeue()
    print(f"Confirming the dequeued item is {dequeued_item}.")
    circular_queue.enqueue(6)

    print("\nPeeking item from a non-empty circular queue: ")
    try:
        peeked_item = circular_queue.peek()
        print(f"Confirming the peeked item is {peeked_item}.")
    except IndexError as e:
        print(e)

    print("\nConfirming circular queue content after an item is peeked: ")
    circular_queue.display()

    print("\nChecking if the circular queue is empty: ")
    if circular_queue.is_empty():
        print("Yes, the circular queue is empty.")
    else:
        print("No, the circular queue is not empty")

    print("\nGetting the size of queue: ")
    print(f"The size of the circular queue is {circular_queue.size()}.")

    print("\nDequeuing item from a non-empty circular queue: ")
    try:
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
        dequeued_item = circular_queue.dequeue()
        print(f"Confirming the dequeued item is {dequeued_item}.")
    except IndexError as e:
        print(e)

    print("\nConfirming the circular queue content: ")
    circular_queue.display()


if __name__ == "__main__":
    main()
