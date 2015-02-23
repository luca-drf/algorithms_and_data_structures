from random import randint


def partition(A, l, r, pid):
    A[pid], A[r] = A[r], A[pid]
    j = l
    for i in range(l, r):
        if A[i] < A[r]:
            A[j], A[i] = A[i], A[j]
            j = j + 1
    A[j], A[r] = A[r], A[j]
    return j


def RecQuickSort(A, l, r):
    """ Recursive Quicksort main function """
    if l < r:
        pid = randint(l, r)
        pid = partition(A, l, r, pid)
        RecQuickSort(A, l, pid - 1)
        RecQuickSort(A, pid + 1, r)
    return A

def ItrQuickSort(A, l, r):
    """ Iterative Quicksort main function """
    stack = [(l, r)]
    while stack:
        context = stack.pop()
        l, r = context[0], context[1]
        if l < r:
            pid = randint(l, r)
            pid = partition(A, l, r, pid)

            stack.append((pid + 1, r))
            stack.append((l, pid - 1))
    return A

# if __name__ == "__main__":
#     A = [3, 4, 8, 0, 12, 34, 1, 1, 5]

#     ItrQuickSort(A, 0, 8)

#     print A
