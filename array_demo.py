# array_demo.py
# Assessment 3.2 - Array (dynamic version of ArrayDemo)

def main():
    while True:
        last_name = input("\nEnter last name (or 'q' to quit): ").strip().upper()
        if last_name == "Q":
            print("Goodbye!")
            break
        if not last_name.isalpha():
            print("Please enter letters only.")
            continue

        n = len(last_name)
        arr = [None] * n      # Declare arr[n]
        size = 0

        # ADD
        print("\n--- ADD ---")
        for i in range(n):
            arr[i] = last_name[i]
            size += 1
            print(f"Added {last_name[i]:<2} -> {arr}")

        # REMOVE
        print("\n--- REMOVE ---")
        removed = []
        while size > 0:
            print(f"Removed {arr[size - 1]:<2}", end="")
            removed.append(arr[size - 1])
            arr[size - 1] = None
            size -= 1
            print(f" -> {arr}")

        print("\nAdd order:   ", ", ".join(last_name))
        print("Remove order:", ", ".join(removed), "(array is now empty)")


if __name__ == "__main__":
    main()
