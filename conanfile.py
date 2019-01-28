#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostStatic_AssertConan(base.BoostBaseConan):
    name = "boost_static_assert"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_static_assert"
    lib_short_names = ["static_assert"]
    header_only_libs = ["static_assert"]
    b2_requires = ["boost_config"]
