## Boost.Build makes it easy to build C++ projects, everywhere

[![Build Status](https://travis-ci.org/bincrafters/conan-boost-build.svg?branch=testing%2F1.65.1)](https://travis-ci.org/bincrafters/conan-boost-build)
[![Build status](https://ci.appveyor.com/api/projects/status/v5iuw7v9rlse9chp/branch/master?svg=true)](https://ci.appveyor.com/project/BinCrafters/conan-boost-build/branch/testing%2F1.65.1)

[Conan.io](https://conan.io) package for [Boost.Build](https://github.com/boostorg/build) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/conan-public/Boost.Build%3Abincrafters).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload Boost.Build/1.65.1@bincrafters/testing --all

## Reuse the packages

### Basic setup

    $ conan install Boost.Build/1.65.1@bincrafters/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Build/1.65.1@bincrafters/testing

    [generators]
    txt

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* with all the paths and variables that you need to link with your dependencies.

### License
[Boost](LICENSE)
