import Mesh

if __name__ == "__main__":

    mesh = Mesh.Mesh()
    mesh2 = Mesh.Mesh()

    #mesh.read_from_file('lattice_2.txt')
    mesh.read_from_file('lattice_1.txt')

    mesh.plot_lattice()

    global_0 = Mesh.Node(0,0)
    global_x = Mesh.Rod(global_0, Mesh.Node(2,0))

    # mesh.select_rods([global_x])

    #mesh.select_rods([mesh.rods[6], mesh.rods[7]])
    # print(mesh.angle(mesh.rods[6], mesh.rods[7]))

    for r in mesh.rods:
        print(mesh.angle(r))

        print(mesh.angle_matrix(r))


