from conans import ConanFile, CMake


class ZenGithubConan(ConanFile):
    name = "ZenGitHub"
    version = "1.0"
    license = "Apache 2.0"
    url = "https://github.com/jonico/libzengithub"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "no_asm": [True, False]}
    default_options = "shared=True", "no_asm=False"
    generators = "cmake"
    exports_sources = "zengithub/*"
    requires = "libcurl/7.64.1@bincrafters/stable"

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="zengithub")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="zengithub")
        self.copy("*zengithub.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["zengithub"]
