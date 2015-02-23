
def countingSort (A, k):
    """ Smarter Counting Sort """

    L = [[] for _ in range(k)]
    for n in A:
        L[n].append(n)

    output = []
    for i in L:
        output.extend(i)
    
    return output

# if __name__ == "__main__":
#     A = [5, 4, 2, 0, 4, 3, 3]
#     k = 6
    
#     B = countingSort(A, k)
#     print B

