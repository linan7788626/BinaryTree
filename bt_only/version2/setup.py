# run python setup.py build_ext
#  in order to build cpp files from the pyx files

import os

import numpy

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

for extension in ["tree_utils", "dist_metrics", "typedefs"]:
    setup(cmdclass = {'build_ext': build_ext},
          name=extension,
          version='1.0',
          ext_modules=[Extension(extension,
                                 [extension + ".pyx"])],
          include_dirs=[numpy.get_include(),
                        os.path.join(numpy.get_include(), 'numpy')]
          )