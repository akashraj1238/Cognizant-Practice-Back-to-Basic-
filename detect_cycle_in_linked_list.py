class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def detect_cycle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next           
            fast_ptr = fast_ptr.next.next      
            
            if slow_ptr == fast_ptr:
                return True  
        
        return False 

    def create_cycle(self, pos):
        if pos == -1:
            return
        
        temp = self.head
        cycle_node = None
        index = 0
        
        while temp.next:
            if index == pos:
                cycle_node = temp
            temp = temp.next
            index += 1
        
        temp.next = cycle_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    
    print("Linked List before creating a cycle:")
    ll.display()

    ll.create_cycle(1)

    if ll.detect_cycle():
        print("Cycle detected in the linked list.")
    else:
        print("No cycle detected in the linked list.")
