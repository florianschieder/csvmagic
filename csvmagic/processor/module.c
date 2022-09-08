#include "CSVProcessor/definition.h"
#include "CSVProcessorMode/definer.hpp"
#include "dependencies.h"

static PyModuleDef CSVProcessorModule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "processor",
    .m_doc = "Example module that creates an extension type.",
    .m_size = -1,
};

// TODO After everything is finalized, overthink if helper functions
// or macros are appropriate.
PyMODINIT_FUNC PyInit_processor() {
  if (PyType_Ready(&CSVProcessorType) < 0) {
    return NULL;
  }

  PyObject *module = PyModule_Create(&CSVProcessorModule);
  if (module == NULL) {
    return NULL;
  }

  Py_INCREF(&CSVProcessorType);
  if (PyModule_AddObject(module, "CSVProcessor",
                         (PyObject *)&CSVProcessorType) < 0) {
    Py_DECREF(&CSVProcessorType);
    Py_DECREF(module);
    return NULL;
  }

  PyObject *CSVProcessorMode = define_CSVProcessorMode();
  if (PyModule_AddObject(module, "CSVProcessorMode", CSVProcessorMode) < 0) {
    Py_DECREF(&CSVProcessorMode);
    Py_DECREF(module);
    return NULL;
  }

  return module;
}
