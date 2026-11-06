# stack_demo.py
# Assessment 3.2 - Stack (LIFO) (dynamic version of StackDemo)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        # bottom ... top
        return "[" + ", ".join(self.items) + "]  (top is right)"


def main():
    while True:
        last_name = input("\nEnter last name (or 'q' to quit): ").strip().upper()
        if last_name == "Q":
            print("Goodbye!")
            break
        if not last_name.isalpha():
            print("Please enter letters only.")
            continue

        s = Stack()

        # ADD
        print("\n--- PUSH ---")
        for letter in last_name:
            s.push(letter)
            print(f"Pushed {letter:<2} -> {s}")

        # REMOVE
        print("\n--- POP ---")
        popped = []
        while not s.is_empty():
            letter = s.pop()
            popped.append(letter)
            print(f"Popped {letter:<2} -> {s}")

        print("\nPush order:", ", ".join(last_name))
        print("Pop order: ", ", ".join(popped), "(stack is now empty)")


if __name__ == "__main__":
    main()
