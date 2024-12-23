import numpy as np

from exact_cover.io import DTYPE_FOR_ARRAY

# one specific problem that I had trouble with
# originally based on solving the trivial problem
# of arranging 2 identical triminos on a 3x3 board

#    +--+
#    |  |
# +--+--+
# |  |  |
# +--+--+

# +--+--+--+
# |xx|  |xx|
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |xx|  |  |
# +--+--+--+


# this problem has 2 solutions
# (5, 13) and (6, 12)
def small_trimino_problem():
    to_cover = [
        [1, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0],  # <- 5
        [1, 0, 0, 0, 0, 1, 1, 1],  # <- 6
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 0, 0],  # <- 12
        [0, 1, 0, 0, 0, 1, 1, 1],  # <- 13
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solution1=[5, 13],
        solution_count=2,
        all_solutions=[
            {5, 13},
            {6, 12},
        ],
    )


def small_trimino_problem_from_file():
    return dict(
        data=np.load("tests/files/small_trimino_problem.npy"),
        solution1=[5, 13],
        solution_count=2,
        all_solutions=[
            {5, 13},
            {6, 12},
        ],
    )


# https://en.wikipedia.org/wiki/Exact_cover#Detailed_example
def detailed_wikipedia_problem():
    sets = [
        {1, 4, 7},
        {1, 4},  # <- 1
        {4, 5, 7},
        {3, 5, 6},  # <- 3
        {2, 3, 6, 7},
        {2, 7},  # <- 5
    ]
    return dict(
        data=np.array(
            [[1 if i in s else 0 for i in range(1, 8)] for s in sets],
            dtype=DTYPE_FOR_ARRAY,
        ),
        solution1=[1, 3, 5],
        solution_count=1,
        all_solutions=[
            {1, 3, 5},
        ],
    )


def bruteforce_problem1():
    to_cover = [
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 1, 2],
        solution_count=2,
        all_solutions=[
            {0, 1, 2},
            {3, 4, 5},
        ],
    )


def bruteforce_problem2():
    to_cover = [
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 1, 2],
        solution_count=9,
        all_solutions=[
            {0, 1, 2},
            {0, 1, 8},
            {0, 2, 7},
            {0, 7, 8},
            {1, 2, 6},
            {1, 6, 8},
            {2, 6, 7},
            {3, 4, 5},
            {6, 7, 8},
        ],
    )


def bruteforce_problem3():
    to_cover = [
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
        [1, 0, 0, 1, 0, 0, 1, 0],  # <- sol1
        [0, 1, 0, 0, 1, 0, 0, 1],  # <- sol1
        [0, 0, 1, 0, 0, 1, 0, 0],  # <- sol1
        [0, 0, 0, 1, 0, 0, 0, 0],  # <- sol2
        [1, 0, 1, 0, 1, 0, 0, 1],  # <- sol2
        [0, 1, 0, 0, 0, 1, 1, 0],  # <- sol2
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 1, 2],
        solution_count=16,
        all_solutions=[
            {0, 1, 2},
            {0, 1, 8},
            {0, 2, 7},
            {0, 7, 8},
            {1, 2, 6},
            {1, 6, 8},
            {2, 6, 7},
            {3, 4, 5},
            {3, 4, 11},
            {3, 5, 10},
            {3, 10, 11},
            {4, 5, 9},
            {4, 9, 11},
            {5, 9, 10},
            {6, 7, 8},
            {9, 10, 11},
        ],
    )

def trailing_zero_row_problem():
    tc = (
        (1, 1, 0),
        (1, 0, 1),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
    )
    return dict(
        data=np.array(tc, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 1, 2],
        solution_count=8,
        all_solutions=[
            {9, 10},
            {7, 4},
            {2, 10},
            {7, 11, 10},
            {7, 3},
            {7, 0},
            {1, 10},
            {7, 8},

def trivial_multiset_problem():
    multiset = [1, 1, 2]
    rows = [
        [1, 1, 2],
        [2, 2, 2],
    ]

    return dict(
        data=np.array(rows, dtype=DTYPE_FOR_ARRAY),
        target=np.array(multiset, dtype=DTYPE_FOR_ARRAY),
        solution1=[0],
        solution_count=1,
        all_solutions=[
            {0}
        ],
    )

def rows_are_normal_sets_multiset_problem():
    multiset = [1, 2, 2]
    rows = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 0, 1],
        [0, 1, 1],
    ]

    return dict(
        data=np.array(rows, dtype=DTYPE_FOR_ARRAY),
        target=np.array(multiset, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 2, 3],
        solution_count=2,
        all_solutions=[
            {0, 2, 3},
            {1, 3}
        ],
    )

def every_row_matches_column_multiplicity_multiset_problem():
    multiset = [2, 3, 4]
    rows = [
        [2, 0, 4],
        [2, 3, 0],
        [0, 3, 0],
        [0, 0, 4],
    ]

    return dict(
        data=np.array(rows, dtype=DTYPE_FOR_ARRAY),
        target=np.array(multiset, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 2],
        solution_count=2,
        all_solutions=[
            {0, 2},
            {1, 3}
        ],
    )

def small_multiset_problem():
    multiset = [1, 2, 3]
    rows = [
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 2],
        [0, 1, 3],
        [0, 1, 0]
    ]

    return dict(
        data=np.array(rows, dtype=DTYPE_FOR_ARRAY),
        target=np.array(multiset, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 1, 2],
        solution_count=2,
        all_solutions=[
            {0, 1, 2},
            {1, 3, 4}
        ],
    )

def small_multiset_problem_with_equal_rows():
    multiset = [2, 2]
    rows = [
        [1, 1],
        [1, 1],
    ]

    return dict(
        data=np.array(rows, dtype=DTYPE_FOR_ARRAY),
        target=np.array(multiset, dtype=DTYPE_FOR_ARRAY),
        solution1=[0, 1],
        solution_count=1,
        all_solutions=[
            {0, 1},
        ],
    )
    
def small_multiset_problem_with_row_exceeding_column_multiplicity():
    multiset = [1, 1, 2]
    rows = [
        [1, 0, 3],
        [1, 1, 2],
        [0, 2, 0],
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 1]
    ]

    return dict(
        data=np.array(rows, dtype=DTYPE_FOR_ARRAY),
        target=np.array(multiset, dtype=DTYPE_FOR_ARRAY),
        solution1=[1],
        solution_count=2,
        all_solutions=[
            {1},
            {4, 5}
        ],
    )
