#ifndef _CSVPROCESSOR_DEFINITION_H
#define _CSVPROCESSOR_DEFINITION_H

#include "../dependencies.h"

typedef struct {
  PyObject_HEAD  // noqa

  PyObject *escaping_delimiter;
  PyObject *field_delimiter;
  PyObject *line_terminator;
  PyObject *mode;
} CSVProcessorObject;

PyObject *CSVProcessor_parse_from_string(CSVProcessorObject *self,
                                         PyObject *args);

#ifdef __cplusplus
extern "C" {
#endif

int CSVProcessor___init__(CSVProcessorObject *self, PyObject *args,
                          PyObject *kwargs);
#ifdef __cplusplus
}  // extern "C"
#endif 

extern PyTypeObject CSVProcessor;

#endif  // _CSVPROCESSOR_DEFINITION_H
