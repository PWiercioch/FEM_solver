from Node import Node
from math import sqrt

class Rod:

    def __init__(self, n1: Node, n2: Node):
        self.n1 = n1
        self.n2 = n2

    def length(self):
        return sqrt((self.n2.x - self.n1.x)**2 + (self.n2.y - self.n1.y)**2)

    def angle(self):  # TODO can be made a abstarct class and inherited to cosine and sine
        l = self.length()
        left_n, right_n = self.orient_nodes()

        return [(right_n.y - left_n.y)/l, (right_n.x - left_n.x)/l]  # sine, cosine

    def orient_nodes(self):
        if self.n1.x < self.n2.x:
            return [self.n1, self.n2]
        else:
            return [self.n2, self.n1]