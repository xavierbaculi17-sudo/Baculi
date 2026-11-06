# linked_list_demo.py
# Assessment 3.2 - Singly Linked List (dynamic version of LinkedListDemo)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:     # traverse to the last node
                temp = temp.next
            temp.next = new_node

    def delete_from_head(self):
        if self.head is None:
            raise IndexError("List is empty")
        data = self.head.data
        self.head = self.head.next
        return data

    def is_empty(self):
        return self.head is None

    def __str__(self):
        parts = []
        temp = self.head
        while temp is not None:
            parts.append(temp.data)
            temp = temp.next
        parts.append("NULL")
        return " -> ".join(parts)


def main():
    while True:
        last_name = input("\nEnter last name (or 'q' to quit): ").strip().upper()
        if last_name == "Q":
            print("Goodbye!")
            break
        if not last_name.isalpha():
            print("Please enter letters only.")
            continue

        ll = LinkedList()

        # ADD (insert at tail)
        print("\n--- INSERT AT TAIL ---")
        for letter in last_name:
            ll.insert_at_tail(letter)
            print(f"Inserted {letter:<2} -> {ll}")

        # REMOVE (delete from head)
        print("\n--- DELETE FROM HEAD ---")
        removed = []
        while not ll.is_empty():
            letter = ll.delete_from_head()
            removed.append(letter)
            print(f"Removed {letter:<2} -> {ll}")

        print("\nInsert order:", ", ".join(last_name))
        print("Remove order:", ", ".join(removed), "(head = NULL, list is now empty)")


if __name__ == "__main__":
    main()
