from Node import Node
from math import sqrt
import numpy as np

class Rod:

    def __init__(self, n1: Node, n2: Node):
        self.A = 1
        self.E = 1

        if n1.x < n2.x:
            self.n1 = n1
            self.n2 = n2
        else:
            self.n1 = n2
            self.n2 = n1

    def length(self):
        return sqrt((self.n2.x - self.n1.x)**2 + (self.n2.y - self.n1.y)**2)

    def angle(self):  # TODO can be made a abstarct class and inherited to cosine and sine
        l = self.length()

        return [(self.n2.y - self.n1.y)/l, (self.n2.x - self.n1.x)/l]  # sine, cosine

    def get_nodes(self):
        return [self.n1, self.n1, self.n2, self.n2]

    def angle_matrix(self):
        result = np.zeros([4, 4])
        result[(0, 1, 2, 3), (0, 1, 2, 3)] = self.angle()[1]
        result[(0, 2, 1), (1, 3, 0)] = self.angle()[0]
        result[(1, 3), (0, 2)] = -self.angle()[0]

        return result

    def get_k(self):
        constant = (self.A * self.E)/self.length()

        return constant * np.array([[1, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 1, 0], [0, 0, 0, 0]])

    def get_stiffnes(self):
        return self.angle_matrix().transpose() * self.get_k() * self.angle_matrix()

    def node_id(self, mesh):
        return 2*mesh.nodes.index(self.n1), 2*mesh.nodes.index(self.n2)

    def get_stiffnes_cords(self, mesh):  # TODO - in a loop
        n1_id, n2_id = self.node_id(mesh)
        self.stiffnes_cords = np.array([[[n1_id, n1_id], [n1_id, n1_id+1], [n1_id, n2_id], [n1_id, n2_id+1]],
                               [[n1_id+1, n1_id], [n1_id+1, n1_id+1], [n1_id+1, n2_id], [n1_id+1, n2_id+1]],
                               [[n2_id, n1_id], [n2_id, n1_id+1], [n2_id, n2_id], [n2_id, n2_id+1]],
                               [[n2_id+1, n1_id], [n2_id+1, n1_id+1], [n2_id+1, n2_id], [n2_id+1, n2_id+1]]])