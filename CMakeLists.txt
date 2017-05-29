project(Zen)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(zen zen.c)
target_link_libraries(zen ${CONAN_LIBS})

TARGET_LINK_LIBRARIES(zen ${CONAN_LIBS})
