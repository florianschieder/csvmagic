#ifndef _CSVPROCESSOR_DEFINITION_H
#define _CSVPROCESSOR_DEFINITION_H

#include "../dependencies.h"

typedef struct {
  PyObject_HEAD
  /* Type-specific fields go here. */
} CSVProcessorObject;

extern PyTypeObject CSVProcessorType;

#endif  // _CSVPROCESSOR_DEFINITION_H