from cube_solver.enums import Edge
from cube_solver.utils import rotate_face, cycle_4


A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'
I = 'I'
J = 'J'
K = 'K'
L = 'L'
M = 'M'
N = 'N'
O = 'O'
P = 'P'
Q = 'Q'
R = 'R'
S = 'S'
T = 'T'
U = 'U'
V = 'V'
W = 'W'
X = 'X'
Y = 'Y'
Z = 'Z'

A2 = 'A2'
B2 = 'B2'
C2 = 'C2'
D2 = 'D2'
E2 = 'E2'
F2 = 'F2'
G2 = 'G2'
H2 = 'H2'
I2 = 'I2'
J2 = 'J2'
K2 = 'K2'
L2 = 'L2'
M2 = 'M2'
N2 = 'N2'
O2 = 'O2'
P2 = 'P2'
Q2 = 'Q2'
R2 = 'R2'
S2 = 'S2'
T2 = 'T2'
U2 = 'U2'
V2 = 'V2'
W2 = 'W2'
X2 = 'X2'
Y2 = 'Y2'
Z2 = 'Z2'


def test_rotate_face_cw():
    face = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    expected_rotated_face = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    rotate_face(face, clockwise=True)
    assert expected_rotated_face == face


def test_rotate_face_ccw():
    face = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    expected_rotated_face = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]

    rotate_face(face, clockwise=False)
    assert expected_rotated_face == face


def test_cycle_4_cw_1():
    """
    See `cube_solver.cube`
    faces: 2, 0, 4, 5
    """
    faces = [[
                 [A, B, C],
                 [D, E, F],
                 [G, H, I]
             ], [
                 [J, K, L],
                 [M, N, O],
                 [P, Q, R]
             ], [
                 [S, T, U],
                 [V, W, X],
                 [Y, Z, Z2]
             ], [
                 [A2, B2, C2],
                 [D2, E2, F2],
                 [G2, H2, I2]
             ]]

    edges = [Edge.RIGHT(ascending_indices=False), Edge.BOTTOM(), Edge.LEFT(), Edge.TOP(ascending_indices=False)]
    expected_cycled_faces = [[
                                 [A, B, A2],
                                 [D, E, B2],
                                 [G, H, C2]
                             ], [
                                 [J, K, L],
                                 [M, N, O],
                                 [I, F, C]
                             ], [
                                 [P, T, U],
                                 [Q, W, X],
                                 [R, Z, Z2]
                             ], [
                                 [Y, V, S],
                                 [D2, E2, F2],
                                 [G2, H2, I2]
                             ]]

    cycle_4(faces=faces, edges=edges, clockwise=True)
    assert expected_cycled_faces == faces


def test_cycle_4_ccw_1():
    """
    See `cube_solver.cube`
    faces: 2, 0, 4, 5
    """
    faces = [[
                 [A, B, C],
                 [D, E, F],
                 [G, H, I]
             ], [
                 [J, K, L],
                 [M, N, O],
                 [P, Q, R]
             ], [
                 [S, T, U],
                 [V, W, X],
                 [Y, Z, Z2]
             ], [
                 [A2, B2, C2],
                 [D2, E2, F2],
                 [G2, H2, I2]
             ]]

    edges = [Edge.RIGHT(ascending_indices=False), Edge.BOTTOM(), Edge.LEFT(), Edge.TOP(ascending_indices=False)]
    expected_cycled_faces = [[
                                 [A, B, R],
                                 [D, E, Q],
                                 [G, H, P]
                             ], [
                                 [J, K, L],
                                 [M, N, O],
                                 [S, V, Y]
                             ], [
                                 [C2, T, U],
                                 [B2, W, X],
                                 [A2, Z, Z2]
                             ], [
                                 [C, F, I],
                                 [D2, E2, F2],
                                 [G2, H2, I2]
                             ]]

    cycle_4(faces=faces, edges=edges, clockwise=False)
    assert expected_cycled_faces == faces

