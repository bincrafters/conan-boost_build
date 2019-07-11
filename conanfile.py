#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
import shutil


class BoostBuildConan(ConanFile):
    name = "boost_build"
    version = "4.0.0"
    url = "https://github.com/bincrafters/conan-boost_build"
    description = "boost_build makes it easy to build C++ projects, everywhere"
    license = "BSL-1.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    settings = "os_build", "arch_build"
    lib_short_names = ["build"]
    exports_sources = "*.jam"

    def source(self):
        tools.get(
            "https://github.com/boostorg/build/archive/{0}.tar.gz"
            .format(self.version))
        os.rename("build-" + self.version, 'b2')

    def build(self):
        use_windows_commands = os.name == 'nt'
        command = "build" if use_windows_commands else "./build.sh"
        build_dir = os.path.join(self.source_folder, "b2")
        engine_dir = os.path.join(build_dir, "src", "engine")
        os.chdir(engine_dir)
        with tools.environment_append({"VSCMD_START_DIR": os.curdir}):
            self.run(command)
        os.chdir(build_dir)
        command = os.path.join(
            engine_dir, "b2.exe" if use_windows_commands else "b2")
        full_command = \
            "{0} --prefix=../output --abbreviate-paths install".format(
                command)
        self.run(full_command)

    def package(self):
        self.copy(pattern="*b2", dst="", src="output")
        self.copy(pattern="*b2.exe", dst="", src="output")
        self.copy(pattern="*.jam", dst="", src="output")

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
        self.env_info.path = [os.path.join(
            self.package_folder, "bin")] + self.env_info.path
        self.env_info.BOOST_BUILD_PATH = os.path.join(
            self.package_folder, "share", "boost-build", "src", "kernel")
