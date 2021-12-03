import numpy as np
from Mesh import Mesh
from ModalRod import ModalRod
from scipy import linalg
import matplotlib.pyplot as plt


class ModalAnalysis(Mesh):
    def __init__(self):
        super().__init__()

    def create_rod(self, n1, n2):
        self.rods.append(ModalRod(n1, n2))

    def get_inertia_matrix(self):  # TODO - do not create additional variable for cords - do it on the go
        self.inertia_matrix = np.zeros([len(self.nodes)*2, len(self.nodes)*2])

        for rod in self.rods:
            rod.get_stiffnes_cords(self)
            inertia = rod.get_inertia()
            cords = rod.stiffnes_cords

            for inertia_r, cord_r in zip(inertia, cords):
                for inertia_c, cord_c in zip(inertia_r, cord_r):
                    self.inertia_matrix[cord_c[0], cord_c[1]] += inertia_c

    def create_model(self):
        self.get_stiffnes_matrix()
        self.get_inertia_matrix()
        self.set_boundary_conditions()

    def solve(self, prepare_model=True):
        if prepare_model:
            self.create_model()
        result = linalg.eigh(self.stiffnes_matrix, self.inertia_matrix)

        return 1/(2*np.pi)*np.sqrt(result[0]), result[1]

    def plot_frequencies(self, result, factor=1):
        for freq in result.transpose():
            plt.figure()
            self.plot_lattice()
            self.plot_solved(freq, factor, col='r')  # switch between displacement direction
            # self.plot_solved(-freq, factor, col='r')
