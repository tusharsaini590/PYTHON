import my_linkedlist as ll
import my_stack as st
import my_queue as que
import my_graph as grp
import my_tree as tr
import dynamic_array as my_array
import learn_array as la
import learn_ll as lll
import learn_stack as ls
import learn_queue as lque
import learn_graph as lg
import learn_tree as lt
import matplotlib.pyplot as plt



# code snippet to give gfg link for array
def learn_array():
    print("Learn Array:")
    la.main()
    print("\n-for reference of  ARRAY: https://www.geeksforgeeks.org/array-data-structure/\n")


# code snippet to give gfg link for linked list
def learn_ll():
    print("Learn Linked List:")
    lll.main()
    print("\n- For reference of LINKED LIST: https://www.geeksforgeeks.org/data-structures/linked-list/\n")


# code snippet to give gfg link for stack
def learn_stack():
    print("Learn Stack:")
    ls.main()
    print("\n- For reference of STACK: https://www.geeksforgeeks.org/stack-data-structure/\n")


# code snippet to give gfg link for queue
def learn_queue():
    print("Learn Queue:")
    lque.main()
    print("\n- For reference of QUEUE: https://www.geeksforgeeks.org/queue-data-structure/\n")


# code snippet to give gfg link for graph
def learn_graph():
    print("Learn Graph:")
    lg.main()
    print("\n-For reference of GRAPH: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/\n")


# code snippet to give gfg link for trees
def learn_tree():
    print("Learn Tree:")
    lt.main()
    print("\n-For reference of TREE: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/\n")


# Define a dictionary to store menu options and their URLs using dictionay
# user have to type the key to get the desired links of the topic
online_resources = {
    # for an intro to the dsa
    "Introduction": {
        "Web References": "- [Introduction to Theory of Computation](https://ict.iitk.ac.in/wp-content/uploads/CS340-Theory-of-Computation-18-toc.pdf)",
        "Audio-Video": "- [Introduction to Theory of Computation](https://www.youtube.com/watch?v=6VF2Q0pgUFI)\n"
    },
    # for an intro to array
    "Array": {
        "Web References": "- [Bubble Sort Visualization](https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/)",
        "Audio-Video": "- [Introduction to Arrays](https://www.youtube.com/watch?v=udapt4FGY20)\n"
    },
    # for an intro to stack
    "Stack": {
        "Web References": "- [Stacks](https://courses.edx.org/assets/courseware/v1/e049a1cb2818e36d0e24f17ead92813f/c4x/PekingX/04830050x/asset/chapter3_EN.pdf)",
        "Audio-Video": "- [Stacks](https://www.youtube.com/watch?v=g1USSZVWDsY&list=PLBF3763AF2E1C572F&index=2)\n"
    },
    # for an intro to queue
    "Queue": {
        "Web References": "- [Queues](https://courses.edx.org/assets/courseware/v1/e049a1cb2818e36d0e24f17ead92813f/c4x/PekingX/04830050x/asset/chapter3_EN.pdf)",
        "Audio-Video": "- [Queues](https://www.youtube.com/watch?v=PGWZUgzDMYI&list=PLBF3763AF2E1C572F&index=3)\n"
    },
    # for an intro to linked list
    "Linked List": {
        "Web References": "- [Linked Lists](https://cse.iitkgp.ac.in/~pds/cs210/html/lectures.htm)",
        "Audio-Video": "- [Linked Lists](https://www.youtube.com/watch?v=udapt4FGY20)\n"
    },
    # for an intro to sorting
    "Sorting": {
        "Web References": "- [Sorting Techniques](https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/)",
        "Audio-Video": "- [Sorting Techniques](https://www.youtube.com/watch?v=gtWw_8VvHjk&list=PLBF3763AF2E1C572F&index=10)\n"
    },
    # for an intro to tree
    "Tree": {
        "Web References": "- [Binary Trees](https://www.cse.iitk.ac.in/users/dsrkg/cs210/html/lectures.htm)",
        "Audio-Video": "- [Binary Trees](https://www.youtube.com/watch?v=tORLeHHtazM&list=PLBF3763AF2E1C572F&index=6)\n"
    }
}


# function to print the link online rsource then print the keys from the dictionary in the online_resources function
def display_online_resources():
    print("Online Resources:\n")
    for key in online_resources:
        print(key)


# function to print the values against the key which the user selected
def select_online_resource(resource):
    if resource in online_resources:
        print(resource)
        for subheading, link in online_resources[resource].items():
            print(subheading)
            print(link)
    else:
        print("Invalid resource")


# declaring this function for 2nd option in the main menu of the  code
def display_testing_choice():
    print("1) Array")
    print("2) Linked List")
    print("3) Stack")
    print("4) Queue")
    print("5) Tree")
    print("6) Graph\n")
    choice = input("Enter your choice: ")
    # using the imported functions for operations on array, stack, queue, linked list
    if (choice == "1"):
        my_array.main()

    elif (choice == "2"):
        ll.cdll_main()

    elif (choice == "3"):
        st.stack_main()

    elif (choice == "4"):
        que.main()

    elif (choice == "5"):
        tr.main()

    elif (choice == "6"):
        grp.main()

    else:
        print("Invalid choice")


def visualize_user_progress():
    # Example: Visualize user progress for an array
    total_attempts = int(input("Enter the total number of attempts: "))
    successful_attempts = int(input("Enter the number of successful attempts: "))
    errors = int(input("Enter the number of errors: "))

    # Visualization for user progress
    plt.bar(['Total Attempts', 'Successful Attempts', 'Errors'], [total_attempts, successful_attempts, errors])
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.title('User Progress Visualization')
    plt.show()


# Very main menu of choice of actions
def main_menu():
    print(
        "\t\t\t\t\t\tGood to see you are interested in dsa\n\t\t\t\t\t\t From below option from where you wanna start:\n")
    print("1) Learn DSA")
    print("2) Learn by Testing")
    print("3) Git Repository for accessing codes")
    print("4) Get online resources")
    print("5) Visualize user progress\n")


# sub-menu under the Learn DSA option
def dsa_menu():
    print(" Learn DSA Menu:")
    print("1) Array")
    print("2) Linked List")
    print("3) Stack")
    print("4) Queue")
    print("5) Graph")
    print("6) Tree\n")


# codes for the Sub-Menu under Learn DSA option with exception handling
def main(linked_list=None):
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            dsa_menu()

            dsa_choice = input("Enter your choice (1-6): ")

            if dsa_choice == "1":
                learn_array()

            elif dsa_choice == "2":
                learn_ll()

            elif dsa_choice == "3":
                learn_stack()

            elif dsa_choice == "4":
                learn_queue()

            elif dsa_choice == "5":
                learn_graph()

            elif dsa_choice == "6":
                learn_tree()


            else:
                print("Invalid choice")

        elif choice == "2":
            display_testing_choice()

        elif choice == "3":
            print("GIT Repository for accessing codes: https://github.com/tusharsaini590/Data-Structures-Algorithm\n")

        elif choice == "4":
            display_online_resources()
            selected_resource = input("Select a resource: ")
            select_online_resource(selected_resource)
        elif choice == "5":
            visualize_user_progress()


        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()






















    '''def visualize_array(array):
        array = [5, 6, 4, 1, 0]
        plt.bar(range(len(array)), array)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Array Visualization')
        plt.show()


    def visualize_linked_list(linked_list):
        fig, ax = plt.subplots()
        ax.set_xlim([0, 10])
        ax.set_ylim([0, 10])

        for i, node in enumerate(linked_list):
            circle = patches.Circle((i, node), 0.5, edgecolor='black', facecolor='none')
            ax.add_patch(circle)

        plt.title('Linked List Visualization')
        plt.show()

    def visualize_stack(stack):
        plt.bar(range(len(stack)), stack)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Stack Visualization')
        plt.show()

    def visualize_queue(queue):
        plt.barh(range(len(queue)), queue)
        plt.xlabel('Value')
        plt.ylabel('Index')
        plt.title('Queue Visualization')
        plt.show()


    def visualize_tree(tree):
        G = nx.DiGraph()
        for node in tree:
            if node.parent is not None:
                G.add_edge(node.parent.value, node.value)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.title('Tree Visualization')
        plt.show()


    def visualize_graph(graph):
        G = nx.Graph()
        for edge in graph.edges:
            G.add_edge(*edge)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.title('Graph Visualization')
        plt.show()
    '''
