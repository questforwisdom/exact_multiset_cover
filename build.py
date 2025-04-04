from setuptools import Extension

import numpy


# define the extension module
src_dir = "src/"
exact_multiset_cover_impl = Extension(
    "exact_multiset_cover_impl",
    sources=[
        src_dir + "exact_cover.c",
        src_dir + "dlx.c",
        src_dir + "sparse_matrix.c",
        src_dir + "quad_linked_list.c",
    ],
    include_dirs=[src_dir, numpy.get_include()],
)


def build(setup_kwargs):
    setup_kwargs.update(
        {
            # Doubtful that we need to specify packages here?
            # Poetry could probably get this right using pyproject.toml
            "packages": ["exact_multiset_cover"],
            "ext_modules": [exact_multiset_cover_impl],
        }
    )
