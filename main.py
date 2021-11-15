import StaticAnalysis, ModalAnalysis
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    mesh_static = StaticAnalysis.StaticAnalysis()
    mesh_static.read_mesh_from_file('lattice_2.txt')

    mesh_static.boundary_conditions = [1, 4, 11]
    force = np.array([[0],[0],[0],[0],[0],[0],[0],[-2e5],[0],[0],[0],[0]])
    static_displacement = mesh_static.solve(force)

    mesh_modal = ModalAnalysis.ModalAnalysis()
    mesh_modal.read_mesh_from_mesh(mesh_static)

    mesh_modal.boundary_conditions = [1, 4, 11]
    frequencies, modal_displacement = mesh_modal.solve()

    plt.figure()
    mesh_static.plot_lattice()
    mesh_static.plot_solved(static_displacement, factor=500)

    mesh_modal.plot_frequencies(modal_displacement, factor=10)
