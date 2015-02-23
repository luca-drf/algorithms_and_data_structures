
def insertionSort (lista):
    for i in xrange(len(lista)):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            lista[j - 1], lista[j] = lista[j], lista[j - 1]
            j = j - 1


def bucketSort (A):
    L = [[] for _ in xrange(100)]
    dim = len(A)

    for num in A:
        L[int(num * dim)].append(num)
    for buc in L:
        insertionSort(buc)
    
    lst = []
    for sub in L:
        lst.extend(sub)
    
    return lst

# if __name__== "__main__":
#     A = [0.43, 0.21, 0.98, 0.16, 0.32, 0.11]
    
#     print bucketSort(A)
