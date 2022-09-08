#include "definition.h"

int CSVProcessor___init__(CSVProcessorObject *self, PyObject *args,
                          PyObject *kwargs) {
  if (!PyArg_ParseTuple(args, "sssO",
                        &self->escaping_delimiter,  // str
                        &self->field_delimiter,     // str
                        &self->line_terminator,     // str
                        &self->mode                 // CSVProcessorMode
                        )) {
    return -1;
  }
  // TODO do type checking!
  return 0;
}
