import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pi


# TODO - move classes to separeate files and move methods (e.g. - length and vector to rod classs)

class Mesh:

    def __init__(self):
        self.nodes = [] # store as a datframe with columns: index and node or see read_from_file_method
        self.rods = []

    def determinability(self):  # TODO
        pass

    def length(self, n1, n2):  # TODO calculate from vector and use in angle method
        return sqrt((n2.x - n1.x)**2 + (n2.y - n1.y)**2)

    def vector(self, n1, n2):
        return np.array([n2.x-n1.x, n2.y-n1.y])

    def common_node(self, r1, r2):
        if r1.n1 == r2.n1:
            return r1.n1
        elif r1.n1 == r2.n2:
            return r1.n1
        else:
            return r1.n2

    def angle(self, r1, r2):
        c_n = self.common_node(r1, r2)

        if c_n != r1.n2:
            v1 = self.vector(c_n, r1.n2)
        else:
            v1 = self.vector(c_n, r1.n1)

        if c_n != r2.n2:
            v2 = self.vector(c_n, r2.n2)
        else:
            v2 = self.vector(c_n, r2.n1)

        return np.arccos((v1[0]*v2[0] + v1[1]*v2[1]) / (self.length(r1.n1,r1.n2) * self.length(r2.n1,r2.n2))) * 180/pi

    def get_nodes(self):
        nodes = np.empty(shape=[0, 2])
        for n in self.nodes:
            nodes = np.append(nodes, [n.x, n.y], axis=0)
        return nodes

    def get_lengths(self):
        lengths = np.empty(shape=[0, 1])
        for r in self.rods:
            lengths = np.append(lengths, self.length(r.n1, r.n2))  # TODO accept rod as argument
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


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rod:

    def __init__(self, n1: Node, n2: Node):
        self.n1 = n1
        self.n2 = n2