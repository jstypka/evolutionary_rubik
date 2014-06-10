"""
 F = white = 3
 R = red = 4
 U = blue = 0
 B = yellow = 1
 L = orange = 2
 D = green = 5

faces names:
                U U U
                U U U
                U U U

B B B   L L L   F F F   R R R
B B B   L L L   F F F   R R R
B B B   L L L   F F F   R R R

                D D D
                D D D
                D D D

faces indices:
                0 0 0
                0 0 0
                0 0 0

1 1 1   2 2 2   3 3 3   4 4 4
1 1 1   2 2 2   3 3 3   4 4 4
1 1 1   2 2 2   3 3 3   4 4 4

                5 5 5
                5 5 5
                5 5 5
"""
import random

from cube_solver.mutation import rotate_functions
from cube_solver.enums import Colour


class Cube:
    def __init__(self):
        self.faces = None
        self.fitness = None
        self._reset()

    def _reset(self):
        def face(face_indx):
            return [[Colour(face_indx) for i in range(3)] for j in range(3)]

        self.faces = [face(i) for i in range(6)]
        self.fitness = 0

    def scramble(self, moves=70):
        for i in range(moves):
            random.choice(rotate_functions)(self)
        self.recalculate_fitness()

    def is_solved(self):
        return self.fitness == 0

    def recalculate_fitness(self):
        """
        Out of performance premises cube can be in inconsistent state - it's programmer's responsibility to perform fitness recalculation.
        e.g. Fitness shouldn't be recalculated until scrambling or applying a "magic move" is finished.
        """
        self.fitness = 0

        # q1:
        for face in self.faces:
            for row in face:
                for facelet in row:
                    if facelet != face[1][1]:
                        self.fitness += 1

        # q2 and q3:
        edges_and_corners_coordinates = (
            # ((face_1, row_1, col_1), (face_2, row_2, col_2), ... ,(face_n, row_n, col_n))

            # q2 - edges:
            ((3, 1, 0), (2, 1, 2)),
            ((3, 0, 1), (0, 2, 1)),
            ((3, 1, 2), (4, 1, 0)),
            ((3, 2, 1), (5, 0, 1)),

            ((1, 1, 0), (4, 1, 2)),
            ((1, 0, 1), (0, 0, 1)),
            ((1, 1, 2), (2, 1, 0)),
            ((1, 2, 1), (5, 2, 1)),

            ((0, 1, 0), (2, 0, 1)),
            ((0, 1, 2), (4, 0, 1)),

            ((5, 1, 0), (2, 2, 1)),
            ((5, 1, 2), (4, 2, 1)),

            # q3 - corners:
            ((3, 0, 0), (0, 2, 0), (2, 0, 2)),
            ((3, 0, 2), (0, 2, 2), (4, 0, 0)),
            ((3, 2, 0), (2, 2, 2), (5, 0, 0)),
            ((3, 2, 2), (5, 0, 2), (4, 2, 0)),

            ((1, 0, 0), (0, 0, 2), (4, 0, 2)),
            ((1, 0, 2), (0, 0, 0), (2, 0, 0)),
            ((1, 2, 0), (5, 2, 2), (4, 2, 2)),
            ((1, 2, 2), (2, 2, 0), (5, 2, 0))
        )

        pack_size_to_fitness_increment = {2: 4, 3: 6}
        for coordinates_pack in edges_and_corners_coordinates:
            middles_colours = {self.faces[coordinates[0]][1][1] for coordinates in coordinates_pack}
            facelets_colours = {self.faces[coordinates[0]][coordinates[1]][coordinates[2]] for coordinates in coordinates_pack}

            if middles_colours != facelets_colours:
                self.fitness += pack_size_to_fitness_increment[len(facelets_colours)]

    def __eq__(self, obj):
        return isinstance(obj, Cube) and obj.faces == self.faces

    def __ne__(self, obj):
        return not self == obj

    def readable_string(self):
        '''
         do not name this method as __str__ or __repr__ since it'll screw debugging inside PyCharm
        '''
        s = ''

        def stringify_U_or_D(face):
            nonlocal s
            for row in face:
                s += ' ' * 22
                for facelet in row:
                    s += ("%2s" % str(facelet)) + ' '
                s += '\n'

        stringify_U_or_D(self.faces[0])
        s += '\n'

        for row_idx in range(3):
            for face_idx in range(1, 5):
                for facelet in self.faces[face_idx][row_idx]:
                    s += str(facelet) + ' '
                s += ' ' * 2
            s += '\n'

        s += '\n'
        stringify_U_or_D(self.faces[5])

        return s

    def __str__(self):
        return super(Cube, self).__str__() + (' fitness=%d' % self.fitness)




