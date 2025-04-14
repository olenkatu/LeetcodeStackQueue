class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class FreqNode:
    def __init__(self, key, count):
        self.key = key
        self.count = count
        self.next = None

class FreqStack:
    def __init__(self):
        self.stack_head = None
        self.freq_head = None

    def _get_freq(self, x):
        curr = self.freq_head
        while curr:
            if curr.key == x:
                return curr.count
            curr = curr.next
        return 0

    def _update_freq(self, x, delta):
        prev = None
        curr = self.freq_head
        while curr:
            if curr.key == x:
                curr.count += delta
                if curr.count == 0:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.freq_head = curr.next
                return
            prev = curr
            curr = curr.next
        if delta > 0:
            new_node = FreqNode(x, delta)
            new_node.next = self.freq_head
            self.freq_head = new_node

    def push(self, x: int) -> None:
        self._update_freq(x, 1)
        new_node = Node(x)
        new_node.next = self.stack_head
        self.stack_head = new_node

    def pop(self) -> int:
        if self.stack_head is None:
            return None
        max_freq = -1
        candidate = None
        candidate_prev = None
        prev = None
        curr = self.stack_head
        while curr:
            freq = self._get_freq(curr.data)
            if freq > max_freq:
                max_freq = freq
                candidate = curr
                candidate_prev = prev
            prev = curr
            curr = curr.next
        if candidate_prev is None:
            self.stack_head = candidate.next
        else:
            candidate_prev.next = candidate.next
        self._update_freq(candidate.data, -1)
        return candidate.data
