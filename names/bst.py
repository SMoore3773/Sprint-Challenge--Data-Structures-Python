class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Insert the given value into the tree
    def insert(self, value):
        # check for valid insert
        if not self:
            return
        if value is self.value:
            self.right = BSTNode(value)
        elif value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if the current node value is the target value
        if self.value == target:
            return True
        # if the target is greater than the current node value
        elif target > self.value:
            # if there is no node to the right and the target is still larger, then there is no target value in the tree
            if not self.right:
                return False
            else:
                # if there is a node to the right, call contains method on the node to the right
                return self.right.contains(target)
        else:
            # otherwise move down the left side of the tree, and if there is no left node and target is still smaller, then there is no target in the tree
            if not self.left:
                return False
            else:
                # if there is a node to the left, then call contains method on the node to the left
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # base case to return the right most node in the tree
        if self.right is None:
            return self.value
        else:
            # recursive call of get max on the node to the right of the current node
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # function call onthe current node value
        fn(self.value)
        # check for node to the right
        if self.right:
            # call method on the node to the right
            self.right.for_each(fn)
        # check for node to the left
        if self.left:
            # call method on the node to the left
            self.left.for_each(fn)
