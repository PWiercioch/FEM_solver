import Mesh
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    mesh_static = Mesh.StaticAnalysis()
    mesh_static.read_mesh_from_file('lattice_2.txt')

    mesh_static.set_boundary_conditions([1, 4, 11])
    force = np.array([[0],[0],[0],[0],[0],[0],[0],[-2e5],[0],[0],[0],[0]])
    static_result = mesh_static.solve(force)

    mesh_modal = Mesh.ModalAnalysis()
    mesh_modal.read_mesh_from_mesh(mesh_static)

    mesh_modal.set_boundary_conditions([1, 4, 11])
    modal_result = mesh_modal.solve()

    plt.figure()
    mesh_static.plot_lattice()
    mesh_static.plot_solved(static_result, factor=500)

    plt.figure()
    mesh_static.plot_lattice()
