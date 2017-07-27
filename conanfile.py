"""Conan.io recipe for Boost.Build
"""
from conans import ConanFile, tools
from os import path
import subprocess

class BoostBuildConan(ConanFile):
    """Checkout Boost.Build, build and create package
    """
    name = "Boost.Build"
    version = "1.64.0"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    url = "https://github.com/boostorg/build"

    def source(self):
        self.run("git clone --depth=50 --branch=v%s %s.git %s" % (self.version, self.url, self.cpprestsdk_dir))

    def build(self):


    def package(self):


    def package_info(self):
