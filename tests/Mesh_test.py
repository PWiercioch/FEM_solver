from Mesh import Mesh, Node

def test_length():
    mesh = Mesh()

    n1 = Node(0,0)
    n2 = Node(0,0)

    assert mesh.length(n1,n2) == 0