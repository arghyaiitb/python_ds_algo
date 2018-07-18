class ArrayBasedStack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            self._data.pop()
        else:
            raise 'Stack is empty'

    def top(self):
        if self.is_empty():
            return self._data[-1]
        else:
            raise 'Stack is empty'

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False
