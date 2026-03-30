#include <pybind11/pybind11.h>
#include "math_ops.hpp"

namespace py = pybind11;

PYBIND11_MODULE(mars_core, m) {
    m.def("add", &add);
    m.def("subtract", &subtract);
    m.def("multiply", &multiply);
    m.def("divide", &divide);
}
