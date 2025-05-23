class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return  # silently ignore
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None  # match test case
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None  # match test vibe
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return self.items[::-1].index(target)  # 0-based from top
        except ValueError:
            return -1
