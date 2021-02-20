class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # define node placeholders
        current = self.head
        prev = None

        # check for empty
        if not current:
            return

        # reverse loop
        while current:
            # placeholder for current next node
            nxt = current.next_node
            # set the real next node to the placeholder for previous node
            current.next_node = prev
            # set the placeholder for previous node to the current node
            prev = current
            # sets the current node to the next nonde
            current = nxt
        # set the self.head node to the previos node placeholder
        self.head = prev
