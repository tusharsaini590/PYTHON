class TreeNode:
    def __init__(self, value):
        self.value = value # data
        self.children = [] # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

    def display_tree(self, level=0):
        # prints the tree structure with indentation
        print(" " * level + self.value)
        for child in self.children:
            child.display_tree(level + 1)

def display_menu():
    print("Tree Data Structure Operations:")
    print("1. Add Node")
    print("2. Remove Node")
    print("3. Traverse Tree")
    print("4. Display Tree")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    root = None
    while True:
        choice = display_menu()
        if choice == "1":
            value = input("Enter the value for the new node: ")
            if root is None:
                root = TreeNode(value)
            else:
                root.add_child(TreeNode(value))
        elif choice == "2":
            value = input("Enter the value of the node to remove: ")
            if root is not None:
                root.remove_child(TreeNode(value))
            else:
                print("Tree is empty.")
        elif choice == "3":
            if root is not None:
                root.traverse()
            else:
                print("Tree is empty.")
        elif choice == "4":
            if root is not None:
                root.display_tree()
            else:
                print("Tree is empty.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
