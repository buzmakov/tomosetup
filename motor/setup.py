from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("ximc_wrapper",
              sources=["ximc_wrapper.pyx"],
              libraries=["libximc"] # Unix-like specific
    )
]

setup(
  name = "ximc_wrapper",
  ext_modules = cythonize(ext_modules)
)