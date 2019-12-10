from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["primes_cpy.pyx", "primes_py_compile.py", "primes_cpp_py.pyx"])
)
