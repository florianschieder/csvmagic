from .exceptions import IncompleteBuilderConfigurationException
from .processor import CSVProcessor


class Builder:
    def __init__(self):
        self._fields = {
            "escaping_delimiter": None,
            "field_delimiter": None,
            "line_terminator": None,
            "mode": None,
        }

    # RFC 4180
    _defaults = {
        "escaping_delimiter": '"',
        "field_delimiter": ",",
        "line_terminator": "\r\n",
    }

    def use_mode(self, mode):
        self._fields["mode"] = mode
        return self

    def use_line_terminator(self, terminator):
        self._fields["line_terminator"] = terminator
        return self

    def use_field_delimiter(self, delimiter):
        self._fields["field_delimiter"] = delimiter
        return self

    def use_escaping_delimiter(self, delimiter):
        self._fields["escaping_delimiter"] = delimiter
        return self

    def apply_defaults(self):
        Self = type(self)
        self._fields = {
            **self._fields,
            **Self._defaults,
        }
        return self

    def get_instance(self):
        self._check_if_fields_are_complete()
        return CSVProcessor(**self._fields)

    def _check_if_fields_are_complete(self):
        incomplete_fields = filter(
            lambda value: value is None,
            self._fields.values(),
        )
        if tuple(incomplete_fields):
            raise IncompleteBuilderConfigurationException(
                ", ".join(incomplete_fields)
            )
