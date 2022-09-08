#include "enum.hpp"

/*
 * Instantiates a new Python enum.
 *
 * Example:
 *   std::vector<std::string> choices = {"FOO", "BAR"};
 *   PyObject *MyEnum = make_int_enum("MyEnum", choices);
 *
 * Would be equivalent to:
 *   class MyEnum(Enum):
 *       FOO = 0
 *       BAR = 1
 *
 * This is achieved by emulating the following python call:
 *   MyEnum = Enum("MyEnum", {"FOO": 0, "BAR": 1})
 *
 * Return value: New reference.
 */
PyObject *make_int_enum(
    const std::string &type_name,
    const std::vector<std::string> &choices) noexcept(true) {
  PyObject *attrs = PyDict_New();

  unsigned int i = 0;
  for (auto const &choice : choices) {
    PyObject *key = PyUnicode_FromString(choice.c_str());
    PyObject *val = PyLong_FromLong(i);
    PyObject_SetItem(attrs, key, val);

    Py_DECREF(key);
    Py_DECREF(val);
    i++;
  }

  PyObject *name = PyUnicode_FromString(type_name.c_str());
  PyObject *args = PyTuple_Pack(2, name, attrs);

  Py_DECREF(attrs);
  Py_DECREF(name);

  PyObject *enum_module = PyImport_ImportModule("enum");
  PyObject *EnumBaseClass = PyObject_GetAttrString(enum_module, "Enum");
  PyObject *EnumSubClass = PyObject_CallObject(EnumBaseClass, args);

  Py_DECREF(args);
  Py_DECREF(enum_module);
  Py_DECREF(EnumBaseClass);

  return EnumSubClass;
}
