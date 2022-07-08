import time

class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def __repr__(self):
        return "Node({0}, {1})".format(self._value, self._next)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def tolist(self):
        result = list()
        node = self
        while node.next:
            result.append(node.value)
            node = node.next
        result.append(node.value)

        return result

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, item):
        self._value = item

    @property
    def tail(self):
        node = self
        while node.next:
            node = node.next
        return node


class LinkedList:
    def __init__(self, head: Node):
        self._head = head
        self._tail = self._head.tail

    def __len__(self):
        return len(self._head.tolist())

    def __getitem__(self, item: int):
        counter = 0
        node = self._head
        while node.next:
            if counter == item:
                return node
            counter += 1
            node = node.next
        if counter == item:
            return node
        return None     # Error

    def append(self, item):
        new = Node(item)
        self._tail.next = new
        self._tail = new

    def appendleft(self, item):
        self._head = Node(item, self._head)

    def pop(self):
        result = self._tail.value
        self._tail = self[len(self)-2]
        self._tail.next = None
        return result

    def popleft(self):
        result = self._head.value
        self._head = self._head.next
        return result

    def extend(self, array):
        for item in array:
            self.append(item)
        return None

    def extendleft(self, array):
        for item in array:
            self.appendleft(item)
        return None

    def remove(self, item):
        node = self._head
        prev = None
        while node:
            if node.value == item:
                if prev:    # 헤드가 아닐 경우
                    prev.next = node.next
                else:
                    self._head = node.next

            prev = node
            node = node.next
        return None

    def reverse(self):
        prev = None
        node = self._head
        self._tail = node
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp    # node, node.next = node.next, prev?
        self._head = prev
        return None

    def count(self, item):
        count = 0
        node = self._head
        while node.next:
            if node.value == item:
                count += 1
            node = node.next
        if node.value == item:
            count += 1
        return count

    def tolist(self):
        return self._head.tolist()



olist = list(range(1000000))

temp = None
for o in olist:
    node = Node(o)
    if temp:
        temp.next = node
    else:
        head = node
    temp = node
llist = LinkedList(head)


start = time.time()
llist.append(32)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
olist.append(32)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
list_to_append = ['a', 'b', 'c']
llist.extend(list_to_append)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
olist.extend(list_to_append)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
llist.popleft()
print('Time: {0:01.50f}'.format(time.time()-start))

start = time.time()
olist.pop(0)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
llist.reverse()
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
olist.reverse()
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
olist.remove(32)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
llist.remove(32)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
olist.count(32)
print('Time: {0:01.50f}'.format(time.time()-start))


start = time.time()
llist.count(32)
print('Time: {0:01.50f}'.format(time.time()-start))



