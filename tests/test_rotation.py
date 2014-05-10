from cube_solver.cube import Cube
from cube_solver.rotation import F, D, L, B, U, R, Di, Li, Bi, Ui, Ri, Fi


def test_4_turn():
    rotations = [F, R, U, B, L, D,
                 Fi, Ri, Ui, Bi, Li, Di]
    for rotation in rotations:
        c = Cube()
        for i in range(4):
            rotation(c)
        fresh_one = Cube()
        assert c == fresh_one


def _assert_rotate(fresh_visually, expected_visually, rotation_fun):
    def faces_visually_to_faces(faces_visually):
        row0_indices = (0, 9, 12, 15, 18, 45)
        next_row_indices_shift = (3, 12, 12, 12, 12, 3)

        def facelet_value(face_idx, row_idx, col_idx):
            index = row0_indices[face_idx] + next_row_indices_shift[face_idx] * row_idx + col_idx
            return faces_visually[index]

        faces = [[[facelet_value(face_idx, row_idx, col_idx)
                   for col_idx in range(3)]
                  for row_idx in range(3)]
                 for face_idx in range(6)]

        return faces

    fresh = Cube()
    expected = Cube()
    fresh.faces = faces_visually_to_faces(fresh_visually)
    expected.faces = faces_visually_to_faces(expected_visually)
    rotation_fun(fresh)

    print("actual:\n" + fresh.readable_string())
    print("expected:\n" + expected.readable_string())

    # more useful for debugging than: assert fresh == expected :
    assert fresh.faces == expected.faces


def test_F():
    fresh_visually = [    1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    expected_visually = [ 1, 2, 3,
                          4, 5, 6,
                          27,24,21,

    10,11,12,  19,20,46,  34,31,28,  7,38,39,
    13,14,15,  22,23,47,  35,32,29,  8,41,42,
    16,17,18,  25,26,48,  36,33,30,  9,44,45,

                          43,40,37,
                          49,50,51,
                          52,53,54]

    _assert_rotate(fresh_visually, expected_visually, F)


def test_R():
    fresh_visually = [    1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    expected_visually = [ 1, 2, 30,
                          4, 5, 33,
                          7, 8, 36,

    9, 11,12,  19,20,21,  28,29,48,  43,40,37,
    6, 14,15,  22,23,24,  31,32,51,  44,41,38,
    3, 17,18,  25,26,27,  34,35,54,  45,42,39,

                          46,47,16,
                          49,50,13,
                          52,53,10]

    _assert_rotate(fresh_visually, expected_visually, R)


def test_U():
    fresh_visually = [    1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    expected_visually = [ 7, 4, 1,
                          8, 5, 2,
                          9, 6, 3,

    19,20,21,  28,29,30,  37,38,39,  10,11,12,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    _assert_rotate(fresh_visually, expected_visually, U)


def test_B():
    fresh_visually = [    1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    expected_visually = [ 39,42,45,
                          4, 5, 6,
                          7, 8, 9,

    16,13,10,  3, 20,21,  28,29,30,  37,38,54,
    17,14,11,  2, 23,24,  31,32,33,  40,41,53,
    18,15,12,  1, 26,27,  34,35,36,  43,44,52,

                          46,47,48,
                          49,50,51,
                          19,22,25]

    _assert_rotate(fresh_visually, expected_visually, B)


def test_L():
    fresh_visually = [    1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    expected_visually = [ 18,2, 3,
                          15,5, 6,
                          12,8, 9,

    10,11,52,  25,22,19,  1, 29,30,  37,38,39,
    13,14,49,  26,23,20,  4, 32,33,  40,41,42,
    16,17,46,  27,24,21,  7, 35,36,  43,44,45,

                          28,47,48,
                          31,50,51,
                          34,53,54]

    _assert_rotate(fresh_visually, expected_visually, L)


def test_D():
    fresh_visually = [    1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    16,17,18,  25,26,27,  34,35,36,  43,44,45,

                          46,47,48,
                          49,50,51,
                          52,53,54]

    expected_visually = [ 1, 2, 3,
                          4, 5, 6,
                          7, 8, 9,

    10,11,12,  19,20,21,  28,29,30,  37,38,39,
    13,14,15,  22,23,24,  31,32,33,  40,41,42,
    43,44,45,  16,17,18,  25,26,27,  34,35,36,

                          52,49,46,
                          53,50,47,
                          54,51,48]

    _assert_rotate(fresh_visually, expected_visually, D)
