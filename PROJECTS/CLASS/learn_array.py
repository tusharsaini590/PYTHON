def learn_array():
   print('''An array is a fundamental data structure in computer science that stores a collection of elements of the same type in a contiguous block of memory1. It allows for efficient access to elements using indices and is widely used in programming for organizing and manipulating data1. Each item in an array is indexed starting with 01. Arrays can be one-dimensional or multi-dimensional1.

\nHere are the common operations performed on arrays:

\nTraversal: Visiting each element of an array in a specific order (e.g., sequential, reverse)1.
\nInsertion: Adding a new element to an array at a specific index1.
\nDeletion: Removing an element from an array at a specific index1.
\nSearching: Finding the index of an element in an array1.
\nThe algorithm for these operations can be summarized as follows3:

\nTraversal:
\nInitialize counter c = lower_bound_index
\nRepeat steps 3 and 4 while c < upper_bound
\nApply the specified operation on A[c]
\nIncrement counter: c = c + 1
\nInsertion at index i:
\nShift elements from index i to the end of the array one position to the right
\nInsert the new element at index i
\nDeletion at index i:
\nShift elements from index i+1 to the end of the array one position to the left
\nDecrease the size of the array by 1
\nSearching for a value v:
\nStart from the first element of the array
\nCompare each element with v
\nIf v is found, return the index of the element
\nIf v is not found in the array, return an error or a specific value indicating that v is not in the array

\nUpdating Array Elements: The value of a specific element in an array can be updated by using the assignment operator. For example, if you want to update the 5th element of an array arr to 10, you can do it as follows: arr[4] = 10;.
\nMulti-dimensional Arrays: Arrays can have more than one dimension. For example, a two-dimensional array can be thought of as a table with rows and columns. To declare a two-dimensional array, you would write something like int arr[3][4]; which creates an array with 3 rows and 4 columns.
\nPassing Arrays to Functions: You can pass arrays to functions just like you pass variables to functions. The function can then access the elements of the array. For example, to calculate the average of the elements in an array, you could pass the array and its size to a function.
\nReturning Arrays from Functions: In C, a function can’t return an array directly, but it can return a pointer to the array.
\nDynamic Arrays: Unlike arrays, dynamic arrays are not fixed in size and can grow or shrink as needed. Dynamic arrays are implemented using pointers and memory allocation functions.

\nThe time complexities of common operations on arrays are as follows12:

\nAccessing an Element by Index:
\nTime Complexity: O(1)
\nInserting an Element:
\nAt the End: Time Complexity: O(1) (Amortized)
\nAt the Beginning or at a Specific Position: Time Complexity: O(n)
\nSearching for an Element (Linear Search):
\nTime Complexity: O(n)
\nDeleting an Element:
\nTime Complexity: O(n)
\nFor two-dimensional arrays, the time complexities are1:

\nAccessing an Element by Indices:
\nTime Complexity: O(1)
\nInserting an Element at a Specific Position:
\nTime Complexity: O(1)
\nSearching for an Element (Linear Search):
\nTime Complexity: O(m * n), where ‘m’ is the number of rows and ‘n’ is the number of columns.
\nDeleting an Element:
\nTime Complexity: O(m*n)
\nTransposing a Matrix:
\nTime Complexity: O(m * n)
''')


def main():
   learn_array()

if __name__ == "__main__":
    main()

