import time
from linked_list import SinglyLinkedList


# Adding 1000 nodes to the beginning of a linked list

linked_list_a = SinglyLinkedList()

start = time.time()

for x in range(1000):
    linked_list_a.push(x)

end = time.time()

print(f"Time it takes to push 1000 elements to the beginning of a Linked List: {end - start}")

# Adding 1000 nodes to the end of a linked list

linked_list_b = SinglyLinkedList()

start = time.time()

for x in range(1000):
    linked_list_b.append(x)

end = time.time()

print(f"Time it takes to append 1000 elements to the end of a Linked List: {end - start}")



# The builtin Python list has the opposite complexities

normal_list_a = []

start = time.time()

for x in range(1000):
    normal_list_a.insert(0, x)

end = time.time()

print(f"Time it takes to insert 1000 elements to the beginning of a builtin list: {end - start}")


normal_list_b = []

start = time.time()

for x in range(1000):
    normal_list_a.append(x)

end = time.time()

print(f"Time it takes to add 1000 elements to the end of a builtin list: {end - start}")
