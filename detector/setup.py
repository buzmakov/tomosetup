from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import numpy

ext_modules=[
    Extension("xiApi",
              sources=["xiApi.pyx"],
              libraries=["m3apiX64"], # Unix-like specific
              include_dirs=[numpy.get_include()]
    )
]

setup(
  name = "xiApi",
  ext_modules = cythonize(ext_modules)
)