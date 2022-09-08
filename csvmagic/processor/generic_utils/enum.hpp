#ifndef CSVMAGIC_PROCESSOR_GENERIC_UTILS_ENUM_HPP_
#define CSVMAGIC_PROCESSOR_GENERIC_UTILS_ENUM_HPP_

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

#include <string>
#include <vector>

PyObject *make_int_enum(const std::string &type_name,
                        const std::vector<std::string> &choices) noexcept(true);

#endif  // CSVMAGIC_PROCESSOR_GENERIC_UTILS_ENUM_HPP_
