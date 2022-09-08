#include "definition.h"
#include "../generic_utils/type_utils.hpp"

extern "C" int CSVProcessor___init__(CSVProcessorObject *self, PyObject *args,
                                     PyObject *kwargs) {
  if (!PyArg_ParseTuple(args, "sssO",
                        &self->escaping_delimiter,  // str
                        &self->field_delimiter,     // str
                        &self->line_terminator,     // str
                        &self->mode                 // CSVProcessorMode
                        )) {
    return -1;
  }
  
  // TODO: If possible, omit param no.2
  raise_if_mistyped(self->escaping_delimiter, "escaping_delimiter", "str");
  raise_if_mistyped(self->field_delimiter, "field_delimiter", "str");
  raise_if_mistyped(self->line_terminator, "line_terminator", "str");
  raise_if_mistyped(self->mode, "mode", "CSVProcessorMode");

  return 0;
}