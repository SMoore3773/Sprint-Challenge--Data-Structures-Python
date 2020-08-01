class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.pos = 0

    def append(self, item):
        if len(self.arr) < self.capacity:
            self.arr.append(item)
        else:
            # reassigns item at position
            self.arr[self.pos] = item
            #advances position
            self.pos = (self.pos + 1) % self.capacity

    def get(self):
        return self.arr
