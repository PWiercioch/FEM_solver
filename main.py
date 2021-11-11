import Mesh
import numpy as np

if __name__ == "__main__":

    mesh = Mesh.Mesh()

    mesh.read_from_file('lattice_2.txt')

    mesh.plot_lattice()

    mesh.get_stiffnes_matrix()

    mesh.set_boundary_conditions([1, 4, 11])

    force = np.array([[0],[0],[0],[0],[0],[0],[0],[-2e5],[0],[0],[0],[0]])

    result = mesh.solve(force)
