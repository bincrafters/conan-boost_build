"""Conan.io recipe for Boost.Build
"""
from conans import ConanFile, tools, os

class BoostBuildConan(ConanFile):
    """Checkout Boost.Build, build and create package
    """
    name = "Boost.Build"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/build"
    description = "Boost.Build makes it easy to build C++ projects, everywhere"
    license = "www.boost.org/users/license.html"
    folder_name = "boost_{0}".format(version.replace(".", "_"))
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git {2}"
                 .format(self.version, self.url, self.folder_name))

    def build(self):
        command = "bootstrap" if self.settings.os == "Windows" else "./bootstrap.sh"
        flags = []
        if self.settings.os == "Windows" and self.settings.compiler == "gcc":
            command += " mingw"
            flags.append("--layout=system")

        build_path_full = os.path.join(self._conanfile_directory, self.folder_name)
        vscmd_path_full = os.path.join(build_path_full, "src", "engine")
        with tools.environment_append({"VSCMD_START_DIR": vscmd_path_full}):
            try:
                self.run(command, cwd=build_path_full)
            except:
                if self.settings.os == "Windows":
                    read_cmd = "type"
                else:
                    read_cmd = "cat"
                self.run("{0} bootstrap.log".format(read_cmd))
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

        cxx_flags = 'cxxflags="{0}"'.format(" ".join(cxx_flags) if cxx_flags else "")
        flags.append(cxx_flags)

        # JOIN ALL FLAGS
        b2_flags = " ".join(flags)
        command = "b2" if self.settings.os == "Windows" else "./b2"
        full_command = "{0} {1} --abbreviate-paths".format(command, b2_flags)
        self.output.warn(full_command)
        self.run(full_command, cwd=self.folder_name)

    def package(self):
        release_dir = path.join(self.folder_name, "Release")
        self.copy(pattern="*.h", dst="include", src=path.join(release_dir, "include"))
        self.copy(pattern="*.hpp", dst="include", src=path.join(release_dir, "include"))
        self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)