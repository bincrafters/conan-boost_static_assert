#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostStatic_AssertConan(base.BoostBaseConan):
    name = "boost_static_assert"
    url = "https://github.com/bincrafters/conan-boost_static_assert"
    lib_short_names = ["static_assert"]
    header_only_libs = ["static_assert"]
    b2_requires = [
        "boost_config",
    ]


