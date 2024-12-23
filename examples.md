# Examples

Importing the package:

    >>> import exact_multiset_cover as ec

Input and output to the package are using the numpy array type:

    >>> import numpy as np

This example is explained in README.md
    >>> S = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=np.int32)
    >>> print(ec.get_exact_cover(S))
    [0 2 3]

The numpy type to use is defined in the package for convenience and compatibility:
    >>> from exact_multiset_cover.io import DTYPE_FOR_ARRAY
    >>> T = np.array([[1,0,0,1,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=DTYPE_FOR_ARRAY)
    >>> print(ec.get_exact_cover(T))
    [0 2 3]

It's also possible to retrieve the total number of solutions to an exact cover problem:
    >>> ec.get_solution_count(T)
    1

When a multiset should be covered, its multiplicity function must be provided as a `target` vector.
If no `target` is given, every element is assumed to appear once (as in a normal set).
    >>> S = np.array([[1,1,0,1,0],[0,1,3,0,0],[0,1,1,0,0],[0,0,0,0,1]], dtype=np.int32)
    >>> T = np.array([1,2,3,1,1], dtype=np.int32)
    >>> print(ec.get_exact_cover(S, target=T))
    [0 3 1]
