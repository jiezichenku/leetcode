class Stack:
    def __init__(self):
        self.list = []

    def push(self, obj):
        self.list.append(obj)

    def pop(self):
        if len(self.list) > 0:
            ret = self.list.pop(0)
            return ret

    def getLen(self) -> int:
        return len(self.list)
