
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    def insert(self, data):
        if self.data :
            if self.left is None:
                if self.parent is not None and self. parent.left.right is not None:
                    self.left = self.parent.left.right
                    self.right = Node(data)
                    self.right.parent = self
                self.left = Node(data)
                self.left.parent = self
            elif self.right is None:
                self.right = Node(data)
                self.right.parent = self
            else :
                self.left.insert(data)


    def PrintTree(self):
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

    def PrintRight(self):
        if self.left:
            self.left.PrintRight()
        print(self.data)

root = Node(75)

with open('problem18set', 'r') as set:
    for line in set :
        nums = line.split(" ")
        for num in nums :
            root.insert(int(num))

root.PrintTree()
