# Implement the towers of Hanoi algorithm


def print_stacks():
    """ Print current state of three stacks.
    """
    global from_stack
    global to_stack
    global spare_stack
    print("From stack:\t", from_stack)
    print("To stack:\t", to_stack)
    print("Spare stack:", spare_stack)
    print()


def towers(n, A_stack, B_stack, C_stack):
    """ Move discs from A_stack to B_stack.
    :param n: int: Number of discs in A_stack
    :param A_stack: list: stack to move from
    :param B_stack: list: stack to move to
    :param C_stack:  list: spare stack
    :return:None
    """
    if n == 1:
        # Move the top element from A_stack to B_stack
        move_item = A_stack.pop()
        B_stack.append(move_item)
        # Print stacks after last disc move
        print_stacks()
    else:
        # Recursion for moving the whole stack of discs
        towers(n-1, A_stack, C_stack, B_stack)
        towers(1, A_stack, B_stack, C_stack)
        towers(n-1, C_stack, B_stack, A_stack)


if __name__ == "__main__":
    n = int(input("How many discs do you want on the original stack?"))
    from_stack = list(range(n, 0, -1))
    to_stack = []
    spare_stack = []
    # Print original stacks
    print_stacks()
    towers(n, from_stack, to_stack, spare_stack)
    print("Finished moving the stack of discs.")
