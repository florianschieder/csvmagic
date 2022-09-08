#include "definition.h"

// TODO: implement constructor
// TODO: add `NotImplemented` stub for `CSVProcessor.parse_from_string(str)`
PyTypeObject CSVProcessorType = {
    PyVarObject_HEAD_INIT(NULL, 0)  // noqa

    .tp_name = "CSVProcessor",  // XXX NOTE relevant for module.c
    .tp_doc = PyDoc_STR("Parses data out of a CSV document."),
    .tp_basicsize = sizeof(CSVProcessorObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
};
