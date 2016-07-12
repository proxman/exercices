from radon.complexity import cc_visit

test = '''
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
'''
test1 = '''
def mergesort( aList ):
  _mergesort( aList, 0, len( aList ) - 1 )


def _mergesort( aList, first, last ):
  # break problem into smaller structurally identical pieces
  mid = ( first + last ) / 2
  if first < last:
    _mergesort( aList, first, mid )
    _mergesort( aList, mid + 1, last )

  # merge solved pieces to get solution to original problem
  a, f, l = 0, first, mid + 1
  tmp = [None] * ( last - first + 1 )

  while f <= mid and l <= last:
    if aList[f] < aList[l] :
      tmp[a] = aList[f]
      f += 1
    else:
      tmp[a] = aList[l]
      l += 1
    a += 1

  if f <= mid :
    tmp[a:] = aList[f:mid + 1]

  if l <= last:
    tmp[a:] = aList[l:last + 1]

  a = 0
  while first <= last:
    aList[first] = tmp[a]
    first += 1
    a += 1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergesort(alist)
'''


# La fonction insert prend l'élément à insérer et une séquence triée en tant qu'arguments.
# Elle insère l'élement à la place correcte dans la séquence et retourne cette-dernière.

def insert(element, sequence):
    if sequence == []:
        return [element]
    elif element <= sequence[0]:
        return [element] + sequence
    else:
        return [sequence[0]] + insert(element, sequence[1:len(sequence)])


# La fonction merge prend 2 séquences triées comme arguments.
# Elle retourne une fusion des 2 séquences telles que la séquence résultante est triée.

def merge(subSequence1, subSequence2):
    if subSequence1 == []:
        return subSequence2
    elif subSequence2 == []:
        return subSequence1
    else:
        return merge(subSequence1[1:len(subSequence1)], insert(subSequence1[0], subSequence2))


# La fonction mergeSort prend la séquence à trier comme argument. La séquence d'entrée est supposée être une liste.
# Cette fonction retourne une permutation de la séquence d'entrée, triée par ordre croissant.

def mergeSort(sequence):
    if len(sequence) == 0 or len(sequence) == 1:
        return sequence
    else:
        return merge(mergeSort(sequence[0:len(sequence) // 2]), mergeSort(sequence[len(sequence)// 2 + 1:len(sequence)]))


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)


