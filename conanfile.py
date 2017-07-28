"""Conan.io recipe for Boost.Build
"""
from conans import ConanFile, tools


class BoostBuildConan(ConanFile):
    """Checkout Boost.Build, build and create package
    """
    name = "Boost.Build"
    version = "1.64.0"
    generators = "txt"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/boostorg/build"
    src_folder = "git_src"
    FOLDER_NAME = "boost_%s" % version.replace(".", "_")

    def source(self):
        self.run("git clone --depth=50 --branch=boost-%s %s.git %s" % (self.version, self.url, self.FOLDER_NAME))

    def build(self):
        command = "bootstrap" if self.settings.os == "Windows" else "./bootstrap.sh"
        flags = []
        if self.settings.os == "Windows" and self.settings.compiler == "gcc":
            command += " mingw"
            flags.append("--layout=system")
        if self.settings.compiler == "Visual Studio":
            flags.append("toolset=msvc-%s.0" % self.settings.compiler.version)
        elif str(self.settings.compiler) in ["clang", "gcc"]:
            flags.append("toolset=%s"% self.settings.compiler)

        try:

            self.run("cd %s && %s" % (self.FOLDER_NAME, command))
        except:
            self.run("cd %s && type bootstrap.log" % self.FOLDER_NAME
                     if self.settings.os == "Windows"
                     else "cd %s && cat bootstrap.log" % self.FOLDER_NAME)
            raise

        cxx_flags = []

        # LIBCXX DEFINITION FOR BOOST B2
        try:
            if str(self.settings.compiler.libcxx) == "libstdc++":
                flags.append("define=_GLIBCXX_USE_CXX11_ABI=0")
            elif str(self.settings.compiler.libcxx) == "libstdc++11":
                flags.append("define=_GLIBCXX_USE_CXX11_ABI=1")
            if "clang" in str(self.settings.compiler):
                if str(self.settings.compiler.libcxx) == "libc++":
                    cxx_flags.append("-stdlib=libc++")
                    cxx_flags.append("-std=c++11")
                    flags.append('linkflags="-stdlib=libc++"')
                else:
                    cxx_flags.append("-stdlib=libstdc++")
                    cxx_flags.append("-std=c++11")
        except:
            pass

        cxx_flags = 'cxxflags="%s"' % " ".join(cxx_flags) if cxx_flags else ""
        flags.append(cxx_flags)

        # JOIN ALL FLAGS
        b2_flags = " ".join(flags)

        command = "b2" if self.settings.os == "Windows" else "./b2"

        full_command = "cd %s && %s %s --abbreviate-paths" % (
            self.FOLDER_NAME,
            command,
            b2_flags)
        self.output.warn(full_command)

        self.run(full_command)


