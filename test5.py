class ListNode:
    def __init__(self, next, value):
        self.next = next
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(None, value)
            self.end = self.head
            return

        _end = ListNode(None, value)
        self.end.next = _end
        self.end = _end

    def pop(self):
        if self.head:
            res = self.head.value
            self.head = self.head.next
            return res
        return Nonetest

    def __repr__(self):
        array = []
        head = self.head
        while head:
            array.append(head.value)
            head = head.next
        return " ".join(map(str, array))


q = Queue()

q.append(4)
print(q)
q.append(5)
print(q)
q.append(89)
print(q)

print(q.pop())
print(q)
print(q.pop())
print(q)
print(q.pop())
print(q)
print(q.pop())
print(q)

q.append(7)
print(q)
print(q.pop())
