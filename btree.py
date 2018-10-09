class BTree:
    ''' Binary Tree implementation (min heap)'''


    def __init__(self, value):
        ''' constructor method '''
        
        self.tree = [None, value, None]

    def insert(self, value):
        ''' insert value as a new terminal node in the appropriate spot
            in self if value is not already in the BTree '''

        while self.tree is not None:
            if self.tree[1] == value:
                break
            elif value < self.tree[1]:
                if self.tree[0]:
                    self.tree[0].insert(value)
                else:
                    self.tree[0] = BTree(value)
                break
            else:
                if self.tree[2]:
                    self.tree[2].insert(value)
                else:
                    self.tree[2] = BTree(value)
                break

    def traverse(self):
        ''' Traverse all of the nodes in BTree from smallest to largest and return a list of values from each node '''

        nodes = []

        if self.tree is not None:
            if self.tree[0] is not None:
                nodes = self.tree[0].traverse()
            nodes.append(self.tree[1])
            if self.tree[2] is not None:
                nodes += self.tree[2].traverse()

        return nodes

    def find(self, value):
        ''' Return True if value is in the BTree or False '''

        if self.tree is not None:
            if self.tree[1] == value:
                return True
            elif self.tree[0] is not None and value < self.tree[1]:
                return self.tree[0].find(value)
            elif self.tree[2] is not None and value > self.tree[1]:
                return self.tree[2].find(value)
        
        return False
