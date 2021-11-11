import matplotlib.pyplot as plt
import numpy as np
from Node import Node
from Rod import Rod


class Mesh:

    def __init__(self):
        self.nodes = []  # store as a dataframe with columns: index and node or see read_from_file_method
        self.rods = []


    def determinability(self):  # TODO
        pass

    def get_stiffnes_matrix(self):
        self.stiffnes_matrix = np.zeros([len(self.nodes)*2, len(self.nodes)*2])

        for rod in self.rods:
            rod.get_stiffnes_cords(self)
            stiff = rod.get_stiffnes()
            cords = rod.stiffnes_cords

            for stiff_r, cord_r in zip(stiff, cords):
                for stiff_c, cord_c in zip(stiff_r, cord_r):
                    self.stiffnes_matrix[cord_c[0], cord_c[1]] += stiff_c

    def get_nodes(self):  #first create list then change to ndarray
        nodes =[]
        for n in self.nodes:
            nodes.append([n.x, n.y])
        return np.array(nodes)

    def get_lengths(self):
        lengths = np.empty(shape=[0, 1])
        for r in self.rods:
            lengths = np.append(lengths, r.length())
        return lengths

    def read_from_file(self, path):  # TODO - test for any input
        f = open(path, "r")
        for row in f:
            row = row.split(' ')

            if int(row[4]) > len(self.nodes):  # not working with unformatted input - create index temporary table
                self.nodes.append(Node(int(row[0]), int(row[1])))

            if int(row[5]) > len(self.nodes):
                self.nodes.append(Node(int(row[2]), int(row[3])))

            self.rods.append(Rod(self.nodes[int(row[4])-1], self.nodes[int(row[5])-1]))

    def select_rods(self, rods):
        plt.figure(1)

        for r in rods:
            plt.plot([r.n1.x, r.n2.x], [r.n1.y, r.n2.y], color='r', label='selected')

        plt.legend()
        plt.show()


    def plot_lattice(self):
        plt.figure(1)

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
