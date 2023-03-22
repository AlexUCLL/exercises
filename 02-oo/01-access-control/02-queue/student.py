class Queue:
    def __init__(self):
        self.__q = []
    
    def add(self, item):
        self.__q.append(item)

    def next(self):
        item = self.__q[0]
        del self.__q[0]
        return item

    def is_empty(self):
        return len(self.__q) == 0