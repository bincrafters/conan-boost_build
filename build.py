#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_installer
from bincrafters import build_shared

if __name__ == "__main__":

    builder = build_template_installer.get_builder()
    builder.add({"os" : build_shared.get_os(), "arch" : "x86"}, {}, {}, {})
    builder.add({"os" : build_shared.get_os(), "arch" : "x86_64"}, {}, {}, {})
    builder.run()

