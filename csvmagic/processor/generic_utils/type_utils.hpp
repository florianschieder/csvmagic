#include <Python.h>
#include <string>

void raise_if_mistyped(PyObject *object,
                       const std::string& var_name,
                       const std::string& type_name) noexcept(true);