from copy import deepcopy


def rotate_face(face, clockwise=True):
    old_face = deepcopy(face)
    for i in range(3):
        for j in range(3):
            if clockwise:
                face[j][i] = old_face[2 - i][j]
            else:
                face[j][i] = old_face[i][2 - j]


def _cycle_4_cw(*, faces, edges):
    old_last_face = deepcopy(faces[3])
    for i in range(3, -1, -1):
        face, edge, edge_prev = faces[i], edges[i], edges[i - 1 % len(edges)]
        face_prev = faces[i - 1] if i > 0 else old_last_face
        for j in range(3):
            face[edge(j)[0]][edge(j)[1]] = face_prev[edge_prev(j)[0]][edge_prev(j)[1]]


def _cycle_4_ccw(*, faces, edges):
    old_first_face = deepcopy(faces[0])
    for i in range(4):
        face, edge, edge_next = faces[i], edges[i], edges[(i + 1) % len(edges)]
        face_next = faces[i + 1] if i < 3 else old_first_face
        for j in range(3):
            face[edge(j)[0]][edge(j)[1]] = face_next[edge_next(j)[0]][edge_next(j)[1]]


def cycle_4(*, faces, edges, clockwise=True):
    if clockwise:
        _cycle_4_cw(faces=faces, edges=edges)
    else:
        _cycle_4_ccw(faces=faces, edges=edges)

