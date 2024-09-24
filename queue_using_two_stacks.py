class queue_using_stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return "Queue is empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

    def is_empty():
        return not self.stack1 and not self.stack2


if __name__ == "__main__":
    queue = queue_using_stacks()

    while True:
        command = input("Enter command (enqueue <value>/ dequeue/ exit): ").split()

        if command[0].lower() == "enqueue" and len(command) == 2:
            try:
                value = int(command[1])
                queue.enqueue(value)

            except ValueError:
                print("Please enter a valid integer to enqueue")

        elif command[0].lower() == "dequeue":
            result = queue.dequeue()
            print(f"Dequeued: {result}")

        elif command[0].lower() == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid command. Please use 'enqueue <value>', 'dequeue', or 'exit'.")

