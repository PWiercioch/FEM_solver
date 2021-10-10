import matplotlib.pyplot as plt

class Mesh:

    def __init__(self):
        self.nodes = []
        self.rods = []

    def read_from_file(self, path):
        f = open(path, "r")
        for row in f:
            row = row.split(' ')

            if int(row[4]) > len(self.nodes):
                self.nodes.append(Node(int(row[0]), int(row[1])))

            if int(row[5]) > len(self.nodes):
                self.nodes.append(Node(int(row[2]), int(row[3])))

            self.rods.append(Rod(self.nodes[int(row[4])-1], self.nodes[int(row[5])-1]))

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