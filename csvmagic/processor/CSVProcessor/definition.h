#ifndef _CSVPROCESSOR_DEFINITION_H
#define _CSVPROCESSOR_DEFINITION_H

#include "../dependencies.h"

typedef struct {
  PyObject_HEAD  // noqa

  const PyObject *escaping_delimiter;
  const PyObject *field_delimiter;
  const PyObject *line_terminator;
  const PyObject *mode;
} CSVProcessorObject;

PyObject *CSVProcessor_parse_from_string(CSVProcessorObject *self,
                                         PyObject *args);

int CSVProcessor___init__(CSVProcessorObject *self, PyObject *args,
                          PyObject *kwargs);

extern PyTypeObject CSVProcessor;

#endif  // _CSVPROCESSOR_DEFINITION_H
