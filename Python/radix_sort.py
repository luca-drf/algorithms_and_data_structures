from math import log


def split(lst, base, digit_num):
    """ append the number to the list selected by the digit """
    buckets = [[] for _ in xrange(base)]
    for num in lst:
        d = (num // base ** digit_num) % base
        buckets[d].append(num)
    return buckets


def merge(lst):
    """ concatenate the lists back in order for the next step """
    new_list = []
    for sublist in lst:
        new_list.extend(sublist)
    return new_list


def max_abs(lst):
    """ return largest abs value element of a list """
    return max(abs(num) for num in lst)


def radixSort(lst, base):
    # there are as many passes as there are digits in the longest number
    passes = int(round(log(max_abs(lst), base)) + 1)
    new_list = lst[:]
    for digit_num in range(passes):
        new_list = merge(split(new_list, base, digit_num))

    return new_list


# if __name__ == "__main__":
#     A = [5, 4, 2, 0, 4, 3, 3]

#     print radixSort(A, 10)
