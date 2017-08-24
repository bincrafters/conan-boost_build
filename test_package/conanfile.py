from conans import ConanFile

class B2TestConan(ConanFile):
    settings = "os", "arch"

    def build(self):
        pass
    
    def imports(self):
        self.copy("jamroot.jam", dst=".", src=self.conanfile_directory)

    def test(self):
        self.run("b2 --debug-configuration")
