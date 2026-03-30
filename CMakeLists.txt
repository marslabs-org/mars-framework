cmake_minimum_required(VERSION 3.15...3.29)
project(mars_framework LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(core_lib STATIC core/src/math_ops.cpp)
target_include_directories(core_lib PUBLIC core/include)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(mars_core bindings/python/src/bindings.cpp)
target_link_libraries(mars_core PRIVATE core_lib)

install(TARGETS mars_core DESTINATION .)
