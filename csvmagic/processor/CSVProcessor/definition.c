#include "definition.h"

PyMethodDef CSVProcessor_methods[] = {
    {"parse_from_string", (PyCFunction)CSVProcessor_parse_from_string,
     METH_VARARGS, "Parses a CSV document from a string"},
    {NULL}  // Sentinel
};

PyTypeObject CSVProcessor = {
    PyVarObject_HEAD_INIT(NULL, 0)  // noqa

    .tp_name = "CSVProcessor",  // XXX NOTE relevant for module.c
    .tp_doc = PyDoc_STR("Parses data out of a CSV document."),
    .tp_basicsize = sizeof(CSVProcessorObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,

    .tp_init = (initproc)CSVProcessor___init__,
    .tp_methods = CSVProcessor_methods,
};
