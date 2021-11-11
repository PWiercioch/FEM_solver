import Mesh

if __name__ == "__main__":

    mesh = Mesh.Mesh()
    mesh2 = Mesh.Mesh()

    #mesh.read_from_file('lattice_2.txt')
    mesh.read_from_file('lattice_3.txt')

    mesh.plot_lattice()

    mesh.get_stiffnes_matrix()
