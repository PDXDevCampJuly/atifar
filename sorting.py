# Implimentation of various sorting algorithms for our_lists
##########################

def selection_sort(our_list):
    """
    Look through the our_list.  Find the smallest element.  Swap it to the front.
    Repeat.
    """
    def find_min(in_list):
        """ Return the index of the minimum element in the argument."""
        smallest = in_list[0]
        smallest_index = 0
        for i in range(len(in_list)):
            if in_list[i] < smallest:
                smallest = in_list[i]
                smallest_index = i
        return smallest_index


    for i in range(len(our_list)):
        # Find smallest element of unsorted sublist
        smallest_index = find_min(our_list[i:])
        # Swap smallest item found in unsorted sublist with i-th element
        if smallest_index > 0:
            our_list[smallest_index + i], our_list[i] = our_list[i], our_list[smallest_index + i]
    return our_list


def insertion_sort(our_list):
    """
    Insert (via swaps) the next element in the sorted our_list of the previous
    elements.
    """
    # Traverse list from second element to the end
    for i in range(1, len(our_list)):
        for j in range(i, 0, -1):
            if our_list[j] < our_list[j - 1]:
                our_list[j], our_list[j - 1] = our_list[j - 1], our_list[j]
    return our_list


def merge_sort(our_list):
    """
    Our first recursive algorithm.
    """
    # Base case: If input list length is == 1, return it
    if len(our_list) == 1:
        return our_list
    # Make two recursive merge_sort() calls on two ~halves of the list
    # Roughly half length of the list
    half_length = len(our_list) // 2
    left_list = merge_sort(our_list[:half_length])
    right_list = merge_sort(our_list[half_length:])

    # Merge the two sublists
    sorted_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] < right_list[0]:
            sorted_list.append(left_list.pop(0))
        else:
            sorted_list.append(right_list.pop(0))
    if len(left_list) == 0:
        sorted_list += right_list
    if len(right_list) == 0:
        sorted_list += left_list
    return sorted_list


def get_unsorted_list(test_file):
    """
    :param test_file: string
    :return: list of items to sort
    """
    unsorted_list = []
    with open(test_file, "r") as f:
        file_contents_list = f.readline().strip("[]").split(",")
        return(list(map(eval, file_contents_list)))


# Test files of lists to sort
test_files = [
    'char10.txt',
    # 'char100.txt',
    # 'char1000.txt',
    'float10.txt',
    # 'float100.txt',
    # 'float1000.txt',
    'int10.txt',
    # 'int100.txt',
    # 'int1000.txt',
]

# Path prefix to test files
prefix = "./lists_to_sort/"
for test_file in test_files:
    unsorted_list = get_unsorted_list(prefix + test_file)
    # Save original unsorted list
    orig_unsorted_list = unsorted_list
    print("Unsorted list:", unsorted_list, "\n")

    # Run selection sort - will also sort 'unsorted_list'
    sorted_list = selection_sort(unsorted_list)
    print("Selection sort:", sorted_list)

    # Restore 'unsorted_list'
    unsorted_list = orig_unsorted_list
    # Run insertion sort - will also sort 'unsorted_list'
    sorted_list = insertion_sort(unsorted_list)
    print("Insertion sort:", sorted_list)

    # Restore 'unsorted_list'
    unsorted_list = orig_unsorted_list
    # Run merge sort - will also sort 'unsorted_list'
    sorted_list = merge_sort(unsorted_list)
    print("Merge sort:", sorted_list)

    print()
