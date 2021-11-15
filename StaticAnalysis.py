from Mesh import Mesh
import numpy as np
from StaticRod import StaticRod

class StaticAnalysis(Mesh):
    def __init__(self):
        super().__init__()

    def create_rod(self, n1, n2):
        self.rods.append(StaticRod(n1, n2))

    def create_model(self):
        self.get_stiffnes_matrix()
        self.set_boundary_conditions()

    def solve(self, force, prepare_model=True):
        if prepare_model:
            self.create_model()
        return np.matmul(np.linalg.inv(self.stiffnes_matrix), force)