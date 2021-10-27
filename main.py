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

    mesh.get_stiffnes_matrix()

    for r in mesh.rods:
        print(f"node one: {mesh.nodes.index(r.n1)}, node two: {mesh.nodes.index(r.n2)}")
        stif = mesh.get_stiffnes(r)

        # TODO - i na loop

        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n1)] = stif[0,0]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n2), mesh.nodes.index(r.n1)] = stif[0,1]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n2), mesh.nodes.index(r.n1)] = stif[0,2]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n1)] = stif[0,3]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n1)] = stif[1,0]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n2), mesh.nodes.index(r.n1)] = stif[1,1]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n2), mesh.nodes.index(r.n1)] = stif[1,2]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n2)] = stif[1,3]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n2)] = stif[2,0]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n2), mesh.nodes.index(r.n2)] = stif[2,1]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n2), mesh.nodes.index(r.n2)] = stif[2,2]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n2)] = stif[2,3]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n2)] = stif[3,0]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n1)] = stif[3,1]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n1)] = stif[3,2]
        mesh.stiffnes_matrix[mesh.nodes.index(r.n1), mesh.nodes.index(r.n1)] = stif[3,3]

        print(mesh.stiffnes_matrix)



