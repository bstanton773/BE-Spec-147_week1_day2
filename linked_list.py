################
# Linked Lists #
################

# Linked lists are fundamental data structures in computer science used for storing and managing collections of data. Unlike python lists, 
# linked lists do not require contiguous memory allocation, allowing for dynamic memory allocation and efficient insertion and 
# deletion operations. Linked lists consist of nodes, each containing a data element and a reference (or pointer) to the next 
# node in the sequence. This flexibility makes linked lists suitable for various applications, such as implementing stacks, queues,
# and managing dynamic lists of items, making them an essential concept for aspiring software developers to understand.


# 2 Classes - A Node Class and a Linked List class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


class SinglyLinkedList:
    def __init__(self):
        # set the .head attribute to point to None to start (an empty Linked List)
        self.head = None # The head attribute points to the first node in the linked list

    # Method to add a new node to the beginning of the Linked List
    def push(self, new_value): # O(1) - Constant Time
        # Create a new node with the value passed in
        new_node = Node(new_value)
        # Set the new node's .next attribute to be the front of the list (aka the head)
        new_node.next = self.head
        # Set the new node as the head of the Linked List
        self.head = new_node

    # Method to add a new node to the end of the Linked List
    def append(self, new_value): # O(n) - Linear
        # Create a new node with the value passed in
        new_node = Node(new_value)
        # If the linked list is empty
        if self.head is None:
            # Set the new node as the first element of the list
            self.head = new_node
        # if not empty
        else:
            # Start at the first node
            current_node = self.head
            # Keep going to the next node until there is no next node
            while current_node.next is not None:
                # Move to the next node in the list
                current_node = current_node.next
            # Once the current_node.next is None, add the new node as its next
            current_node.next = new_node

    # Method to print out all of the nodes in the linked list in order
    def show(self): # O(n) - Linear Time
        print('Linked List Elements:')
        # Start at the beginning of the list
        print('head\n | \n V')
        current = self.head
        # While current is a node and not None
        while current:
            # Print the node and an arrow
            print(current, end=' -> ')
            # Move on to the next node in the linked list
            current = current.next
        # Print None at the end
        print(None)

    # Method to get a node by value
    def get_node(self, value_to_get):
        # Start with the beginning
        node_to_check = self.head
        # While node_to_check is a node
        while node_to_check is not None:
            # Check if this node's value is the value we are trying to find
            if node_to_check.value == value_to_get:
                # We found our node, return it
                return node_to_check
            # if not, move onto the next node
            node_to_check = node_to_check.next
        # If the node_to_check becomes None, we know the value is not in the linked list
        return None

    # Method to insert a new node into the linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value):
        # Get the previous node by its value
        prev_node = self.get_node(prev_value)
        # Make sure that node exists
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            # Create a new node with new value
            new_node = Node(new_value)
            # point the new_node's .next to the prev_node's .next
            new_node.next = prev_node.next
            # point the prev_node's .next to the new node
            prev_node.next = new_node

    # Method to remove a node by value
    def remove_node(self, value_to_remove):
        # Check if the list is empty
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        # If it is the head node that we are trying to remove
        if self.head.value == value_to_remove:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            return
        # Start at the first node
        current_node = self.head
        # While the current_node has a next value
        while current_node.next is not None:
            # Check if the next node is the node we are trying to remove
            if current_node.next.value == value_to_remove:
                # Set the current node's next to the next node's next
                current_node.next = current_node.next.next
                return
            # If the next node is not the node we are trying to remove
            current_node = current_node.next
        # If we get to the end of the LL, the node was never there
        print(f"{value_to_remove} is not in the Linked List")


if __name__ == "__main__":
    months = SinglyLinkedList()
    months.remove_node('January')
    months.append('Codember')
    months.append('August')
    months.push('June')
    months.push('April')
    months.push('January')
    months.append('October')
    months.remove_node('January')
    months.insert_after('June', 'July')
    months.insert_after('April', 'May')
    months.remove_node('Codember')

    months.show()
