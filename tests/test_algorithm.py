from cube_solver.algorithm import compressed


def test_compressed():
    uncompressed = ['L', 'L', 'B', 'Bi', 'Li', 'Ui', 'U', 'R']
    expected = ['L', 'R']

    assert compressed(uncompressed) == expected


def test_compressed2():
    uncompressed = ['R', 'Ri']
    expected = []

    assert compressed(uncompressed) == expected


def test_compressed3():
    uncompressed = ['Ri', 'Ri']
    expected = ['Ri', 'Ri']

    assert compressed(uncompressed) == expected
