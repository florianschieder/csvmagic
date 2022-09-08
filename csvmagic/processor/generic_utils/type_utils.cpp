#include "type_utils.hpp"

void raise_if_mistyped(PyObject *object,
                       const std::string& var_name,
                       const std::string& type_name) noexcept(true) {
  PyObject *type = PyObject_Type(object);
  
  // Determine actual type name
  PyObject *__name__ = PyObject_GetAttrString(type, "__name__");
  PyObject *actual_type_name_encoded = PyUnicode_AsUTF8String(__name__);
  const char *actual_type_name = PyBytes_AsString(actual_type_name_encoded);
  
  if (type_name != std::string(actual_type_name)) {
      std::string error_message("");
      error_message += var_name;  // TODO `object.__name__` if appropriate
      error_message += ": ";
      error_message += actual_type_name;
      
      PyErr_SetString(PyExc_TypeError, error_message.c_str());
  }

  Py_DECREF(type);
  Py_DECREF(__name__);
  Py_DECREF(actual_type_name_encoded);  // + deallocates `actual_type_name`
}