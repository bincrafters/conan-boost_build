from conans import ConanFile, tools, os


class BoostBuildConan(ConanFile):
    name = "Boost.Build"
    version = "1.65.1"
    url = "https://github.com/boostorg/build"
    description = "Boost.Build makes it easy to build C++ projects, everywhere"
    license = "www.boost.org/users/license.html"
    settings = "os", "arch"
    lib_short_names = ["build"]
          
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def build(self):
        command = "bootstrap" if self.settings.os == "Windows" else "./bootstrap.sh"
        build_dir = os.path.join(self.source_folder, "build")
        vscmd_path = os.path.join(build_dir, "src", "engine")
        os.chdir(build_dir)
        
        with tools.environment_append({"VSCMD_START_DIR": vscmd_path}):
            try:
                self.run(command)
            except:
                if self.settings.os == "Windows":
                    read_cmd = "type"
                else:
                    read_cmd = "cat"
                self.run("{0} bootstrap.log".format(read_cmd))
                raise

        command = "b2" if self.settings.os == "Windows" else "./b2"
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
