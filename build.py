from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(remotes=["https://api.bintray.com/conan/bincrafters/public-conan"], build_policy="missing")
    builder.add_common_builds(pure_c=True, shared_option_name="ZenGitHub:shared")
    # for some reason arm fails to link shared against openssl static build
    builder.remove_build_if(lambda build: build.settings['arch'].startswith("arm") and build.options['ZenGitHub:shared'] == True)
    builder.run()
