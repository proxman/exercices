from collections import Counter
import operator
# Python Function to print leaders in array

def leaders(arr):
    c = Counter(arr)
    l = len(arr) / 2
    m = max(c.items(), key=operator.itemgetter(1))[0]
    return m if c[m] >= l else -1