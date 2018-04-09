from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager(remotes=["https://api.bintray.com/conan/bincrafters/public-conan"])
    builder.add_common_builds(pure_c=True, shared_option_name="ZenGitHub:shared")
    builder.run()
