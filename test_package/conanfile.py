#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class TestPackgeConan(ConanFile):
    settings = "os", "arch"
    
    def test(self):
        tools.save("jamroot.jam", "ECHO info: Success loading project jamroot.jam file. ;")
        self.run("b2 --debug-configuration")
