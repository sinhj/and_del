from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("compile_pyd_test.py"))
