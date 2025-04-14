class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.topNode = None
        self.bottomNode = None
        self.count = 0

    def push(self, x):
        new_node = Node(x)
        if self.bottomNode is None:
            self.topNode = new_node
            self.bottomNode = new_node
        else:
            self.bottomNode.next = new_node
            self.bottomNode = new_node
        self.count += 1

    def pop(self):
        if self.topNode is None:
            return None
        value = self.topNode.data
        self.topNode = self.topNode.next
        if self.topNode is None:
            self.bottomNode = None
        self.count -= 1
        return value

    def peek(self):
        if self.topNode is None:
            return None
        return self.topNode.data

    def is_empty(self):
        return self.topNode is None

    def size(self):
        return self.count

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue1.push(x)

    def pop(self) -> int:
        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        result = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self) -> int:
        while self.queue1.size() > 1:
            self.queue2.push(self.queue1.pop())
        result = self.queue1.peek()
        self.queue2.push(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def empty(self) -> bool:
        return self.queue1.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()