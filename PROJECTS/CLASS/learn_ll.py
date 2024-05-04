def learn_ll():
    print('''
    A linked list is a linear data structure that can store a collection of “nodes” connected together via links, i.e., pointers.
     \nUnlike arrays, linked list nodes are not stored at a contiguous location; instead, they are linked using pointers to different memory locations. Each node consists of the data value and a pointer to the address of the next node within the linked list.

\nA linked list is a dynamic linear data structure whose memory size can be allocated or de-allocated at run time based on the operation insertion or deletion. 
\nThis helps in using system memory efficiently. Linked lists can be used to implement various data structures like a stack, queue, graph, hash maps, etc.

\nA linked list starts with a head node which points to the first node. 
\nEvery node consists of data which holds the actual data (value) associated with the node and a next pointer which holds the memory address of the next node in the linked list. The last node is called the tail node in the list which points to null, indicating the end of the list.

\nIn comparison to arrays, linked lists are dynamic in size, and any number of nodes can be added dynamically. 
\nAn array can accommodate similar types of data types, whereas linked lists can store various nodes of different data types.

\nThere are various types of linked lists, including Singly Linked Lists, Doubly Linked Lists, and Circular Linked Lists.
 \nSingly linked lists contain two “buckets” in one node; one bucket holds the data and the other bucket holds the address of the next node of the list. Doubly Linked Lists contain three “buckets” in one node; one bucket holds the data and the other buckets hold the addresses of the previous and next nodes in the list. Circular linked lists can exist in both singly linked list and doubly linked list.

\nThe basic operations in the linked lists are insertion, deletion, searching, display, and deleting an element at a given key. These operations are performed on Singly Linked Lists. Insertion can be done at the beginning, at the end, or at a given position within the list. Deletion operation deletes an element at the beginning of the list. The display operation displays the complete list. The search operation searches an element using the given key. The delete operation deletes an element using the given key.

\n\t\t **Algorithm For Linked List Operations**\n
\t\tInsertion at the Beginning of the List:
->Create a new node and assign the data to it.\n
->Point the next pointer of the new node to the current head node.\n
->Update the head pointer to point to the new node.\n
\t\tInsertion at the End of the List:\n
->Create a new node and assign the data to it.\n
->Traverse the list to find the last node.\n
->Point the next pointer of the last node to the new node.\n
\t\t->Insertion at a Specific Position in the List:\n
->Create a new node and assign the data to it.\n
->Traverse the list to find the node at the position before the desired position.\n
->Point the next pointer of the new node to the next node of the current node.\n
->Point the next pointer of the current node to the new node.\n
\t\tDeletion at the Beginning of the List:\n
->Point the head pointer to the second node in the list.\n
->Delete the first node.\n
\t\tDeletion at the End of the List:\n
->Traverse the list to find the second last node.\n
->Delete the last node and set the next pointer of the second last node to NULL.\n
\t\tDeletion at a Specific Position in the List:\n
->Traverse the list to find the node before the node to be deleted.\n
->Point the next pointer of the current node to the node after the node to be deleted.\n
\t\tDelete the node.\n
->Searching for an Element in the List:\n
->Start from the head node.\n
->Traverse the list and compare each node’s data with the target data.\n
->If a match is found, return the position of the node.\n
->If no match is found, return an indication that the element is not in the list.\n
\t\tDisplaying the List:\n
->Start from the head node.\n
->Traverse the list and print the data of each node.\n

''')

def main():
   learn_ll()

if __name__ == "__main__":
    main()
