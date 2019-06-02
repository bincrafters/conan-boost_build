#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os
import shutil


class BoostBuildConan(ConanFile):
    name = "boost_build"
    version = "1.70.0"
    url = "https://github.com/bincrafters/conan-boost_build"
    description = "boost_build makes it easy to build C++ projects, everywhere"
    license = "BSL-1.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    settings = "os_build", "arch_build"
    lib_short_names = ["build"]
    exports_sources = "*.jam"

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version
        # archive_name = "master"
        for lib_short_name in self.lib_short_names:
            tools.get(
                "{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)
        shutil.copyfile(
            'os.jam',
            os.path.join('build', 'src', 'util', 'os.jam'))

    def build(self):
        use_windows_commands = os.name == 'nt'
        command = "bootstrap" if use_windows_commands else "./bootstrap.sh"
        build_dir = os.path.join(self.source_folder, "build")
        vscmd_path = os.path.join(build_dir, "src", "engine")
        os.chdir(build_dir)

        with tools.environment_append({"VSCMD_START_DIR": vscmd_path}):
            try:
                self.run(command)
            except:
                read_cmd = "type" if use_windows_commands else "cat"
                self.run("{0} bootstrap.log".format(read_cmd))
                raise

        command = "b2" if use_windows_commands else "./b2"
        full_command = "{0} --prefix=../output --abbreviate-paths".format(command)
        self.run(full_command)

    def package(self):
        self.copy(pattern="*b2", dst="", src="output")
        self.copy(pattern="*b2.exe", dst="", src="output")
        self.copy(pattern="*.jam", dst="", src="output")

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
        self.env_info.path = [os.path.join(self.package_folder, "bin")] + self.env_info.path
        self.env_info.BOOST_BUILD_PATH = os.path.join(self.package_folder, "share", "boost-build", "src", "kernel")
