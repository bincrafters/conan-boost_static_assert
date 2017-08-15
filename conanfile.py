from conans import ConanFile, tools, os

class BoostStatic_AssertConan(ConanFile):
    name = "Boost.Static_Assert"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-static_assert"
    source_url = "https://github.com/boostorg/static_assert"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["static_assert"]
    requires = "Boost.Config/1.64.0@bincrafters/testing"
    
    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()