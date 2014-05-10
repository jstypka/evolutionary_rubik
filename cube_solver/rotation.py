from cube_solver.enums import Edge
from cube_solver.utils import rotate_face, cycle_4


def _F(cube, clockwise=True):
    rotate_face(cube.faces[3], clockwise)
    cycle_4(
        faces=[cube.faces[i] for i in [2, 0, 4, 5]],
        edges=[Edge.RIGHT(ascending_indices=False), Edge.BOTTOM(), Edge.LEFT(), Edge.TOP(ascending_indices=False)],
        clockwise=clockwise
    )


def _R(cube, clockwise=True):
    rotate_face(cube.faces[4], clockwise)
    cycle_4(
        faces=[cube.faces[i] for i in [3, 0, 1, 5]],
        edges=[Edge.RIGHT(ascending_indices=False), Edge.RIGHT(ascending_indices=False), Edge.LEFT(), Edge.RIGHT(ascending_indices=False)],
        clockwise=clockwise
    )


def _U(cube, clockwise=True):
    rotate_face(cube.faces[0], clockwise)
    cycle_4(
        faces=[cube.faces[i] for i in [2, 1, 4, 3]],
        edges=[Edge.TOP(ascending_indices=False), Edge.TOP(ascending_indices=False), Edge.TOP(ascending_indices=False), Edge.TOP(ascending_indices=False)],
        clockwise=clockwise
    )


def _B(cube, clockwise=True):
    rotate_face(cube.faces[1], clockwise)
    cycle_4(
        faces=[cube.faces[i] for i in [2, 5, 4, 0]],
        edges=[Edge.LEFT(), Edge.BOTTOM(), Edge.RIGHT(ascending_indices=False), Edge.TOP(ascending_indices=False)],
        clockwise=clockwise
    )


def _L(cube, clockwise=True):
    rotate_face(cube.faces[2], clockwise)
    cycle_4(
        faces=[cube.faces[i] for i in [3, 5, 1, 0]],
        edges=[Edge.LEFT(), Edge.LEFT(), Edge.RIGHT(ascending_indices=False), Edge.LEFT()],
        clockwise=clockwise
    )


def _D(cube, clockwise=True):
    rotate_face(cube.faces[5], clockwise)
    cycle_4(
        faces=[cube.faces[i] for i in [3, 4, 1, 2]],
        edges=[Edge.BOTTOM(), Edge.BOTTOM(), Edge.BOTTOM(), Edge.BOTTOM()],
        clockwise=clockwise
    )


# TODO(vucalur): refactor error-prone copy-paste. OCaml high order functions would be handy ...
def F(cube):
    _F(cube)


def Fi(cube):
    _F(cube, clockwise=False)


def R(cube):
    _R(cube)


def Ri(cube):
    _R(cube, clockwise=False)


def U(cube):
    _U(cube)


def Ui(cube):
    _U(cube, clockwise=False)


def B(cube):
    _B(cube)


def Bi(cube):
    _B(cube, clockwise=False)


def L(cube):
    _L(cube)


def Li(cube):
    _L(cube, clockwise=False)


def D(cube):
    _D(cube)


def Di(cube):
    _D(cube, clockwise=False)

