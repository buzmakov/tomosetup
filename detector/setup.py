from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("xiApi",
              sources=["xiApi.pyx"],
              libraries=["m3apiX64"] # Unix-like specific
    )
]

setup(
  name = "xiApi",
  ext_modules = cythonize(ext_modules)
)