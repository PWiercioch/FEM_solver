import Mesh

if __name__ == "__main__":

    mesh = Mesh.Mesh()
    mesh2 = Mesh.Mesh()

    #mesh.read_from_file('lattice_2.txt')
    mesh.read_from_file('lattice_3.txt')

    mesh.plot_lattice()

    mesh.get_stiffnes_matrix()

    '''
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
    '''

    import numpy as  np
    result = np.zeros([len(mesh.nodes)*2, len(mesh.nodes)*2])
    for rod in mesh.rods:
        stiff = mesh.get_stiffnes(rod)
        print(stiff)
        for id, row in enumerate(rod.get_nodes()):

            if id % 2 != 0:
                odd = 1
            else:
                odd = 0

            n1_id = mesh.nodes.index(rod.n1)
            n2_id = mesh.nodes.index(rod.n2)

            if mesh.nodes.index(row) == n2_id:
                multiply = 24
            else:
                multiply = 1

            result[mesh.nodes.index(rod.n1), multiply * mesh.nodes.index(row)+odd] = stiff[0, id]
            result[mesh.nodes.index(rod.n1) + 1, multiply * mesh.nodes.index(row)+odd] = stiff[1, id]
            result[2 * mesh.nodes.index(rod.n2), multiply*mesh.nodes.index(row)+odd] = stiff[2, id]
            result[2 * mesh.nodes.index(rod.n2) + 1, multiply*mesh.nodes.index(row)+odd] = stiff[3, id]
            '''
            result[col -> n1.x_index, row_index] = row[0]
            result[col -> n1.y_index, row_index] = row[1]
            result[col -> n2.x_index, row_index] = row[2]
            result[col -> n2.y_index, row_index] = row[3]
            '''

            '''
            for item in row:
                print(f"row: {row}, col: {item}")
            '''