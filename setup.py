import os
from setuptools import setup, find_packages, Extension
import numpy as np

PACKAGENAME = "cython_pkg_demo"
__version__ = None
pth = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "cython_pkg_demo", "_version.py"
)
with open(pth, "r") as fp:
    exec(fp.read())


ext_names = (
    "cython_pkg_demo.cython_kernels.elementwise_add_cython",
    "cython_pkg_demo.cython_kernels.elementwise_subtract_cython",
)

ext_sources = (
    "cython_pkg_demo/cython_kernels/elementwise_add_cython.pyx",
    "cython_pkg_demo/cython_kernels/elementwise_subtract_cython.pyx",
)


def get_extensions(names, sources):

    language = "c++"
    extra_compile_args = ["-Ofast"]

    extensions = []
    for name, source in zip(names, sources):
        extensions.append(
            Extension(
                name=name,
                sources=[source],
                include_dirs=np.get_include(),
                language=language,
                extra_compile_args=extra_compile_args,
            )
        )

    return extensions


setup(
    name=PACKAGENAME,
    version=__version__,
    author="Andrew Hearin",
    author_email="ahearin@anl.gov",
    description="Some package",
    long_description="Just some package",
    install_requires=["numpy", "cython"],
    ext_modules=get_extensions(ext_names, ext_sources),
    packages=find_packages(),
    url="https://github.com/aphearin/cython_pkg_demo",
    package_data={"cython_pkg_demo": ("tests/testing_data/*.dat",)},
)
