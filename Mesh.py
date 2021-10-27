import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pi


# TODO - move classes to separeate files and move methods (e.g. - length and vector to rod classs)

class Mesh:

    def __init__(self):
        self.nodes = [] # store as a datframe with columns: index and node or see read_from_file_method
        self.rods = []

        self.A = 1
        self.E = 1


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

    def orient_nodes(self, r):  # TODO implement in rod class
        if r.n1.x < r.n2.x:
            return [r.n1, r.n2]
        else:
            return [r.n2, r.n1]

    def angle(self, r):  # TODO can be made a abstarct class and inherited to cosine and sine
        l = self.length(r.n1, r.n2)
        left_n, right_n = self.orient_nodes(r)

        print(f"left x: {left_n.x}, right x: {right_n.x}")
        print(f"left y: {left_n.y}, right y: {right_n.y}")

        return [(right_n.y - left_n.y)/l, (right_n.x - left_n.x)/l]  # sine, cosine

    def angle_matrix(self, r):
        result = np.zeros([4, 4])
        result[0,0] = self.angle(r)[1]
        result[1,1] = self.angle(r)[1]
        result[2,2] = self.angle(r)[1]
        result[3,3] = self.angle(r)[1]  # TODO dont call everytime  - create variable
        result[0,1] = self.angle(r)[0]
        result[2,3] = self.angle(r)[0]
        result[1,0]= -self.angle(r)[0]
        result[3,2] = -self.angle(r)[0]  # TODO unpacking variables in numpy

        return result

    def get_nodes(self):  #first create list then change to ndarray
        #nodes = np.empty(shape=[0, 1])
        nodes =[]
        for n in self.nodes:
            nodes.append([n.x, n.y])
            #nodes = np.append(nodes, [n.x, n.y], axis=0)
        return np.array(nodes)

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