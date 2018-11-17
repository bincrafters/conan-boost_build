#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class TestPackgeConan(ConanFile):
    settings = "os", "arch"
    
    def test(self):
        tools.save("jamroot.jam", "ECHO info: Success loading project jamroot.jam file. ;")
        self.run("b2 --debug-configuration")
