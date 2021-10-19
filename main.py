import Mesh

if __name__ == "__main__":

    mesh = Mesh.Mesh()

    mesh.read_from_file('lattice_2.txt')

    mesh.plot_lattice()

    mesh.select_rods([mesh.rods[6], mesh.rods[7]])
    print(mesh.angle(mesh.rods[6], mesh.rods[7]))

