import os
from setuptools import setup, find_packages
from Cython.Build import cythonize

PACKAGENAME = "cython_pkg_demo"
__version__ = None
pth = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "cython_pkg_demo", "_version.py"
)
with open(pth, "r") as fp:
    exec(fp.read())


setup(
    name=PACKAGENAME,
    version=__version__,
    author="Andrew Hearin",
    author_email="ahearin@anl.gov",
    description="Some package",
    long_description="Just some package",
    install_requires=["numpy", "cython"],
    ext_modules=cythonize("cython_pkg_demo/cython_kernels/elementwise_add_cython.pyx"),
    packages=find_packages(),
    url="https://github.com/aphearin/cython_pkg_demo",
    package_data={"cython_pkg_demo": ("tests/testing_data/*.dat",)},
)
