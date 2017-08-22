from conans import ConanFile

class B2TestConan(ConanFile):
    name = "B2Test"
    version = "1"
    generators = "txt"
    settings = "os", "arch"

    def build(self):
        pass

    def test(self):
        self.run("b2 -v")
