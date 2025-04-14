import ctypes

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.topNode = None
        self.count = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.topNode
        self.topNode = new_node
        self.count += 1

    def pop(self):
        if self.topNode is None:
            return None
        pop_value = self.topNode.data
        self.topNode = self.topNode.next
        self.count -= 1
        return pop_value

    def peek(self):
        if self.topNode is None:
            return None
        return self.topNode.data

    def is_empty(self):
        return self.topNode is None

    def size(self):
        return self.count

class MyQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def push(self, value: int) -> None:
        self.inStack.push(value)

    def pop(self) -> int:
        if self.outStack.is_empty():
            while not self.inStack.is_empty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        if self.outStack.is_empty():
            while not self.inStack.is_empty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.peek()

    def empty(self) -> bool:
        return self.inStack.is_empty() and self.outStack.is_empty()

    def size(self) -> int:
        return self.inStack.size() + self.outStack.size()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()