def test():
    print "g9fxwor;"



'''
# 嵌入式版本不支持 Cpython
1. pip install Cython --install-option="--no-cython-compile"

2. require Visual C++ 9.0 Compiler for Python
"VCForPython27.msi"

3. 新建 setup.py
"setup.py" << END
from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("compile_pyd_test.py"))
END

4. python setup.py build_ext (--inplace) clean
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  upload            upload binary package to PyPI
  check             perform some checks on the package
 
Extra commands:
  rotate            delete older distributions, keeping N newest files
  develop           install package in 'development mode'
  setopt            set an option in setup.cfg or another config file
  saveopts          save supplied options to setup.cfg or other config file
  egg_info          create a distribution's .egg-info directory
  install_egg_info  Install an .egg-info directory for the package
  alias             define a shortcut to invoke one or more commands
  easy_install      Find/get/install Python packages
  bdist_egg         create an "egg" distribution
  test              run unit tests after in-place build
'''
