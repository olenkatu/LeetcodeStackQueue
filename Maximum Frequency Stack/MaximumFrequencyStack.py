class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class FreqStack:
    def __init__(self):
        self.count = {}
        self.maxcount = 0
        self.group = {}
        self.stack = None

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        freq = self.count[val]

        if freq > self.maxcount:
            self.maxcount = freq

        if freq not in self.group:
            self.group[freq] = None
        new_node = Node(val, self.group[freq])
        self.group[freq] = new_node

    def pop(self) -> int:
        if self.maxcount == 0:
            return None

        node = self.group[self.maxcount]
        self.group[self.maxcount] = node.next

        val = node.val
        self.count[val] -= 1

        if self.group[self.maxcount] is None:
            self.maxcount -= 1

        return val
