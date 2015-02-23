
def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif l == len(left):
            result.extend(right[r:])
            r = len(right)
        else:
            result.extend(left[l:])
            l = len(left)
    return result


def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) / 2
        left = A[0:mid]
        right = A[mid:]
        left = MergeSort(left)
        right = MergeSort(right)
        return merge(left, right)


if __name__ == "__main__":
    A = [5, 6, 1, 2, 8, 3, 2, 1, 0]

    print MergeSort(A)
