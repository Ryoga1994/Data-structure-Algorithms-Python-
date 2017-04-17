
import sys

def merge(s,t):
    """merge ordered list s and t into an ordered list"""

    # if one of the input list is empty
    if s == []:
        return  t
    elif t == []:
        return s

    # if both s and t are not empty
    result = []

    i = 0; j = 0; # index for list s and t
    while i<len(s) and j<len(t):
        if s[i] > t[j]:
            result.append(t[j])
            j += 1
        else:
            result.append(s[i])
            i += 1

    # either list is completely append to result
    result += s[i:]
    result += t[j:]

    return result


def merge_sort(x):
    """sort list x recursively"""
    if len(x) < 2: # with less than one element in list
        return x

    # sort list recursively
    mid = int(len(x)/2)
    s = merge_sort(x[:mid]) # elements with index [0,1,..,mid-1]
    t = merge_sort(x[mid:]) # elements with index [mid,...]

    return merge(s,t)



if __name__ == "__main__":
    # read a comma-separated list of numbers from stdin
    lis = []
    # data = sys.stdin.readlines()
    # for line in data:
    for line in sys.stdin:
        line = line.rstrip()
        words = line.split(',')

        for word in words:
            # assume all input should be in correct format
            lis.append(int(word.strip(' ')))

    print(merge_sort(lis))





