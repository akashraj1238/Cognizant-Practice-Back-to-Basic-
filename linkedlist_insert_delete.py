# Node class represents each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def insert_at_beginning(self, data):
        new_node = Node(data)  
        new_node.next = self.head  
        self.head = new_node  
        print(f"Inserted {data} at the beginning of the list.")

    def insert_at_end(self, data):
        new_node = Node(data)  
        if not self.head:
            self.head = new_node  
        else:
            temp = self.head
            while temp.next:  
                temp = temp.next
            temp.next = new_node 
        print(f"Inserted {data} at the end of the list.")

    def delete_node(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next  
            temp = None  
            print(f"Deleted {key} from the list.")
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"{key} not found in the list.")
            return

        prev.next = temp.next
        temp = None
        print(f"Deleted {key} from the list.")

    def display(self):
        if self.head is None:
            print("The list is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)

    print("Current Linked List:")
    ll.display()

    ll.delete_node(20)  
    ll.delete_node(100)  
    print("Linked List after deletion:")
    ll.display()
