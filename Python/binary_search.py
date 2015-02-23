""" Recursive and iterative implementation of the Binary Search Algorithm. """


def RecBinarySearch(A, num, l, r):
    """ Recursive Binary Search """
    if l > r:
        return -1

    mid = l + (r - l) / 2

    if A[mid] == num:
        return mid
    elif A[mid] < num:
        return RecBinarySearch(A, num, mid + 1, r)
    else:
        return RecBinarySearch(A, num, l, mid - 1)


def ItrBinarySearch(A, num, l, r):
    """ Iterative Binary Search """
    while l <= r:
        mid = l + (r - l) / 2

        if A[mid] == num:
            return mid
        elif A[mid] < num:
            l = mid + 1
        else:
            r = mid - 1

    return -1

# if __name__ == "__main__":
#     A = (1, 2, 3, 4, 5, 6, 7)

#     print ItrBinarySearch(A, 1, 0, 6)
