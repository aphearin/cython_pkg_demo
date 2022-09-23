# cython_pkg_demo

## Installation
To install cython_pkg_demo into your environment from the source code:

```
$ cd /path/to/root/cython_pkg_demo
$ python setup.py install
```

## Testing
To run the suite of unit tests:

```
$ cd /path/to/root/cython_pkg_demo
$ pytest
```

To build html of test coverage:

```
$ pytest -v --cov --cov-report html
$ open htmlcov/index.html
```

