class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.pos = 0

    def append(self, item):
        # check if the current array is less than capacity
        if len(self.arr) < self.capacity:
            self.arr.append(item)

        # if the ring buffer is at capacity
        else:
            # reassigns item at the current position to the item added
            self.arr[self.pos] = item
            # advances position, but not past the capacity defined
            self.pos = (self.pos + 1) % self.capacity

    def get(self):
        return self.arr
