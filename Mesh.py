import matplotlib.pyplot as plt
import numpy as np
from Node import Node
from Rod import StaticRod, ModalRod
from scipy import linalg


class Mesh:

    def __init__(self):
        self.nodes = []  # TODO store as a dataframe with columns: index and node or see read_from_file_method
        self.rods = []

    def determinability(self):  # TODO
        pass

    def set_boundary_conditions(self, dof):
        for dir in dof:
            self.stiffnes_matrix[:, dir] = 0
            self.stiffnes_matrix[dir, :] = 0
            self.stiffnes_matrix[dir, dir] = 1

    def get_stiffnes_matrix(self):  # TODO - do not create additional variable for cords - do it on the go
        self.stiffnes_matrix = np.zeros([len(self.nodes)*2, len(self.nodes)*2])

        for rod in self.rods:
            rod.get_stiffnes_cords(self)
            stiff = rod.get_stiffnes()
            cords = rod.stiffnes_cords

            for stiff_r, cord_r in zip(stiff, cords):
                for stiff_c, cord_c in zip(stiff_r, cord_r):
                    self.stiffnes_matrix[cord_c[0], cord_c[1]] += stiff_c

    def get_nodes(self):
        nodes =[]
        for n in self.nodes:
            nodes.append([n.x, n.y])
        return np.array(nodes)

    def get_lengths(self):
        lengths = np.empty(shape=[0, 1])
        for r in self.rods:
            lengths = np.append(lengths, r.length())
        return lengths

    def read_mesh_from_mesh(self, mesh):
        self.nodes = mesh.nodes
        for r in mesh.rods:
            self.create_rod(r.n1, r.n2)

    def read_mesh_from_file(self, path):  # TODO - test for any input
        f = open(path, "r")
        for row in f:
            row = row.split(' ')

            if int(row[4]) > len(self.nodes):  # TODO not working with unformatted input - create index temporary table
                self.nodes.append(Node(int(row[0]), int(row[1])))

            if int(row[5]) > len(self.nodes):
                self.nodes.append(Node(int(row[2]), int(row[3])))

            self.create_rod(self.nodes[int(row[4])-1], self.nodes[int(row[5])-1])

    def select_rods(self, rods):
        for r in rods:
            plt.plot([r.n1.x, r.n2.x], [r.n1.y, r.n2.y], color='r', label='selected')

        plt.legend()
        plt.show()

    def plot_lattice(self):
        for i, n in enumerate(self.nodes):
            if i == 0:
                plt.scatter(n.x, n.y, color='k', linewidths=10, label='nodes')
            else:
                plt.scatter(n.x, n.y, color='k', linewidths=10, label='_nolegend_')

        for i, r in enumerate(self.rods):
            if i == 0:
                plt.plot([r.n1.x, r.n2.x], [r.n1.y, r.n2.y], color='k', label='rods')
            else:
                plt.plot([r.n1.x, r.n2.x], [r.n1.y, r.n2.y], color='k', label='_nolegend_')

        plt.legend()
        plt.show()

    def plot_solved(self, result, factor=1):
        for i, n in enumerate(self.nodes):
            if i == 0:
                plt.scatter(n.x + result[2*i] * factor, n.y + result[2*i+1] * factor, color='r', linewidths=8, label='nodes - solved')
            else:
                plt.scatter(n.x + result[2*i] * factor, n.y + result[2*i+1] * factor, color='r', linewidths=8, label='_nolegend_')

        for i, r in enumerate(self.rods):
            n1_id = self.nodes.index(r.n1)
            n2_id = self.nodes.index(r.n2)

            if i == 0:
                plt.plot([r.n1.x + result[2*n1_id] * factor, r.n2.x + result[2*n2_id] * factor],
                         [r.n1.y + result[2*n1_id+1] * factor, r.n2.y + result[2*n2_id+1] * factor],
                         color='r', label='rods')
            else:
                plt.plot([r.n1.x + result[2*n1_id] * factor, r.n2.x + result[2*n2_id] * factor],
                         [r.n1.y + result[2*n1_id+1] * factor, r.n2.y + result[2*n2_id+1] * factor],
                         color='r', label='_nolegend_')

        plt.legend()
        plt.show()


class StaticAnalysis(Mesh):
    def __init__(self):
        super().__init__()

    def create_rod(self, n1, n2):
        self.rods.append(StaticRod(n1, n2))

    def create_model(self):
        self.get_stiffnes_matrix()

    def solve(self, force, prepare_model=False):
        if prepare_model:
            self.create_model()
        return np.matmul(np.linalg.inv(self.stiffnes_matrix), force)


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

    def solve(self, prepare_model=False):
        if prepare_model:
            self.create_model()
        return linalg.eigh(self.stiffnes_matrix, self.inertia_matrix)
        # return np.sqrt(linalg.eig(self.stiffnes_matrix, self.inertia_matrix)[0].real) * 0.15915