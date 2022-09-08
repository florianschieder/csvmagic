#include "definer.hpp"

#include <string>
#include <vector>

#include "../generic_utils/enum.hpp"

extern "C" PyObject *define_CSVProcessorMode() {
  std::vector<std::string> choices = {"DICT"};
  return make_int_enum("CSVProcessorMode", choices);
}
