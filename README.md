## Boost.Build makes it easy to build C++ projects, everywhere.

[![Build status](https://ci.appveyor.com/api/projects/status/v5iuw7v9rlse9chp/branch/stable/1.65.1?svg=true)](https://ci.appveyor.com/project/BinCrafters/conan-boost-build/branch/stable/1.65.1)
[![Travis Status](https://travis-ci.org/bincrafters/conan-boost-build.svg?branch=stable%2F1.65.1)](https://travis-ci.org/bincrafters/conan-boost-build)
[![Download](https://api.bintray.com/packages/bincrafters/public-conan/Boost.Build%3Abincrafters/images/download.svg?version=1.65.1%3Astable) ](https://bintray.com/bincrafters/public-conan/Boost.Build%3Abincrafters/1.65.1%3Astable/link)

[Conan.io](https://conan.io) package for [Boost.Build](https://github.com/boostorg/build) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/conan-public/Boost.Build%3Abincrafters).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload Boost.Build/1.65.1@bincrafters/stable --all

## Reuse the packages

### Basic setup

    $ conan install Boost.Build/1.65.1@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Build/1.65.1@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* with all the paths and variables that you need to link with your dependencies.

### License
[Boost](www.boost.org/LICENSE_1_0.txt)
