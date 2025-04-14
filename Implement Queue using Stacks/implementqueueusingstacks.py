import ctypes

class Array :
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__( self ):
        return self._size

    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value

    def __iter__( self ):
        return _ArrayIterator( self._elements )

class _ArrayIterator :
    def __init__( self, the_array ):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._cur_index < len( self._array_ref ) :
            entry = self._array_ref[ self._cur_index ]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

class Stack:
    def __init__(self, capacity):
        self._data = Array(capacity)
        self._capacity = capacity
        self._top = -1

    def push(self, value):
        assert self._top + 1 < self._capacity, "Stack overflow"
        self._top += 1
        self._data[self._top] = value

    def pop(self):
        assert self._top >= 0, "Stack underflow"
        value = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return value

    def peek(self):
        assert self._top >= 0, "Stack is empty"
        return self._data[self._top]

    def is_empty(self):
        return self._top == -1

    def size(self):
        return self._top + 1

class MyQueue:
    def __init__(self):
        capacity = 100
        self.inStack = Stack(capacity)
        self.outStack = Stack(capacity)

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