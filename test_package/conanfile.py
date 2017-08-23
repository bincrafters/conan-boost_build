from conans import ConanFile

class B2TestConan(ConanFile):
    generators = "txt"
    settings = "os", "arch"

    def build(self):
        pass

    def test(self):
        self.run("b2 -v")
