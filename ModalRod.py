from Node import Node
from StaticRod import StaticRod
import numpy as np

class ModalRod(StaticRod):
    def __init__(self, n1: Node, n2: Node):
        super().__init__(n1, n2)

        self.ro = 7850

    def get_m(self):
        constant = (self.ro * self.A * self.length())/6

        return constant * np.array([[2, 0, 1, 0], [0, 2, 0, 1], [1, 0, 2, 0], [0, 1, 0, 2]])

    def get_inertia(self):
        return np.matmul(np.matmul(self.angle_matrix().transpose(), self.get_m()), self.angle_matrix())
