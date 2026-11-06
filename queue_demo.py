# queue_demo.py
# Assessment 3.2 - Queue (FIFO) (dynamic version of QueueDemo)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)          # add at the rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self.items.pop(0)         # remove from the front

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "front [" + ", ".join(self.items) + "] rear"


def main():
    while True:
        last_name = input("\nEnter last name (or 'q' to quit): ").strip().upper()
        if last_name == "Q":
            print("Goodbye!")
            break
        if not last_name.isalpha():
            print("Please enter letters only.")
            continue

        q = Queue()

        # ADD
        print("\n--- ENQUEUE ---")
        for letter in last_name:
            q.enqueue(letter)
            print(f"Enqueued {letter:<2} -> {q}")

        # REMOVE
        print("\n--- DEQUEUE ---")
        removed = []
        while not q.is_empty():
            letter = q.dequeue()
            removed.append(letter)
            print(f"Dequeued {letter:<2} -> {q}")

        print("\nEnqueue order:", ", ".join(last_name))
        print("Dequeue order:", ", ".join(removed), "(queue is now empty)")


if __name__ == "__main__":
    main()
