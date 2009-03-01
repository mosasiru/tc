#!/usr/bin/env python
import sys
from distutils.core import setup, Extension

if sys.version_info < (2, 3):
  raise Error, "Python 2.3 or later is required"

include_dirs = []
library_dirs = ['/usr/local/lib']

# Add search directories for Mac OS X
if sys.platform == 'darwin':
  # MacPorts
  include_dirs.append('/opt/local/include')
  library_dirs.append('/opt/local/lib')
  # Fink
  include_dirs.append('/sw/include')
  library_dirs.append('/sw/lib')

# Undefine macros
undef_macros=[]
if '--debug' in sys.argv or '--debug-smisk' in sys.argv:
  undef_macros=['NDEBUG']

# C extension
ext = Extension('_pytc',
                libraries = ['tokyocabinet'],
                sources = ['src/pytc.c'],
                include_dirs = include_dirs,
                library_dirs = library_dirs,
                undef_macros = undef_macros
               )

# Package
setup(name = 'pytc',
      version = '0.7',
      description = 'Tokyo Cabinet Python bindings',
      long_description = '''
      Tokyo Cabinet Python bindings
      ''',
      license='BSD',
      author = 'Tasuku SUENAGA',
      author_email = 'gunyarakun@sourceforge.jp',
      ext_modules = [ext],
      package_dir = {'': 'lib'},
      packages = ['pytc']
     )
