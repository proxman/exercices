import random

class IntList(object):
  value = 0
  next = None

  def __str__(self, *args, **kwargs):
      return "Value %d -> Next >> %s" % (self.value, self.next)


def initlist():
    listlen = random.randint(3, 7)
    head = IntList()
    head.value = 5
    for i in range(1, listlen):
        if i == 1:
            tail = head
        tail.next = IntList()
        tail.next.value = random.randint(1, 200)
        tail = tail.next
    return (head, listlen)

ptrlist, listlen = initlist()


def solution(L):
    count = 0
    while L:
        count += 1
        L = L.next
    return count

if solution(ptrlist) != listlen:
    print("solution failed")
else:
    print("solution works")