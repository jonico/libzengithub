from conans import ConanFile, CMake, tools
import os


class ZenGithubConan(ConanFile):
    name = "ZenGitHub"
    version = "1.0"
    license = "Apache 2.0"
    url = "https://github.com/jonico/libzengithub"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "zengithub/*"
    requires = "libcurl/7.50.3@lasote/stable", "zlib/1.2.8@conan/stable"

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake zengithub %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="zengithub")
        self.copy("*zengithub.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["zengithub"]
