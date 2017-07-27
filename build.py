"""This script build Conan.io package to multiple platforms."""
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing")
    builder.run()
