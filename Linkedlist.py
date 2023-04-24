class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    # function to add an element to the linked list
    def add_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print("Element ADDED Successfully")
        
    # function to remove an element from the linked list
    def remove_element(self, data):
        if self.head is None:
            print("List is empty!")
            return
        elif self.head.data == data:
            self.head = self.head.next
            print("Element REMOVED Successfully")
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    print("Element REMOVED Successfully")
                    return
                current = current.next
            print("Element not found in the list!")
    
    # function to replace an element in the linked list
    def replace_element(self, old_data, new_data):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        print("Element not found in the list!")
        
    # function to search for an element in the linked list
    def search_element(self, data):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current is not None:
            if current.data == data:
                print("Element found in the list!")
                return
            current = current.next
        print("Element not found in the list!")
        
    # function to display the linked list
    def display_list(self):
        if self.head is None:
            print("List is empty!")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


# main program
my_list = LinkedList()
print("\nMenu:")
print("1. Add an element")
print("2. Remove an element")
print("3. Replace an element")
print("4. Search for an element")
print("5. Display the linked list")
print("6. Quit")

while True:
    
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        data = input("Enter the element to add: ")
        my_list.add_element(data)
    elif choice == 2:
        data = input("Enter the element to remove: ")
        my_list.remove_element(data)
    elif choice == 3:
        old_data = input("Enter the element to replace: ")
        new_data = input("Enter the new element: ")
        my_list.replace_element(old_data, new_data)
    elif choice == 4:
        data = input("Enter the element to search for: ")
        my_list.search_element(data)
    elif choice == 5:
        my_list.display_list()
    elif choice == 6:
        break
    else:
        print("Incorrect option!")
