import Mesh

if __name__ == "__main__":

    mesh = Mesh.Mesh()

    mesh.read_from_file('lattice_1.txt')

    mesh.plot_lattice()
